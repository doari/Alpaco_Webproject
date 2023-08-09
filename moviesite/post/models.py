from django.conf import settings
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from bcuser.models import Bcuser

class Post(models.Model):
        #User 참조되는 foreigkey로 user가 탈퇴하면 게시물이

    title = models.CharField(max_length=200, verbose_name="제목")
    text = models.TextField(null=True, verbose_name="본문")
    image = models.ImageField(upload_to="", verbose_name="이미지", blank=True, null=True)
    created_date = models.DateTimeField(auto_now_add=True, verbose_name="작성일")
    publiShed_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        Bcuser,
        on_delete=models.CASCADE,
        verbose_name="작성자"
            )
        # null=True : null값 허용
        # blank=True : null값이여도 forms.py 에서 검증하라는 뜻

        # 게시글의 날짜와 시간을 설정하고, 그 정보를 데이터베이스에 반영
    def publiShed(self):
        self.publiShed_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'Post_table'
        verbose_name='포스트'
        verbose_name_plural='포스트들'


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE, verbose_name='포스트')
    name = models.CharField(max_length=80, verbose_name="이름")
    body = models.TextField(verbose_name="본문")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='작성일')

    def __str__(self):
        return f'{self.name} - {self.post.title}'

    class Meta:
        db_table = 'Comment_table'
        verbose_name = '댓글'
        verbose_name_plural = '댓글들'
