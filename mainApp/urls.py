from django.urls import path, include
from django.conf.urls import url
from .views import home_view, contact, signup_view
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('', home_view, name='homepage'),
    path('contact/', contact, name='contact'),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('signup/', signup_view, name="signup")
]
