from django.urls import path
from contact import views


urlpatterns = [
    path('',views.index,name="index"),
    path('about',views.about,name="about"),
    path("insert", views.insertData, name="insertData"),
]