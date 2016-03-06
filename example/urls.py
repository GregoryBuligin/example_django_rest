# -*- coding: utf-8 -*-
from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token

from authentication.views import UserAPIView, CreateUserView, OwnerAPIView
from category.views import CategoryViewSet
from item.views import ItemViewSet

router = routers.DefaultRouter()
router.register(r"items", ItemViewSet, base_name='item')
router.register(r"categories", CategoryViewSet, base_name='category')

v1_patterns = [
    url(r'^auth/', obtain_jwt_token),
    url(r'^register/', CreateUserView.as_view()),
    url(r'^me/$', OwnerAPIView.as_view()),
    url(r'^users/(?P<pk>[0-9]+)/$', UserAPIView.as_view()),
    url(r'^', include(router.urls))
]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/', include(v1_patterns, namespace='v1')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
