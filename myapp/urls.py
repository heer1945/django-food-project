from django.contrib import admin
from django.urls import path
from myapp import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('demo/',views.demo,name="demo.html"),
    path('home/',views.home,name="home.html"),
    path('about/',views.about,name="about.html"),
    path('contact/',views.contact,name="contact.html"),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
