from django.urls import path 
from . import views 


urlpatterns=[
    path("",views.index,name="index"),
    path("about",views.about,name="about"),
    path("contact",views.contact,name="contact"),
    path("single/<int:post_id>",views.single,name="single"),
    path("newsletter/",views.newsletter,name="newsletter"),
    path("verify/<int:token>",views.verify,name="verify"),
    path("search",views.search,name="search"),
]

