from django.shortcuts import render,redirect,HttpResponse
from .models import Post,LetterEmail
from .models import Category
from django.conf import settings
from django.core.mail import EmailMessage
from random import randint
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

# Create your views here.

def index(request):
    posts=Post.objects.order_by("-date")
    all_posts=Post.objects.all()
    categories=Category.objects.all()
    page=request.GET.get('page', 1)
    paginator=Paginator(all_posts,4)


    try:
        page_paginator=paginator.page(page)
    
    except PageNotAnInteger:
        page_paginator=paginator.page(1)
    
    except EmptyPage:
        page_paginator=paginator.page(paginator.num_pages)

    return render(request,"index.html",{
        "posts":posts,
        "categories":categories,
        "page_paginator":page_paginator,
    })


def about(request):
    return render(request,"about.html")



def contact(request):
    if request.method=="POST":
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")

        send_email = EmailMessage(subject, message, from_email=email,to=['info@aamizan.com'])
        send_email.send()
        return redirect("index")
    return render(request,"contact.html")


def single(request,post_id):
    post=Post.objects.filter(id=post_id).first()
    posts=Post.objects.order_by("-date")
    categories=Category.objects.all()
    return render(request,"single.html",{
        "post":post,
        "posts":posts,
        "categories":categories
    })


def newsletter(request):
    if request.method=="POST":
        global email_news
        email_news=request.POST.get("email")

        all_email=LetterEmail.objects.filter(email=email_news)

        if all_email:
            return HttpResponse("<h1>You already subscribed!</h1>")

        global mail_token
        mail_token=randint(000000,999999)
        send_email = EmailMessage('verify mail', f'http://127.0.0.1:8000/verify/{mail_token}', to=[email_news])
        send_email.send()
        return render(request,"newsletter.html")

def verify(request,token):
    if token==mail_token:
        letter_email=LetterEmail(email=email_news)
        letter_email.save()
        return HttpResponse("Mail Verified!")

    else:
        return HttpResponse("Not matched!")


def search(request):
    if request.method=="POST":
        search=request.POST.get("search")

        result=Post.objects.filter(title__contains=search)
        total=result.count

        return render(request,"search.html",{
            "result":result,
            "search":search,
            "total":total
        })