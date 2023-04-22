from django.urls import path
from capstone_server import views

urlpatterns = [
    path('',views.index),
    path('read/<id>/',views.read)

]
