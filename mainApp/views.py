from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def home_view(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request,
                  'mainApp/basic.html',
                  {'values': ['Если у вас остались вопросы, задавайте их по телефону', '8-909-163-23-33']})


def signup_view(request):
    form = UserCreationForm(request.POST)
    if form.is_valid():
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(request, user)
        return redirect('homepage')
    return render(request, 'mainApp/signup.html', {'form': form})
