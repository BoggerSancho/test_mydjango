from django.shortcuts import render
from .models import Books, Reader
from django.shortcuts import redirect
from django.views.generic import TemplateView
from django.template.context_processors import csrf
from django.contrib.auth import authenticate, login, logout
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm

def index(request):
    all_book = Books.objects.all()
    return render(request, 'mainApp/myindex.html', all_book)

def register(request):
    ctx = {}
    if request.POST:
        username = request.POST.get('login', '')
        password = request.POST.get('password', '')
        email = request.POST.get('email', '')
        first_name = request.POST.get('first_name', '')
        last_name = request.POST.get('last_name', '')
        # ctx['username'] = username
        # ctx['password'] = password
        # ctx['email'] = email
        # ctx['first_name'] = first_name
        # ctx['last_name'] = last_name
        reader = Reader(username=username, email=email, password=password, first_name=first_name,
                        second_name=last_name)
        try:
            reader.save()
            return redirect('/')
        except:
            ctx['login_error'] = 'error'
            return redirect('/register',request, ctx)

    return render(request, 'mainApp/register.html', ctx)


def get(request):
    all_book = Books.objects.all().order_by("-date")
    # username = request.POST['username']
    # password = request.POST['password']
    # if username == 'bogger':
    #     template_name = 'mainApp/myindex.html'
    # else:
    #     template_name = 'mainApp/register.html'
    template_name = 'mainApp/myindex.html'
    ctx = {
        'all_book': all_book,
    }
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request, user)
                return redirect('/')
            else:
                ctx['login_error'] = "Invalid user"
                return render(request, template_name,  ctx)
        else:
            ctx['login_error'] = "Invalid"
            return render(request, template_name, ctx)
    else:
        return render(request, template_name, ctx)

    return render(request, template_name, ctx)


def login(request):
    template_name = 'mainApp/login.html'
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                auth.login(request,user)
                return redirect('/')
            else:
                args['login_error'] = "Invalid user"
                return render('/',request, template_name, args)
        else:
            args['login_error'] = "Invalid"
            return render('/', request, template_name, args)
    else:
        return render(request, template_name, args)

def logout(request):
    auth.logout(request)
    return redirect('/')

