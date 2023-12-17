from django.urls import path,include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('a/', custom_admin_index.as_view()),
    path('',products_page.as_view()),
    path('cart/',cartView.as_view()),
    path('login',loginView.as_view()),
    path('logout',logoutView.as_view()),
    path('add_to_cart/<int:product_id>/<str:type>/',ProductToCart.as_view()),
    path('api/products/',productsApi.as_view()),
    path('api/add_to_cart/',addProductCart.as_view())
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

