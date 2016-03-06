# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Item
from category.serializers import CategoryHyperlinkedSerializer


class ItemListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Item
        fields = ('url', 'item_name', 'item_receipt_date', 'item_capture')


class ItemSerializer(serializers.ModelSerializer):

    item_category = serializers.HyperlinkedRelatedField(
        read_only=True,
        view_name='category-detail'
    )

    class Meta:
        model = Item
