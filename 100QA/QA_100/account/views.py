from django.shortcuts import render, get_object_or_404
from django.contrib.auth import login as auth_login
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required


from .forms import SignUpForm, UpdateProfileForm, CustomQuestionFormset
from .models import CustomQuestion
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
    current_user = get_object_or_404(User, username=username)
    form = UpdateProfileForm(instance = current_user.profile)
    formset = CustomQuestionFormset(queryset=CustomQuestion.objects.none())
    #could be simply done by user.username, but mehhh
    if (request.user.id == current_user.id):
        if request.method == 'POST':
            form = UpdateProfileForm(request.POST, instance=current_user.profile)
            formset = CustomQuestionFormset(request.POST)
            if form.is_valid() and formset.is_valid:
                profile = form.save()
                for custom in formset:
                    cq = custom.save(commit=False)
                    cq.profile = profile
                    cq.save()

                #TODO: gotta fix this redirection later.
                return HttpResponseRedirect(request.path_info)
        return render(request, 'account/profile.html', {"form": form, "formset": formset})
    #TODO:Maybe if a user try to access someone's profile that has nothing to with that person
    #more than 3 times,delete that account?
    return render(request, 'redirection.html', {'message': "Dont even try!"})

