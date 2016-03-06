# -*- coding: utf-8 -*-
from rest_framework import serializers
from .models import Category


class CategoryHyperlinkedSerializer(serializers.ModelSerializer):

    items = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='item-detail'
    )

    class Meta:
        model = Category


class CategoryListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Category
        fields = ('url', 'category_title', 'category_capture')
