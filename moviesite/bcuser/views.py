from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Bcuser
from django.contrib.auth.hashers import make_password, check_password
from .forms import LoginForm

# Create your views here.

# 비즈니스 로직


def home(request):
    return render(request, 'home.html')


def logout(request):
    if request.session.get('user'): # 로그인 확인
        del(request.session['user']) # 세션의 생성 여부 확인

    return redirect('/') # 홈으로 들어감

def login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            request.session["user"] = form.user_id
            return redirect("/")
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})
    

# views.py에서는 templates폴더를 참조하고 있으므로
# 요청이 들어왔을 때 Django에 register.html를 참조하는 메소드 구현
def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        # requset로 받을때 넘어오는 값이 없으면 nullpoint error가 발생되므로 None처리
        username=request.POST.get('username', None)
        useremail=request.POST.get('useremail', None)
        password=request.POST.get('password', None)
        re_password=request.POST.get('re-password', None) 

        res_data={}

        if not(username and useremail and password and re_password):
            res_data['error']="모든 값을 입력해야합니다."
        elif password != re_password:
            res_data['error']="비밀번호가 일치하지 않습니다."
        else:
        # 입력받은 값을 변수방에 저장하여(username, password) 데이터베이스에(models) 전달
            bcuser=Bcuser(
                username=username, 
                useremail=useremail, 
                # 평문이 아닌 암호화를 통하여 설정
                password=make_password(password)
            )
            bcuser.save() # 저장

        return render(request, 'register.html', res_data)