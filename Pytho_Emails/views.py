from django.shortcuts import render,redirect
from .forms import myUserForm
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect


# Create your views here.
def index (request):
       return render(request,'myApp/index.html')

def thanks (request):
       return render(request,'myApp/thanks.html')       




def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('thanks')
    else:
        form = UserCreationForm()
    return render(request, 'myApp/index.html', {'form': form})    