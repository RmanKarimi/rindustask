from rest_framework.viewsets import ModelViewSet
from .serializers import UserSerializer, UserDataModelDetailSerializer, DataModelDetailSerializer
from .models import Profile
from utils.permissions import AllowAdminAndOwner, AllowOwner
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


class DataModelViewSet(ModelViewSet):
    serializer_class = DataModelDetailSerializer
    permission_classes = [AllowAdminAndOwner, IsAuthenticated]

    def perform_create(self, serializer, *args, **kwargs):
        serializer.save(**kwargs)


class UserDataModelViewSet(DataModelViewSet):
    serializer_class = UserDataModelDetailSerializer
    permission_classes = [AllowAdminAndOwner]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)

        response_data = {'success': True,
                         'msg': 'Data has been loaded successfully',
                         'results': serializer.data}
        return Response(response_data)

    def perform_create(self, serializer, *args, **kwargs):
        user = self.request.user
        kwargs['user'] = user
        super(UserDataModelViewSet, self).perform_create(serializer=serializer, **kwargs)


class UserViewSet(UserDataModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAdminAndOwner]
    http_method_names = ['get', 'put', 'post', 'delete']
