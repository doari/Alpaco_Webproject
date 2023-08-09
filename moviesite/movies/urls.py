# movies/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # 메인 페이지 (영화 목록 페이지)
    path('', views.movie_list, name='movie_list'),
    # 영화 세부 정보 페이지
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]
