from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.http import HttpResponse
from posts import models

def sign_up_page(request):
    data = {
        'categories': models.Category.objects.all().order_by('id'),
    }
    
    return render(request, 'signup.html', data)


def sign_up(request):
    if request.method == 'POST':
        first_name = request.POST.get('first-name')
        last_name = request.POST.get('last-name')
        email = request.POST.get('email')
        username = request.POST.get('user-name')
        password = request.POST.get('password')
        re_password = request.POST.get('re-password')
        
        if(password != re_password):
            return redirect('/signup?error=not_match')
        
        new_user = User(first_name=first_name, last_name=last_name, email=email, username=username)
        # new_user.first_name = first_name
        # new_user.last_name = last_name
        # new_user.email = email
        # new_user.username = username
        new_user.set_password(password)
        new_user.save()
        
        return redirect('/')

        
    return HttpResponse(request, 'Hello')