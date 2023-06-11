from rest_framework import views, response, exceptions, permissions
from .serializers import UserSerializer
from . import services
from . import authentication
# Create your views here.

class RegisterApi(views.APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        data = serializer.validated_data
        serializer.instance = services.UserDataClass.create_user(user_dc=data)
        print(data)
        return response.Response({"Hello": "world"})
    
class LoginApi(views.APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = services.user_email_selector(email=email)
        if user is None:
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        
        if not user.check_password(raw_password=password):
            raise exceptions.AuthenticationFailed("Invalid Credentials")
        
        token = services.create_token(userid=user.id)

        resp = response.Response()
        resp.set_cookie(key = "jwt", value = token, httponly=True)
        return resp
class UserApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication, )
    permission_classes = (permissions.IsAuthenticated, )

    def get(self, request):
        user = request.user
        serializer = UserSerializer(user)
        return response.Response(serializer.data)

class LogoutApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated, )
    def post(self, requst):
        resp = response.Response()
        resp.delete_cookie("jwt")
        resp.data = {"message": "you are logged out"}
        return resp