"""
URL configuration for myblog project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from post import views

urlpatterns = [
     path('admin/', admin.site.urls),
     path('post/', include('post.urls')),
     path('bcuser/', include('bcuser.urls')),
     path('post/new/', views.post_new, name='post_new'),
     path('profile', views.profile, name='profile'),
     path('movies/', include('movies.urls')),
     path('detail/edit/<int:pk>/', views.post_edit, name='post_edit'),
     path('', include('post.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# static() : DEBUG= True 일때 settings.MEDIA_URL에 정의된 패턴과 일치하는 URL을
# settings.MEDIA_ROOT에서 정의해준 위치에서 제공하도록 라우팅한다는 뜻