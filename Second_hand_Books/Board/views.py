
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect

from Board.models import Post


# Create your views here.
@csrf_protect
def my_login(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            return redirect('index')
        else:
            context['error'] = 'Wrong username or password!'
    

    return render(request, template_name='login.html', context=context)

@login_required
def my_logout(request):
    logout(request)
    return redirect('index')

def index(request):  
    return render(request, template_name='Board/index.html')

def buy(request):
    search = request.GET.get('search', '')

    post_list = Post.objects.filter(
        pose_status="01", text_book__icontains=search
    )

    context= {
        'search': search,
        'post_list': post_list
    }
    return render(request, template_name='Board/buy_page.html', context=context)

def sell(request):
    search = request.GET.get('search', '')

    post_list = Post.objects.filter(
        pose_status="01", text_book__icontains=search
    )

    context= {
        'search': search,
        'post_list': post_list
    }
    return render(request, template_name='Board/sell_page.html', context=context)


def my_register(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_email = request.POST.get('email')
        user_name_inuse = User.objects.filter(username = username)
        user_email_inuse = User.objects.filter(email = user_email)
        if (user_name_inuse == ""):
            print('yes')
        for i in user_name_inuse:
            print("test1234")
            print(i.username)
            if (i.username != username):
                print("01 username pass")
                print(password1, password2)
                if (password1 == password2):
                    print('02 password pass')
                    user = User.objects.create_user(
                        username = username, 
                        email = user_email, 
                        password = password1, 
                        first_name = first_name, 
                        last_name = last_name)
                    user.save()
                    return redirect('login')
                else:
                    context['error'] = 'password not match!'
            else:
                print("else username")
                context['error'] = 'ชื่อผู้ใช้นี้ได้ถูกใช้งานแล้ว'
    
    return render(request, template_name='register.html', context=context)
