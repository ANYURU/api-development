from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Room, Topic
from .forms import RoomForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def loginPage(request):
    """
       1. Get the username and the password from the request. 
       2. Check if the user exists. If the user does not exist inform the user. 
       3. Authenticate the user to verify if their information is correct. 
       4. If the information is correct then redirect the user to the login page. 
    """
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        print('Username:', username, sep=" ")
        print('Password:', password, sep=" ")

        try: 
            user = User.objects.get(username=username)
            if user:
                print("user exists")
        except: 
            messages.error(request, 'User does not exist')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

        else: 
            messages.error(request, 'Wrong Username or password')

    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')

def home(request):
    q = request.GET.get('q') if request.GET.get('q') != None else ''
    rooms = Room.objects.filter(
        Q(topic__name__icontains=q) |
        Q(name__icontains=q) |
        Q(description__icontains=q)
    ) 

    room_count = rooms.count()
    topics = Topic.objects.all()
    context = {'rooms': rooms, 'topics':topics, 'room_count': room_count}
    return render(request, 'base/home.html', context)

def room(request, pk):
    room = Room.objects.get(id=pk)
    context = { 'room': room}
    return render(request, 'base/room.html', context)

# @login_required(login_required='/login')
@login_required(login_url='login')
def create_room(request):
    form = RoomForm()
    if request.method == 'POST':
        print( request.POST)
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def updateRoom(request, pk):
    room = Room.objects.get(id=pk)
    # prefilling form data.  
    form = RoomForm(instance=room)

    if request.user != room.host:
        return HttpResponse("You are not allowed here!!")


    if request.method == 'POST':
        print(request.POST)
        form = RoomForm(request.POST, instance=room)
        if form.is_valid():
            form.save()
            return redirect('home')

    context = {'form': form}
    return render(request, 'base/room_form.html', context)

@login_required(login_url='login')
def deleteRooom(request, pk):
    room = Room.objects.get(id=pk)
    if request.user != room.host:
        return HttpResponse("You are not allowed here!!")

    if request.method == 'POST':
        room.delete()
        return redirect('home')
    return render(request, 'base/delete.html', {'obj': room})