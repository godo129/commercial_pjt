from django.shortcuts import (
    render, redirect, reverse
)
from django.contrib import messages
from .forms import (
    CustomUserCreationForm,
    CustomLoginForm,
)
from django.http import JsonResponse
import requests


# 나중에 key는 가릴 것
key = '07fb27a0628c6bde6abb9e4bd5ea463e'

# Create your views here.
def signup(request):
    form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'users/signup.html', context)


def login(request):
    form = CustomLoginForm()
    context = {
        'form': form,
    }
    return render(request, 'users/login.html', context)


def kakao_login(request):
    REST_API_KEY = key
    REDIRECT_URI = 'http://127.0.0.1:8000/users/login/kakao/callback/'
    # GET 형식의 url
    # 카카오 인증 서버가 사용자에게 동의 화면을 출력하여 인가를 위한 사용자 동의를 요청
    # 인가 코드 요청의 응답은 redirect_uri로 HTTP 302 Redirect
    # 보안 위해서는 state, nonce parameter 추가
    url = f"https://kauth.kakao.com/oauth/authorize?client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&response_type=code"
    return redirect(url)
    
    
def kakao_login_callback(request):
    # code --> 인가 코드 받기 요청을 통해 받은 인가 코드
    code = request.GET.get('code')
    REST_API_KEY = key
    REDIRECT_URI = 'http://127.0.0.1:8000/users/login/kakao/callback/'
    token_request = requests.get(
        f"https://kauth.kakao.com/oauth/token?grant_type=authorization_code&client_id={REST_API_KEY}&redirect_uri={REDIRECT_URI}&code={code}"
    )
    token_json = token_request.json()
    error = token_json.get("error", None)

    return render(request, 'users/success.html')


def kakao_logout(request):
    REST_API_KEY = key
    LOGOUT_REDIRECT_URI = "http://127.0.0.1:8000/users/login/"
    url = f"https://kauth.kakao.com/oauth/logout?client_id={REST_API_KEY}&logout_redirect_uri={LOGOUT_REDIRECT_URI}"
    return redirect(url)