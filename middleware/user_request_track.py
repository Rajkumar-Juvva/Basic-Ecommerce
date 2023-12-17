from ecommerce_app.models import userRequestCountTrack
class user_request_tracking:
    def __init__(self,get_response) -> None:
        self.get_response = get_response
    def __call__(self,request):
        if request.user.is_authenticated:
            # obj = userRequestCountTrack.objects.get_or_create(user = request.user)[0]

            # # print(obj)
            # obj.request_count+=1
            # obj.save()
            pass
        #request
        response  = self.get_response(request)

        return response
    def process_exception(self,request,exception):
        