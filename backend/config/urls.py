from django.contrib import admin
from django.urls import path

from rest_framework_swagger.views import get_swagger_view

scema_view = get_swagger_view(title="Two DEMO API")

urlpatterns = [path("admin/", admin.site.urls), path("swagger/", scema_view)]
