from django.urls import path
from .import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('detail/<int:pk>/', views.post_detail, name='post_detail'),
    # post/new/ 인데 edit으로 경로 설정
    path('new/', views.post_new, name='post_new'),
    path('detail/edit/<int:pk>/', views.post_edit, name='post_edit'),
    path('profile/', views.profile, name='profile'),
]
