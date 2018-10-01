from django.shortcuts import render
from django.contrib.auth import login as auth_login
from django.http import HttpResponse

from .forms import SignUpForm
# Create your views here.

def signup(request):
    form = SignUpForm

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return HttpResponse("HELLO WORLD!")

    return render(request, 'account/signup.html', {"form": form})
