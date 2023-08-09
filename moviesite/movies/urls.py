# movies/urls.py

from django.urls import path
from . import views

urlpatterns = [
    # 메인 페이지 (영화 목록 페이지)
    path('', views.movie_list, name='movie_list'),
    # 유명영화 페이지 (유명영화 목록 페이지)
    path('popular/', views.PopularMovieView.as_view(), name='popular-movies'),  
    # 유명영화 페이지 (유명영화 목록 페이지)
    path('now_play/', views.Now_Playing_MovieView.as_view(), name='now_play-movies'),
     
    # 유명영화 페이지 (유명영화 목록 페이지)
    path('toprate/', views.Top_Rated_View.as_view(), name='toprate-movies'),  
    # 유명영화 페이지 (유명영화 목록 페이지)
    path('upcoming/', views.Upcoming_MovieView.as_view(), name='upcoming-movies'),  
    # 영화 세부 정보 페이지
    path('movie/<int:movie_id>/', views.movie_detail, name='movie_detail'),
]
