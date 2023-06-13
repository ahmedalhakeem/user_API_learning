from rest_framework import views, response, permissions
from user import authentication
from . import serializers as status_serializer
from . import services
from rest_framework import status as rest_status
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

    def get(self, request, status_id):
        status_detail = services.user_status_detail(user=request.user, status_id=status_id)
        serializer = status_serializer.StatusSerializer(status_detail)
        return response.Response(data=serializer.data)
    def delete(self, request, status_id):
        status = services.delete_user_status(user=request.user, status_id=status_id)
        serializer = status_serializer.StatusSerializer(status)
        return response.Response(status=rest_status.HTTP_204_NO_CONTENT)
    def put(self, request, status_id):
        serializer = status_serializer.StatusSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        status = serializer.validated_data
        serializer.instance = services.update_user_status(user=request.user, status_id=status_id, status_data=status)
        return response.Response(data=serializer.data)