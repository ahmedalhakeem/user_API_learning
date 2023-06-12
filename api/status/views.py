from rest_framework import views, response, permissions
from user import authentication
from . import serializers as status_serializer
from . import services
class StatusCreateListApi(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = status_serializer.StatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        data = serializer.validated_data
        serializer.instance = services.create_status(user=request.user ,status=data)
        return response.Response(data=serializer.data)

        
    def get(self, request):
        status_collection = services.status_per_user(user=request.user)
        serializer = status_serializer.StatusSerializer(status_collection, many=True)
        return response.Response(data=serializer.data)

class RetrieveUpdateDeleteStatus(views.APIView):
    authentication_classes = (authentication.CustomUserAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, pk):
        status_detail = services.user_status_detail(user=request.user, status_id=pk)
        serializer = status_serializer.StatusSerializer(status_detail)
        return response.Response(data=serializer.data)
    def delete(self, request):
        pass
    def put(self, request):
        pass