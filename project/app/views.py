from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.http import HttpResponse
def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'Registration.html')
def POST(request):
    return render(request,'post.html')
def TRANSPORT(request):
    return render(request,'transport.html')
def logn(request):
    return render(request,'login.html')

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["postdata"]
collection = mydb["posts"]


def insert(request):
    name=request.user.id
    title=request.POST.get('title')
    number=request.POST.get('contact')
    sendersaddress=request.POST.get('source')
    senderspostalcode=request.POST.get('senderspostalcode')
    recieversaddress=request.POST.get('dest')
    recieverspostalcode=request.POST.get('recieverspostalcode')
    fees=request.POST.get('fees')
    price=request.POST.get('price')
    desc=request.POST.get('desc')
    data={"title":title,"name":name,"number":number,"sendersaddress":sendersaddress,
    "senderspostalcode":senderspostalcode,"recieversaddress":recieversaddress,
    "recieverspostalcode":recieverspostalcode,"fees":fees,"price":price,"desc":desc}
    collection.insert_one(data)
    print(data)
    return render(request,"homepage.html")


def signup(request):
    email=request.POST.get('email')
    passw=request.POST.get('pass')
    data={"email":email,"passw":passw}
    print(data)
    collection.insert_one(data)
    return render(request,'Registration.html')

def signupage(request):
    return render(request,'Registration.html')
    

def handlesignup(request):
    if request.method=='POST':
        
        name=request.POST.get('name')
        email=request.POST.get('email')
        number=request.POST.get('number')
        password=request.POST.get('Password')
        #creating user
        myuser=User.objects.create_user(email,password)
        myuser.number=number
        myuser.name=name
        myuser.save()
        print("User sreated")
        messages.success(request,"Sucessfully signed up")
        return redirect('/')
    else:
        return HttpResponse('404 Not found')

def handlelogin(request):
    if request.method=='POST':
        email=request.POST['loginemail']
        password=request.POST['loginpass']
        user=authenticate(username=email,password=password)
        print(user)
        if user is not None:
            login(request,user)
            print("logged in")
            return redirect('home')
        else:
            messages.success(request,"Invalid")
            return redirect('home')
    else:
        return redirect('home')


def handlelogout(request):
    print("hi")
    if request.method=='GET':
        logout(request)
        print("Logged out")
    return redirect("home")
def display(request):
    if request.method=='POST':
        srcpin=request.POST['srcpin']
        destpin=request.POST['destpin']
        print(srcpin,destpin)
        x = collection.find(
            {
    "recieverspostalcode" : { "$eq" : srcpin},
    "senderspostalcode" : { "$eq" : destpin}
            }
         )
        ls=[]
        for data in x:
            ls.append(data)
        
        ctx = {
        'data': ls
        }
        print(ctx)
    return render(request,'display.html',ctx)


def MyPost(request):
    print(request.user.id)
    print("hi")
    x = collection.find({
    "name" : { "$eq" : request.user.id},
            }
         )
    ls=[]
    for data in x:
        ls.append(data)
        
    ctx = {
    'data': ls
    }
    print(ctx)
    return render(request,'userdisp.html',ctx)


def delt(request):
    return redirect('MyPost')
# Create your views here.
    