from django.contrib import admin
from django.urls import path
from food import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("food/",views.food,name="food"),
    path('food/delete_recipe/<int:pk>/', views.delete_recipe, name='delete_recipe'),
    path('food/update_recipe/<int:pk>/', views.update_recipe, name='update_recipe'),
    path('contact/',views.contact,name="contact"),
    path('login/',views.login,name="login"),
    path("register/",views.register,name="register"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
