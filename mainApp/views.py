from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'mainApp/homePage.html')


def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Если у вас остались вопросы, задавайте их по телефону',
                                                              '123-456-789']})
