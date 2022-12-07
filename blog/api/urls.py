from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('users/', views.UserList.as_view()),
    path('users/<str:pk>', views.UserDetail.as_view()),
    path('posts/', views.PostList.as_view()),
    path('posts/<str:pk>', views.PostDetail.as_view()),
    path('comments/', views.CommentList.as_view()),
    path('comments/<str:pk>', views.CommentDetail.as_view()),
    path('categories/', views.CategoryList.as_view()),
    path('categories/<str:pk>', views.CategoryDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)