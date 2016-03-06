from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import generics
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response

from .permissions import IsOwnerOrReadOnly
from .serializers import (
    UserDetailSerializer,
    UserListSerializer,
    UserCreateSerializer
)

# Create your views here.

class CreateUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = (permissions.AllowAny,)


class UserAPIView(generics.RetrieveUpdateAPIView):
    """
    Updates, and retrives User accounts
    """
    queryset = User.objects.all()
    serializer_class = UserDetailSerializer
    permission_classes = (IsOwnerOrReadOnly,)

class OwnerAPIView(APIView):
    # permission_classes = (permissions.IsAuthenticated,)

    def get_object(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        if request.user:
            owner = self.get_object(request.user.pk)
            print(request.user.pk)
            serializer = UserDetailSerializer(owner)
            return Response(serializer.data)
