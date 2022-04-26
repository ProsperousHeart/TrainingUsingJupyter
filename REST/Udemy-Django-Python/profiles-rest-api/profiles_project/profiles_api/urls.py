# from django.conf.urls import url
from django.urls import path
# from . import views
from profiles_api import views

urlpatterns = [
    # url(r'^hello-view/', views.HelloAPIView.as_view()),
    path('hello-view/', views.HelloAPIView.as_view()),
]
