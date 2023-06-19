from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Note
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
@login_required
def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('display_notes')
        else:
            messages.error(request, 'Invalid username or password.')
    
    return render(request, 'login.html')
def index(request):
    return render(request,'index.html')
def display_notes(request):
    user_notes = Note.objects.filter(user=request.user)
    shared_notes = Note.objects.filter(shared_with=request.user)
    notes = user_notes | shared_notes
    return render(request, 'notes.html', {'notes': notes})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})
