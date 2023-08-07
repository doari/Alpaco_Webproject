# movies/views.py

from django.shortcuts import render
from .models import Movie
from .utils import get_movies_from_api

def movie_list(request):
    # API 키를 가져오거나 하드코딩한 뒤 사용합니다.
    api_key = "a208119c6e1268b59b1ac02b04dd5feb"
    
    # API를 통해 영화 정보 가져오기
    movies_data = get_movies_from_api(api_key)

    # 가져온 영화 정보를 데이터베이스에 저장
    for movie_data in movies_data:
        Movie.objects.get_or_create(
            title=movie_data["title"],
            overview=movie_data["overview"],
            release_date=movie_data["release_date"],
            poster_url="https://image.tmdb.org/t/p/w500" + movie_data["poster_path"]
        )

    # 모든 영화 레코드를 가져와서 템플릿에 전달
    movies = Movie.objects.all()
    
    return render(request, "movies/movie_list.html", {"movies": movies})