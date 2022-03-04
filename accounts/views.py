from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.views import View
from django.contrib.auth.models import User


@login_required(login_url='/login')
def index(request):  # 首頁
    return render(request, 'accounts/index.html')


def sign_in(request):  # 登入頁

    if request.user.is_authenticated:
        return redirect('/')

    form = LoginForm()

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')

    context = {
        'form': form
    }
    return render(request, 'accounts/login.html', context)


def sign_out(request):
    logout(request)
    return redirect('/login')


class LoginView(View):
    form_class = LoginForm
    template_name = 'accounts/login.html'

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('/')

        form = self.form_class()
        return render(request, self.template_name, {'form': form, 'error_text': ''})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        username = form.data['username']
        password = form.data['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/')
        else:
            return render(request, self.template_name, {'form': form, 'error_text': '帳號或密碼錯誤'})


def punch(request, clock_type):  # 打卡
    user = User.objects.get(username=request.user)
    clock = user.clock_set.create(clock_type=clock_type)
    clock.save()

    return redirect('/')
