from rest_framework import routers
from django.urls import path, re_path

from posts import views

router = routers.DefaultRouter()
router.register(r'posts', views.PostList)
router.register(r'^users/$', views.UserList.as_view(), base_name='user_list')
router.register(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), base_name='user_detail')
router.register(r'presentation/', views.PresentationList)

urlpatterns = [
  path(r'users/', views.UserList.as_view()),
  re_path(r'users/(?P<pk>[0-9]+)/', views.UserDetail.as_view()),
  path(r'posts/', views.PostList.as_view()),
  path(r'presentation/', views.PresentationList.as_view()),
  path(r'main/', views.MainList.as_view()),
  path(r'', views.application, name='application'),
]

