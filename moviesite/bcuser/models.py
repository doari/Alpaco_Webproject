from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Bcuser(models.Model):
    # verbose_name : 한글 이름
    username=models.CharField(max_length=32, verbose_name='사용자명')
    useremail = models.EmailField(max_length=128, verbose_name='사용자이메일')
    password=models.CharField(max_length=64, verbose_name='비밀번호')
    # auto_now_add : 현재시간 적용
    registered_dttm=models.DateTimeField(auto_now_add=True, verbose_name='등록시간')
    
    # username 생성시 문자열 함수를 이용하여 객체 username으로 반환
    def __str__(self):
        return self.username

    class Meta:
        db_table='blog_bcuser'
        verbose_name='블로그 사용자'
        # 파이썬에서는 테이블명 복수로 표현
        verbose_name_plural='블로그 사용자'