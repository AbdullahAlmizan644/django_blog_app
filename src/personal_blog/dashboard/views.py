from django.shortcuts import render,redirect
from blog.models import Category,Post

# Create your views here.
def dashboard(request):
    posts=Post.objects.all()
    return render(request,"dashboard.html",{
        "posts":posts
    })


def login(request):
    return render(request,"login.html")


def password(request):
    return render(request,"password.html")


def add_post(request):
    categories=Category.objects.all()
    
    if request.method=="POST":
        title=request.POST.get("title")
        category=request.POST.get("category")
        description=request.POST.get("description")
        date=request.POST.get("date")

        print(title,description,category,date)
        post=Post(title=title,description=description,date=date)
        category2=Category.objects.get(category_name=category)
        post.category_name=category2
        post.save()
        return redirect("index")

    return render(request,"add_post.html",{
        "categories":categories,
    })


def add_category(request):
    categories=Category.objects.all()
    if request.method=="POST":
        category=request.POST.get("category")
        category=Category(category_name=category)
        category.save()
        return redirect("add_category")

    return render(request,"add_category.html",{
        "categories":categories
    })


