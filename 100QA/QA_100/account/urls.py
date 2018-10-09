from django.urls import path
from django.contrib.auth import views as auth_view
from account import views

app_name='account'
urlpatterns = [
    path('signup/', views.signup, name = 'signup'),
    path('logout/', auth_view.LogoutView.as_view(), name='logout'),
    path('login/', auth_view.LoginView.as_view
     (template_name='account/login.html'), name = 'login'),
    path ('profile/<username>', views.save_profile, name = 'profile'),
]
