from django.shortcuts import render
def home(request):
    return render(request,'home.html')

def register(request):
    return render(request,'Registration.html')
def POST(request):
    return render(request,'post.html')
def TRANSPORT(request):
    return render(request,'transport.html')

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["postdata"]
collection = mydb["posts"]
lgn=myclient["LogIn"]
collection1=lgn["login"]

def insert(request):
    name=request.POST.get('name')
    number=request.POST.get('contact')
    sendersaddress=request.POST.get('source')
    senderspostalcode=request.POST.get('senderspostalcode')
    recieversaddress=request.POST.get('dest')
    recieverspostalcode=request.POST.get('recieverspostalcode')
    fees=request.POST.get('fees')
    price=request.POST.get('price')
    data={"name":name,"number":number,"sendersaddress":sendersaddress,"senderspostalcode":senderspostalcode,"recieversaddress":recieversaddress,"recieverspostalcode":recieverspostalcode,"fees":fees,"price":price}
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
    

# Create your views here.
    