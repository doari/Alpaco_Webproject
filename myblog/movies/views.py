# movies/views.py

from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .utils import get_movies_from_api
from post.forms import CommentForm  # CommentForm을 가져오도록 수정

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

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.movie = movie
            new_comment.save()
            return redirect('movie_detail', movie_id=movie_id)
    else:
        comment_form = CommentForm()

    return render(request, 'movies/movie_detail.html', {'movie': movie, 'comment_form': comment_form})