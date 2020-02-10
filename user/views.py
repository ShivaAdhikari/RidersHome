from django.contrib import auth
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect


# Create your views here.
def show_reg(request):
    if request.method == 'POST':
        fn = request.POST['fn']
        ln = request.POST['ln']
        em = request.POST['em']
        un = request.POST['un']
        pw = request.POST['pw']
        user = User.objects.create_user(first_name=fn, last_name=ln, email=em, username=un, password=pw)
        user.save()
        return HttpResponse('<script>alert("user registered!")</script>')

    return render(request, 'registration.html')


def show_login(request):
    if request.method == 'POST':
        un = request.POST['un']
        pw = request.POST['pw']
        usr = auth.authenticate(username=un, password=pw)
        if usr is not None:
            auth.login(request, usr)
            return redirect('../../')
        else:
            return HttpResponse("wrong id or password")

    return render(request, 'login.html')


def do_logout(request):
    auth.logout(request)
    return redirect('../../')
