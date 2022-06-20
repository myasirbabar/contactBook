import json
from django.shortcuts import render,redirect

from .models import Contact
from login.models import User
from .forms import Create_Contact

# Create your views here.

def home(request):
    #Validating User
    if "user" not in request.session:
        return redirect("/")

    #GET Logged User
    user = json.loads(request.session["user"])
    
    uname = user["username"]
   
    try:
        querylist = Contact.objects.filter(username = uname)
        
    except Contact.DoesNotExist:
        return render(request,'home.html',{'contacts' : {}})

    return render(request,'home.html',{'contacts' : querylist})


def Add_New_Contact(req):
    #Validating User
    if "user" not in req.session:
        return redirect("/")

    #GET Logged User
    obj = json.loads(req.session["user"])

    user = User.objects.get(username = obj["username"])
    form = Create_Contact(req.POST or None)
    
    if form.is_valid():
        Contact.objects.create(username = user, **form.cleaned_data)
        return redirect('/phonebook')
    
    context = {"form" : form}
    return render(req, 'add_form.html', context)


def delete_contact(req,name):
    #Validating User
    if "user" not in req.session:
        return redirect("/")

    #GET Logged User
    user = json.loads(req.session["user"])
    
    obj = Contact.objects.filter(username = user["username"], contactname = name)
    
    if(len(obj) == 0):
        return redirect('/phonebook')

    obj.delete()

    return redirect('/phonebook')

def update_contact_view(req,name):
    #Validating User
    if "user" not in req.session:
        return redirect("/")

    #GET Logged User
    user = json.loads(req.session["user"])

    obj = Contact.objects.filter(username = user["username"], contactname = name)
    
    if(len(obj) == 0):
        return redirect('/phonebook')

    obj = obj[0]
    form = Create_Contact(req.POST or None, instance=obj)
    
    context = {"form" : form, "obj":obj}
    return render(req, 'update_form.html', context)

def update_contact(req,id):

    if req.method == 'GET':
        return redirect('/phonebook')

    #Validating User
    if "user" not in req.session:
        return redirect("/")

    #GET Logged User
    user = json.loads(req.session["user"])

    obj = Contact.objects.filter(username = user["username"], id = id)
    obj = obj[0]
    
    obj.contactname = req.POST['contactname']
    obj.number = req.POST['number']
    obj.email = req.POST['email']
    obj.address  = req.POST['address']

    obj.save()

    return redirect('/phonebook')
