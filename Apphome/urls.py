from django.urls import path
from .views import index,api
urlpatterns=[
    path('',index,name="home"),
    path('api/v1/',api,name="api")
]