from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from profiles_api import views 

router= DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, basename='hello-viewset')
router.register('profile', views.UserProfileViewSet)
router.register('feed', views.UserProfileFeedViewSet)
               
urlpatterns = [
    path('list-view/', views.ListView.as_view()),
    path('login/', views.UserLoginApiView.as_view()),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('', include(router.urls))
]


