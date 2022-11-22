from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from .forms import *
from django.contrib import messages
from .models import CustomUser
from django.contrib.auth.hashers import check_password

# Create your views here.
def register_user(request):
    if request.method== "POST":
        form=RegisterForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            email=form.cleaned_data['email']
            password_confirm=form.cleaned_data['password_confirm']
            
            userEmail=CustomUser.objects.filter(email=email).first()
            if userEmail is not None:
                messages.error(request,'Cet email existe dejà')
                return render(request,'auth/register.html',{'form':form})
            else:
                if password != password_confirm:
                    messages.error(request,'Mot de passe non identique')
                    return render(request,'auth/register.html',{'form':form})
                else:
                    user=CustomUser.objects.filter(username=username).first()
                    if user is not None:
                        messages.error(request,'Ce nom d''utilisateur existe')
                        return render(request,'auth/register.html',{'form':form})
                    else:
                        user=CustomUser.objects.create_user(email=email,username=username,password=password)
                        if user is not None:
                            login(request,user)
                            return redirect('login')
                        else:
                            messages.error(request,'Creation de compte echouee')
                            return render(request,'auth/register.html',{'form':form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class']+= ' is-invalid'
            return render(request,"auth/register.html",{"form":form})
    else:
        form=RegisterForm(request.POST)
    return render(request,"auth/register.html",{"form":form})

def login_user(request):
    if request.method== "POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            
            #user=authenticate(username=username,password=password)
            user=CustomUser.objects.filter(username=username).first()
            if user and check_password(password, user.password):
                # print(user)
                if user is not None:
                    #users=CustomUser.objects.filter(username=username).first()
                    if not user.is_active:
                        messages.error(request,"Votre compte n'est pas activé, veuillez contacter l'administrateur")
                        return render(request,"auth/login.html",{"form":form})
                    
                    login(request,user)
                    return redirect('index')
            else:
                messages.error(request,"Autehtification echouee. Vos informations sont incorrectes")
                return render(request,"auth/login.html",{"form":form})
        else:
            for field in form.errors:
                form[field].field.widget.attrs['class']+= ' is-invalid'
            return render(request,"auth/login.html",{"form":form})
    else:
        form=LoginForm()
    return render(request,"auth/login.html",{"form":form})
    

def logout_user(request):
    logout(request)
    return redirect('index')


def forgot_password(request):
    return render(request,'auth/forgot_password.html')