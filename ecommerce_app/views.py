from django.shortcuts import render,redirect
from django.views import View
from django.http import HttpResponse
from django.contrib.auth import logout,authenticate,login
from .models import *
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializer import *
# Create your views here.

class products_page(View):
    def get(self,request):
        products_data = Products.objects.exclude(delete_flag=True).all()
        total_quantity_number = 0
        if request.user.is_authenticated:
            cart_data = Cart.objects.filter(user = request.user).exclude(delete_flag=True).values('product_id_id','quantity')
            products_quantity = {row["product_id_id"]:row["quantity"] for row in cart_data}
            for row in products_data:
                row.quantity = products_quantity.get(row.id,0)
            total_quantity_number = sum(list(products_quantity.values()))
            user_request_count = userRequestCountTrack.objects.get(user = request.user)
        return render(request,'homepage.html',locals())
class ProductToCart(View):
    def get(self,request,product_id,type):
        product_data = Cart.objects.get_or_create(user = request.user, product_id = Products.objects.get(id=product_id))[0]
        if type=='add':
            product_data.quantity+=1
        elif type=='sub':
            product_data.quantity-=1
        product_data.save()
        redirect_url = '/'+request.GET.get('redirect_url','')
        # print(redirect_url)
        return redirect(redirect_url)

class cartView(View):
    def get(self,request):
        if request.user.is_authenticated:
            products_data = list(Cart.objects.filter(quantity__gt = 0,user = request.user).all())
            total_quantity = 0
            total_price = 0
            for data in products_data:
                data.total_price = int(data.quantity*data.product_id.cost)
                total_price +=data.total_price
                total_quantity+=data.quantity
            products_data.sort(reverse = True, key = lambda x:x.total_price)
            return render(request,"cart.html",locals())

        
        else:
            return redirect('/login')




class loginView(View):
    def get(self,request):
        message = ''
        return render(request,'loginPage.html',locals())
    def post(self,request):
        request_data = request.POST
        username = request_data.get('username','')
        password = request_data.get('password','')
        user = authenticate(request,username = username,password = password)
        # print(user)
        # print(username,password)
        is_banned = len(list(banned_users.objects.filter(user__username = username).values()))
        # print(is_banned)
        if user:
            login(request,user)
            obj = userRequestCountTrack.objects.get_or_create(user = request.user)[0]
            # banned_users.objects.create(user = request.user)
            obj.request_count +=1
            obj.save()
            return redirect('/')
        else:
            message = 'Invalid Username or Password'
            if is_banned>0:
                message = "You are banned to login"
            return render(request,'loginPage.html',locals())
class logoutView(View):
    def get(self,request):
        logout(request)
        return redirect('/')
    
class productsApi(APIView):

    def get(self,request):
        query_data = Products.objects.exclude(delete_flag=True).values()
        serializer = products_data_serializer(query_data,many = True)
        return Response(serializer.data)

    def post(self,request):
        post_data = request.data
        data = {}
        data['name'] = post_data.get('name','No Name')
        # print(data['name'])
        data['cost'] = post_data.get('cost',0)
        data['description'] = post_data.get('description','')
        data['image'] = request.FILES['file']
        obj = Products.objects.get(id = id)
        serializer = products_data_serializer(data=data,instance=obj)
        if serializer.is_valid():
            serializer.save()
            return Response({'status':'Success'},status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class addProductCart(APIView):
    def post(self,request):
        post_data = request.data
        try:
            product_id = int(post_data['product_id'])
            quantity = int(post_data['quantity'])
            cart_obj = Cart.objects.get(user=request.user,product_id = Products.objects.get(id = product_id))
            if quantity<0 and abs(quantity)<cart_obj.quantity:
                print(quantity,cart_obj.quantity)
                raise Exception
            if cart_obj:
                cart_obj.quantity+=quantity
                cart_obj.save()
            return Response({"status":"success"},status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({'status':'Got Error','error':str(e)})
from django.urls import reverse
from django.contrib import admin
from django.apps import apps
class custom_admin_index(View):
    def get(self,request):
        app_list = []
        for app in admin.site.get_app_list(request):
            models = []
            for model in app['models']:
                app_label = apps.get_containing_app_config(model._meta.app_label).name
                model_name = model._meta.model_name
                # print(model)
                model_admin_url = reverse('admin:%s_%s_changelist' % (app_label, model_name))
                models.append({
                    'name': model['name'],
                    'admin_url': model_admin_url,
                })
            app_list.append({
                'name': app['name'],
                'models': models,
            })

        context = {
            'app_list': app_list,
        }
        return render(request, 'admin_extend.html', context)

        