from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

from . import UiForms
from .UiForms import profile


def index(request):
    return render(request, "Ui/home.html")


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def signup(request):
    count = User.objects.count()
    print(count)
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        profile_form = UiForms.profile(request.POST)

        if form.is_valid() and profile_form.is_valid():
            user = form.save()
            profileu = profile_form.save(commit=False)
            profileu.user = user
            profileu.save()
            return redirect('index')

    else:
        form = UserCreationForm()
    profile_form = profile()
    context = {
        "Myregistration": form,
        "ProfileForm": profile_form
    }
    return render(request, 'registration/Register.html', context)


def ind(request):
    return render(request, 'index')

# def login1(request):
#     if request.method == 'POST':
#         user_name = request.POST.get('username')
#         passwordd = request.POST.get('password')
#         user = authenticate(request, username=user_name, password=passwordd)
#         login(request, user)
#         return redirect('index')
#     else:
#         return render(request, 'login.html')


# form2 = Registration(request.POST or None)
# if form2.is_valid():
#     form2.save()
# context = {
#     'MyRegistration': form2
# }

# def user(request):
#     if request.method == 'POST':
#         form = Registration(request.POST)
#         if form.is_valid():
#             pass  # does nothing, just trigger the validation
#     else:
#         form = Registration()
#     return render(request, 'applicatio.html', {'form': form})
# user_name = form.cleaned_data.get('username')
# raw_password = form.cleaned_data.get('password1')
# user = authenticate(username=user_name, password=raw_password)
# login(request, user)
