from django.shortcuts import render, redirect

from django.contrib.auth.models import User

from django.contrib import auth

from django.contrib import messages


# Create your views here.


def login(request):

    if request.method == "POST":

        username = request.POST["username"]
        password = request.POST["password"]

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            #sessionid oluşturma
            auth.login(request, user)
            messages.add_message(request, messages.SUCCESS, "Login Successful")
            print("Login Successful")
            return redirect("index")
        else:
            messages.add_message(request, messages.ERROR, "Username or Password is incorrect!")
            print("Username or Password is incorrect!")
            return redirect("login")
        
    else:
        return render(request, "user/login.html")


def register(request):
    if request.method == "POST":

        #print("Registration Information Submitted!")

        #user kayıt, get form values
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if password == repassword:
            #username 
            if User.objects.filter(username = username).exists():
                messages.add_message(request, messages.WARNING, "Username already exists!")
                print("User name already exists!")
                return redirect("register")
            else:
                if User.objects.filter(email = email).exists():
                    messages.add_message(request, messages.WARNING, "User email already exists!")
                    print("User email already exists!")
                    return redirect("register")
                else:
                    #Everything is Okay!
                    user = User.objects.create_user(username=username, password=password, email=email)
                    user.save()
                    messages.add_message(request, messages.SUCCESS, "User has been registered!")
                    print("User has been registered!")
                    return redirect("login")

        else:
            messages.add_message(request, messages.WARNING, "Entered passwords donot matcht!")
            print("Entered passwords do not match!")
            return redirect("register")



        
    else:
        return render(request, "user/register.html")


def logout(request):
    if request.method  == "POST":
        auth.logout(request)  #session id'yi siler
        messages.add_message(request, messages.SUCCESS, "User is logged out!")
        return redirect("index")
    
    
    #return render(request, "user/logout.html")
