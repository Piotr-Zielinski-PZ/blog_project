from django.shortcuts import render
# from django.contrib.auth.forms import UserCreationForm
from .forms import FixedUserCreationForm
# from django.contrib.auth.forms import AuthenticationForm
from .forms import FixedAuthenticationForm
from .forms import ChangeUserProfile
from .forms import ChangeUserPassword
from .forms import ProfilePic
# from django.contrib.auth.forms import PasswordChangeForm
# from .forms import FixedPasswordChangeForm
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm

def sign_up(request):
    form = FixedUserCreationForm()
    registered = False
    if request.method == 'POST':
        form = FixedUserCreationForm(data=request.POST)
        if form.is_valid():
            form.save()
            registered = True

    dict = {'form':form, 'registered':registered}
    return render(request, 'Login_API/sign_up.html', context=dict)


def login_page(request):
    form = FixedAuthenticationForm()
    if request.method == 'POST':
        form = FixedAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('index'))
    return render(request, 'Login_API/login.html', context={'form':form})

@login_required
def logout_page(request):
    logout(request)
    return HttpResponseRedirect(reverse('Login_API:login_page'))


@login_required
def profile(request):
    return render(request, 'Login_API/profile.html', context={})

@login_required
def edit_profile(request):
    current_user = request.user
    form = ChangeUserProfile(instance=current_user)
    if request.method == 'POST':
        form = ChangeUserProfile(data=request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = ChangeUserProfile(instance=current_user)
    return render(request, 'Login_API/edit_profile.html', context={'form':form})

@login_required
def edit_password(request):
    current_user = request.user
    changed = False
    form = ChangeUserPassword(current_user)
    if request.method == 'POST':
        form = ChangeUserPassword(current_user, data=request.POST)
        if form.is_valid():
            form.save()
            changed = True
            form = ChangeUserPassword(current_user)
    return render(request, 'Login_API/edit_password.html', context={'form':form, 'changed':changed})

@login_required
def add_profile_pic(request):
    form = ProfilePic()
    if request.method == 'POST':
        form = ProfilePic(request.POST,request.FILES)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('Login_API:profile'))
    return render(request, 'Login_API/add_profile_pic.html', context={'form':form})

@login_required
def edit_profile_pic(request):
    form = ProfilePic(instance=request.user.user_profile)
    if request.method == 'POST':
        form = ProfilePic(request.POST,request.FILES,instance=request.user.user_profile)
        if form.is_valid():
            user_obj = form.save(commit=False)
            user_obj.user = request.user
            user_obj.save()
            return HttpResponseRedirect(reverse('Login_API:profile'))
    return render(request, 'Login_API/add_profile_pic.html', context={'form':form})
