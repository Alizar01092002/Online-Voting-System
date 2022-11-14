from email import message
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def home(request):
    return HttpResponse("This is home page:")

def signin(request):

    if request.method =="POST":
        username= request.POST['username']
        pass1 = request.POST['pass1']

        user=authenticate(username=username,password=pass1)

        if user is not None:
            login(request,user)
            fname=user.first_name
            return render(request,'env.html',{'fname':fname})

        else:
            messages.error(request,'bad credential')
            return redirect('signin')

    return render(request,"signin.html")

def signup(request):

    if request.method == "POST":
        username=request.POST.get('username')
        fname=request.POST['fname']
        lname=request.POST['lname']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if User.objects.filter(username=username):
            messages.error(request,"The username is taken! try another:")
            return redirect('signup')

        myuser= User.objects.create_user(username, email, pass1)
        myuser.first_name= fname
        myuser.last_name= lname

        myuser.save()

        messages.success(request,"You are signup successfully:")
        return redirect("signin")

    return render(request,"signup.html")


def logout(request):
    logout(request)
    messages.success(request,"you are successfully logged out:")
    return render(request,"index.html")

def index(request):
    return render(request,'index.html')

def vote(request):
    # if request.method=="POST":
        
    return render(request,"vote.html")