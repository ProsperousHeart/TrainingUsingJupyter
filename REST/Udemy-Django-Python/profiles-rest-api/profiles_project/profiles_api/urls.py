# from django.conf.urls import url
from django.urls import path, include
# from . import views
from profiles_api import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

# register a new URL that points to our HelloViewSet
# input 1 - string is the URL you would like to use
# input 2 - name of the viewset we want to assign/register to the router
# input 3 - base name (used for retrieving URLs in Router)
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

# register the user profile ViewSet
router.register('profile', views.UserProfileViewSet)

urlpatterns = [
    # url(r'^hello-view/', views.HelloAPIView.as_view()),
    path('hello-view/', views.HelloAPIView.as_view()),
    path('', include(router.urls))
]
