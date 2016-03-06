# -*- coding: utf-8 -*-
import django_filters
from rest_framework import filters
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import list_route
from django.shortcuts import get_object_or_404
from .models import Item
from .serializers import ItemSerializer, ItemListSerializer

# Create your views here.

# class ItemViewSet(viewsets.ViewSet):
#     """
#     """
#
#     def list(self, request):
#         queryset = Item.objects.all()
#         serializer = ItemListSerializer(queryset, context={'request': request}, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = Item.objects.all()
#         item = get_object_or_404(queryset, pk=pk)
#         serializer = ItemSerializer(item, context={'request': request})
#         return Response(serializer.data)

class ItemViewSet(viewsets.ModelViewSet):
    """
    """
    queryset = Item.objects.all()
    # filter_backends = (filters.SearchFilter,)
    # search_fields = ('item_name',)
    filter_backends = (filters.OrderingFilter,)
    ordering_fields = ('item_name', 'id')
    # filter_backends = (filters.DjangoFilterBackend,)
    # filter_fields = ('item_name',)

    # def get_queryset(self):
    #     if self.action == "list":
    #         return Item.objects.all()#.values('pk', 'item_name', 'item_receipt_date', 'item_capture')
    #     else:
    #         return Item.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return ItemListSerializer
        else:
            return ItemSerializer
