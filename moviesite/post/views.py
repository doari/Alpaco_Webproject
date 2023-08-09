from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment,timezone
from .forms import PostForm, CommentForm
from django.contrib.auth.decorators import login_required
from bcuser.models import Bcuser

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk) # 만약 해당 객체를 찾지 못하면, 서버는 404 에러를 반환
    # post=post는 post 필드에 연결된 모든 Comment 객체를 데이터베이스에서 찾는 역할
    # 즉 post하나에 연결됨 모든 댓글들 Comment 객체를 comments라는 변수에 할당
    comments = Comment.objects.filter(post=post)
    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            # commit=False 인수는 객체를 데이터베이스에 즉시 저장하지 않고 
            # 객체를 반환하여 추가적인 수정을 허용합니다.
            comment.post = post
            # 코멘트 객체의 post 속성(즉, 코멘트가 연결되는 포스트)을 현재 포스트로 설정
            comment.save() #변경된 코멘트 객체를 데이터베이스에 저장
            return redirect('post_list')
    else:
        comment_form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'comments': comments, 'comment_form': comment_form})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            user_id = request.session.get('user')
            bloguser = Bcuser.objects.get(pk=user_id)
            post.author = bloguser
            post.publiShed_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'post_new.html', {'form': form})

def post_list(request):
    # Post데이터 베이스의 모든 데이터 가져오기(published_date가 현재시간기준 이전시간꺼 모두 가져오기)
# publiShed_date__lte: 여기서 lte는 "less than or equal to"의 약자로,
# 이는 publiShed_date 필드 값이 지정된 값보다 작거나 같은 객체를 필터링하겠다는 의미.
    posts=Post.objects.filter(publiShed_date__lte=timezone.now()).order_by('-publiShed_date')
    return render(request, 'post/post_list.html', {'posts': posts})

def post_edit(request ,pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST,request.FILES,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            user_id = request.session.get('user')
            bloguser = Bcuser.objects.get(pk=user_id)
            post.author = bloguser
            post.publiShed_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'post_edit.html', {'form': form})

def profile(request):
    return render(request, 'profile.html')