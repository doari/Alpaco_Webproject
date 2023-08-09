# movies/utils.py

import requests

def get_movies_from_api(api_key):
    base_url = "https://api.themoviedb.org/3/movie/popular"
    params = {"api_key": api_key}  # 한국어 언어 코드: ko-KR
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        return response.json().get("results", [])
    else:
        return []
    
def get_movies_from_api(api_key, endpoint, params=None):
    base_url = f"https://api.themoviedb.org/3/{endpoint}"
    default_params = {"api_key": api_key}

    if params:
        default_params.update(params)

    response = requests.get(base_url, params=default_params)

    if response.status_code == 200:
        data = response.json()
        return data.get("results", [])
    else:
        return []
