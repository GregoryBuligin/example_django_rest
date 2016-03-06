# -*- coding: utf-8 -*-
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Category
from .serializers import CategoryHyperlinkedSerializer, CategoryListSerializer

# Create your views here.

# class CategoryViewSet(viewsets.ViewSet):
#     """
#     """
#     def list(self, request):
#         queryset = Category.objects.all()
#         serializer = CategoryListSerializer(queryset, context={'request': request}, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Category.objects.all()
#         category = get_object_or_404(queryset, pk=pk)
#         serializer = CategoryHyperlinkedSerializer(category, context={'request': request})
#         return Response(serializer.data)


class CategoryViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Category.objects.all()

    def get_serializer_class(self):
        if self.action == 'list':
            return CategoryListSerializer
        else:
            return CategoryHyperlinkedSerializer
