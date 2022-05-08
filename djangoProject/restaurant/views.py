from django.contrib.auth.models import User, Group
from rest_framework import viewsets, status
from rest_framework import permissions
from rest_framework.decorators import api_view
from rest_framework.response import Response

from djangoProject.restaurant.serialisers import UserSerializer, GroupSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]


@api_view(['GET'])
def upcoming(request):
    """
    Retrieve, update or delete a code snippet.
    """
    return Response("roasted chicken", status.HTTP_200_OK)
