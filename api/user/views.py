from rest_framework import views, response, exceptions, permissions
from .serializers import UserSerializer
from . import services
# Create your views here.

class RegisterApi(views.APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.validated_data
        serializer.instance = services.UserDataClass.create_user(user_dc=data)
        print(data)
        return response.Response({"Hello": "world"})