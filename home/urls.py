from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name='work'),
    path("about", views.about, name='about'),
    path("visuals", views.visuals, name='visuals'),
    path("contact", views.contact, name='contact'),
    path("work", views.work, name='work'),

]