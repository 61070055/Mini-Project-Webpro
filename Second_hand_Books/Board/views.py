
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.csrf import csrf_protect
from django.conf import settings
from django.core.files.storage import FileSystemStorage

from Board.models import Post, Message


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
        pose_status="1", text_book__icontains=search
    )

    context= {
        'search': search,
        'post_list': post_list
    }
    return render(request, template_name='Board/buy_page.html', context=context)

def sell(request):
    search = request.GET.get('search', '')

    post_list = Post.objects.filter(
        pose_status="1", text_book__icontains=search
    )

    context= {
        'search': search,
        'post_list': post_list
    }
    return render(request, template_name='Board/sell_page.html', context=context)

@csrf_protect
def my_register(request):
    context = {}
    if request.method == 'POST':
        username = request.POST.get('username')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        user_email = request.POST.get('email')
        # user_name_inuse = User.objects.filter(username = username)
        # user_email_inuse = User.objects.filter(email = user_email)
        # print(user_name_inuse != True)
        # for i in user_name_inuse:
            # print("test1234")
            # print(i.username)
            # if (i.username != username):
                # print("01 username pass")
                # print(password1, password2)
        try:
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
        except:
            context['error'] = 'ชื่อผู้ใช้ได้ถูกใช้งานไปแล้ว' 
            # else:
            #     print("else username")
            #     context['error'] = 'ชื่อผู้ใช้นี้ได้ถูกใช้งานแล้ว'
    
    return render(request, template_name='register.html', context=context)

@login_required
def create_post(request):
    context = {}
    if request.method == 'POST':
        text_book = request.POST.get('text_book')
        type_s_b = request.POST.get('type_s_b')
        price = request.POST.get('price')

        uploaded_picture = request.FILES['picture']
        fs = FileSystemStorage()
        name = fs.save(uploaded_picture.name, uploaded_picture)
        url = fs.url(name)
        print(url)
        user = request.user


        P = Post(
            create_by = user,
            text_book = text_book,
            post_type = type_s_b,
            price = price,
            picture = url
        )

        P.save()
        if (type_s_b == '1'):
            print('buy')
            return redirect('buy')
        else:
            print('sell')
            return redirect('sell')

    return render(request, template_name='Board/create.html', context=context)

def detail(request, post_id):
    post = Post.objects.get(pk=post_id)

    if request.method == 'POST':
        message = request.POST.get('message')
        user = request.user

        M = Message(
            message = message,
            create_by = user,
            post_id = post
            )
        M.save()

    
    message_list = Message.objects.filter(
        post_id = post_id
    )

    context= {
        'post': post,
        'message_list': message_list
    }
    return render(request, template_name='Board/detail.html', context=context)