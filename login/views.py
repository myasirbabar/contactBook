import json
from django.shortcuts import render,redirect
from .models import User
from django.contrib import messages

#Error
def error(request):
    return render(request,"error.html", {})

#login-View
def index_view(request):
    return render(request,"index.html", {})

#Logout
def logout(request):
    if "user" not in request.session:
        return redirect("/error")
    
    request.session.flush()
    messages.success(request,"Logged Out Successfully")
    return redirect("/")


def login_user(request):
    if request.method == "GET":
        return redirect("/error")

    username = request.POST["username"]
    password = request.POST["password"]

    try:
        user = User.objects.get(username = username)
        if user.password != password:
            messages.error(request, "Wrong Password")
            return redirect("/")

        uList = json.dumps(user, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

        request.session["user"] = uList
        return redirect("/phonebook")
    except User.DoesNotExist:
        messages.error(request, "No User Found")
        return redirect("/")


