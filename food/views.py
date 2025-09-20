from django.shortcuts import render
from .models import *
from django.shortcuts import redirect
from django.shortcuts import render,redirect, get_object_or_404
from django.contrib.auth.models import User
# Create your views here.



def food(request):
    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        recipe.objects.create(
            name = name,
            description = description,
            image = image,
        )

        for food_item in recipe.objects.all():
           print(recipe)  
        return redirect("food")
    return render(request, "food.html",context={"recipe":recipe.objects.all()})



def delete_recipe(request, pk):
    queryset = get_object_or_404(recipe,pk = pk)
    queryset.delete()
    return redirect('food')


def update_recipe(request, pk):
    recipe_instance = get_object_or_404(recipe, pk=pk)

    if request.method == "POST":
        name = request.POST.get("name")
        description = request.POST.get("description")
        image = request.FILES.get("image")

        recipe_instance.name = name
        recipe_instance.description = description
        if image :
            recipe_instance.image = image
        recipe_instance.save()
        return redirect("/food/")

    return render(request,"update.html",{"recipe":recipe_instance})
 

   
   


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        message = request.POST.get("message")
        is_check = request.POST.get("is_check") == "on"

        student.objects.create(
            name = name,
            email = email,
            contact = contact,
            message = message,
            is_check = is_check,
        )
        for contact_info in student.objects.all():
            print(student)
        return redirect("contact")
    return render(request,"contact.html",context={"student":student.objects.all()})
        
def register(request):
    if request.method == "POST":
        first_name = request.POST.get("first_name")
        last_name = request.POST.get("last_name")
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")

        if first_name and last_name and username and password:
            user = User.objects.create(
                first_name = first_name,
                last_name = last_name,
                username = username,
                password = password,
                email = email,
        )
            user.set_password(password)
            user.save()
        else:
            context = {'error: all fields are required!'}
            return render(request,"register.html", context)

        
    return render(request,"register.html")

def login(request):
    return render(request,"login.html")