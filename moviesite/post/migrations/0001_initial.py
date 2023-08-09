from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='제목')),
                ('text', models.TextField(verbose_name='본문')),
                ('image', models.ImageField(upload_to='images/', verbose_name='이미지')),
                ('created_date', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('publiShed_date', models.DateTimeField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80, verbose_name='이름')),
                ('body', models.TextField(verbose_name='본문')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='작성일')),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='post.Post', verbose_name='포스트')),
            ],
            options={
                'verbose_name': '댓글',
                'verbose_name_plural': '댓글들',
            },
        ),
    ]
