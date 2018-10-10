from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login as auth_login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from .forms import SignUpForm, UpdateProfileForm
# Create your views here.

def signup(request):
    form = SignUpForm

    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return render(request, 'QA/home.html')

    return render(request, 'account/signup.html', {"form": form})

@login_required(login_url='/account/login/')
def save_profile(request, username):
    form = UpdateProfileForm
    #could be simply done by user.username, but mehhh
    current_user = get_object_or_404(User,username=username)
    if (request.user.id == current_user.id):
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST, instance=current_user.profile)
            if form.is_valid():
                print (form.changed_data)
                form.save()

                #TODO: gotta fix this redirection later.
                return HttpResponseRedirect(request.path_info)
        return render(request, 'account/profile.html', {"form": form})
    #TODO:Maybe if a user try to access someone's profile that has nothing to with that person
    #more than 3 times,delete that account?
    return render(request, 'redirection.html', {'message': "Dont even try!"})
