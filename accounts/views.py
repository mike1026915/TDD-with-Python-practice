import sys
from accounts.models import Token
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.contrib import messages
from django.shortcuts import redirect, render
from django.core.mail import send_mail
from django.http import HttpResponse

def login(request):
    """
    user = authenticate(assertion=request.POST['assertion'])
    if user:
        auth_login(request, user)
    return HttpResponse('OK')
    """
    if request.method == 'GET':
        return render(request, 'login.html')
    if request.method == 'POST':
        email = request.POST.get('email')
        if email:
            token = Token.objects.create(email=email)
            send_mail(
                'Your login code for superlists',
                'Use this code to log in: {uid}\n'.format(uid=token.uid),
                'noreply@superlists',
                [email],
            )
            messages.success(request, 'Email sent to {}'.format(email))
            return redirect('login')

        #user = PasswordlessAuthenticationBackend().authenticate(uid=request.POST.get('uid').strip())
        user = authenticate(uid=request.POST.get('uid').strip())
        if user:
            auth_login(request, user)
            messages.success(request, 'Logged in as {}'.format(user.email))
            return redirect('/')

        messages.error(request, 'Invalid token')
        return redirect('login')    
    

def logout(request):
    auth_logout(request)
    return redirect('/')