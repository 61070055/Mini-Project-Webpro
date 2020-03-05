
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth.decorators import login_required, permission_required

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

            next_url = request.POST.get('next_url')
            if next_url:
                return redirect(next_url)
            else:
                return redirect('index')
        else:
            context['username'] = username
            context['password'] = password
            context['error'] = 'Wrong username or password!'

    next_url = request.GET.get('next')
    if next_url:
        context['next_url'] = next_url
    

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
