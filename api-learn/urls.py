#!/usr/bin/python
# -*- coding:utf-8 -*-
# Author:ChenXuhan
from django.urls import path, include
from rest_framework import routers
from django.views.decorators.csrf import csrf_exempt

from . import views

router = routers.DefaultRouter()
router.register('users', views.UserViewSet)
router.register('groups', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('user/', views.userDetail, name="userDetail"),
]
