from django.urls import path
from . import views

urlpatterns= [
    path('',views.say_hello),
    path('page2.html',views.page2),
    path('register/', views.register_view,name='register'),
    path('login/', views.login_view,name='login'),
    path('logout/', views.logout_view,name='logout')
]