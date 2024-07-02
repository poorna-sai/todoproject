
from django.contrib import admin
from django.urls import path
# from .views import home , about_me
from .views import *

urlpatterns = [
   path('' ,Register , name="register" ),
   path("about/" , about_me , name="about"),
   path("addtask/" , add_task , name="addtask"),
   path("getdata/" , get_data , name="data"),
   path('edit/<parm>/' , edit_data , name="editdata"),
   path('delete/<p>/' , delete_data , name="deletedata"),
]
