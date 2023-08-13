# movies/views.py

from django.db.models import Q # 검색기능
from django.shortcuts import render, get_object_or_404, redirect
from .models import Movie
from .utils import get_movies_from_api
from post.forms import CommentForm  # CommentForm을 가져오도록 수정
from django.views.generic import TemplateView




def movie_list(request):
    # API 키를 가져오거나 하드코딩한 뒤 사용합니다.
    api_key = "a208119c6e1268b59b1ac02b04dd5feb"
    api_endpoints = [
        {"endpoint": "movie/popular", "name": "인기 영화"},
        {"endpoint": "movie/now_playing", "name": "현재 상영 영화"},
        {"endpoint": "movie/top_rated", "name": "높은 평점 영화"},
    ]
    movies_list = []

    for api_info in api_endpoints:
        endpoint = api_info["endpoint"]
        params = {"language": "ko-KR", "region": "KR", "page": 1}
        # API를 통해 영화 정보 가져오기
        movies_data = get_movies_from_api(api_key, endpoint, params)
        
        # poster_url에 이미지 URL 추가 및 영화 데이터 저장
        for movie_data in movies_data:
            movie_data["poster_url"] = "https://image.tmdb.org/t/p/w500" + movie_data["poster_path"]
            
            Movie.objects.get_or_create(
                api_id=movie_data["id"],
                title=movie_data["title"],
                overview=movie_data["overview"],
                release_date=movie_data["release_date"],
                poster_url=movie_data["poster_url"]
            )

        movies_list.append({"api_name": api_info["name"], "movies": movies_data[:5]})


    # Q 객체를 사용하여 제목에 대한 부분 문자열 검색을 수행
    search_query = request.GET.get('search', '')
    if search_query:
        movies = Movie.objects.filter(Q(title__icontains=search_query))
    else:
        movies = Movie.objects.all()

    context = {'movies_list': movies_list, 'search_query': search_query, 'movies': movies}
    return render(request, 'movies/movie_list.html', context)

def movie_detail(request, movie_id):
    movie = get_object_or_404(Movie, api_id=movie_id)
    context = {'movie': movie}
    return render(request, 'movies/movie_detail.html', context)


    
# def movie_detail(request, movie_id):
#     movie = get_object_or_404(Movie, id=movie_id)

#     if request.method == 'POST':
#         comment_form = CommentForm(request.POST)
#         if comment_form.is_valid():
#             new_comment = comment_form.save(commit=False)
#             new_comment.movie = movie
#             new_comment.save()
#             return redirect('movie_detail', movie_id=movie_id)
#     else:
#         comment_form = CommentForm()

#     return render(request, 'movies/movie_detail.html', {'movie': movie, 'comment_form': comment_form})

class PopularMovieView(TemplateView):
    template_name = 'movies/popular_movie.html'  # 템플릿 파일의 경로
    def get_context_data(self, **kwargs):
        api_key = "a208119c6e1268b59b1ac02b04dd5feb"
        endpoint = "/movie/popular"
        params = {"language": "ko-KR","region": "KR", "page": 1}
        popular_movies  = get_movies_from_api(api_key, endpoint, params)
        # poster_url에 이미지 URL 추가
        for movie_data in popular_movies:
            movie_data["poster_url"] = "https://image.tmdb.org/t/p/w500" + movie_data["poster_path"]

        context = {'popular_movies': popular_movies}
        return context  # 템플릿 파일의 경로


class Now_Playing_MovieView(TemplateView):
    template_name = 'movies/now_playing.html'
    
    def get_context_data(self, **kwargs):
        api_key = "a208119c6e1268b59b1ac02b04dd5feb"
        endpoint = "movie/now_playing"
        params = {"language": "ko-KR","region": "KR", "page": 1}
        now_playing_movies = get_movies_from_api(api_key, endpoint, params)
        # poster_url에 이미지 URL 추가
        for movie_data in now_playing_movies:
            movie_data["poster_url"] = "https://image.tmdb.org/t/p/w500" + movie_data["poster_path"]

        context = {'now_playing_movies': now_playing_movies}
        return context  # 템플릿 파일의 경로
    

class Top_Rated_View(TemplateView):
    template_name = 'movies/Top_Rated_movie.html'  # 템플릿 파일의 경로
    def get_context_data(self, **kwargs):
        api_key = "a208119c6e1268b59b1ac02b04dd5feb"
        endpoint = "/movie/top_rated"
        params = {"language": "ko-KR","region": "KR", "page": 1}
        top_rated_movies  = get_movies_from_api(api_key, endpoint, params)
        # poster_url에 이미지 URL 추가
        for movie_data in top_rated_movies:
            movie_data["poster_url"] = "https://image.tmdb.org/t/p/w500" + movie_data["poster_path"]

        context = {'top_rated_movies': top_rated_movies}
        return context  # 템플릿 파일의 경로
    


class Upcoming_MovieView(TemplateView):
    template_name = 'movies/Upcoming.html'  # 템플릿 파일의 경로
    def get_context_data(self, **kwargs):
        api_key = "a208119c6e1268b59b1ac02b04dd5feb"
        endpoint = "/movie/upcoming"
        params = {"language": "ko-KR", "page": 1}
        upcoming_movies  = get_movies_from_api(api_key, endpoint, params)
        # poster_url에 이미지 URL 추가
        for movie_data in upcoming_movies:
            movie_data["poster_url"] = "https://image.tmdb.org/t/p/w500" + movie_data["poster_path"]

        context = {'upcoming_movies': upcoming_movies}
        return context  # 템플릿 파일의 경로