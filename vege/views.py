from django.shortcuts import render , redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# from django.contrib import messages
# Create your views here.

@login_required(login_url="/login")
def receipes(request):
    if request.method == "POST":

        data = request.POST
        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
    
        Receipe.objects.create(
            receipe_name=  receipe_name,
            receipe_description= receipe_description,
            receipe_image= receipe_image,
            )
      
      #for return the page
        return redirect("/receipes/")
    
    # recipes call

    queryset = Receipe.objects.all()
# search it will check perticular string ke ander  ye value aati he ki nhi
    if request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))

        # print(request.GET.get('search'))



    context = {'receipes': queryset } #queryset pass

    return render(request , 'receipes.html', context)
# update receipe
@login_required(login_url="/login")
def update_receipe(request,id):
    queryset = Receipe.objects.get(id = id)

    if request.method == "POST":
        data = request.POST

        receipe_image = request.FILES.get("receipe_image")
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image

        queryset.save()   
        return redirect("/receipes/") 

    context = {'receipe': queryset }
    return render(request , 'update_receipes.html' , context)

# new route for delete

@login_required(login_url="/login")
def delete_receipe(request,id):
    queryset = Receipe.objects.get(id = id)
    queryset.delete()   # delete object
    return redirect("/receipes/") # redirect to the page


def login_page(request):  #should be diff name 
    if request.method == "POST":
         username = request.POST.get('username')
         password = request.POST.get('password')

         if not User.objects.filter(username = username).exists():
             messages.info(request, "Invalid Username")
             return redirect('/login/')

         user = authenticate(username=username , password = password)
         
         if user is None:
             messages.info(request, "Invalid Password")
             return redirect('/login/')

         else:
            login(request, user)  # for this stack overflow
            return redirect('/receipes/')  

    return render(request , 'login.html')


def logout_page(request): 
    logout(request)
    return redirect('/login/')





def register(request):
     if request.method == "POST":
         first_name = request.POST.get('first_name')
         last_name = request.POST.get('last_name')
         username = request.POST.get('username')
         password = request.POST.get('password')

         user = User.objects.filter(username=username)

         if user.exists():
              messages.info(request, "Username already exists")
              return redirect('/register/')   #for unique name
         
         user = User.objects.create(
             first_name = first_name,
             last_name = last_name,
             username = username
         )

         user.set_password(password)  # Encrypts the password
         user.save()

         messages.info(request, "Account created Successfully")

         return redirect('/register/')



     return render(request, 'register.html')




