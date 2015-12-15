from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.mail import EmailMessage
from django.contrib import auth
from django.core.context_processors import csrf 

from .forms import RegistrationForm
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()

from django.conf import settings


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        error_msg = 'Invalid login details supplied.'

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('/homepage')
        else:
            print("Invalid login details: {0}, {1}".format(username, password))
            return render(request, 'homepage/index.html', 
                          {'error_msg' : error_msg})
            # return HttpResponse("Invalid login details supplied.")
    elif request.user.is_authenticated():
        if request.user.avatar:
            avatar = settings.MEDIA_URL + str(request.user.avatar)
        else:
            avatar = None

        return render(request, 'homepage/index.html', 
                      {'full_name' : request.user.username, 
                       'avatar' : avatar})
    else:
        return render(request, 'homepage/index.html')


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST, request.FILES)
        
        if form.is_valid():
            user = form.save(commit=False)
            if 'avatar' in request.FILES:
                user.avatar = request.FILES['avatar']
                
            form.save()
            to_email = request.POST.get("email")
            email = EmailMessage(
                'Site registration', 'Registered successfully', to=[to_email])
            email.send()



            return HttpResponseRedirect('/homepage')
            # return render(request, "homepage/index.html")
    else:
        form = RegistrationForm()
 
    return render(request, "homepage/register.html", { "form" : form })


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/homepage')
