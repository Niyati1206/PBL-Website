from django.urls import path
from . import views

urlpatterns= [
    path('',views.say_hello),
    path('page2.html',views.page2)
]