from django.contrib import admin
from .models import Post, Comment # 모델을 임포트합니다.

# 방법1
admin.site.register(Post)  # 모델을 admin 사이트에 등록합니다.


admin.site.register(Comment)  

# 방법2
