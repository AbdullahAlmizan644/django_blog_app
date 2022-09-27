from django.urls import path
from . import views


urlpatterns=[
    path("",views.dashboard,name="dashboard"),
    path("login",views.login,name="login"),
    path("password",views.password,name="password"),
    path("add_post",views.add_post,name="add_post"),
    path("add_category",views.add_category,name="add_category"),
]