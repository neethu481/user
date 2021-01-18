from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


def home(request):
    return render(request, 'home.html')


# User Register
def register(request):
    form = UserCreationForm
    if request.method == 'POST':
        regForm = UserCreationForm(request.POST)
        if regForm.is_valid():
            regForm.save()
            messages.success(request, 'User has been registered.')
    return render(request, 'main/register.html', {'form': form})



def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            # return render(request, 'authen/dashboard.html',{})
            return get_users_view(request)
    else:
        form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})

