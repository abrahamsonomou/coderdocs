from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    list_categories=CourseCategory.objects.all().filter(statut=True)

    context={
        'categories':list_categories,
        }
    return render(request,"main/pages/index.html",context)

# @login_required
def detail_cours(request,pk:int):
    if not request.user.is_authenticated:
        return redirect('login')
    try:
        categorie=CourseCategory.objects.get(pk=pk)
        subcategories=SubCourseCategory.objects.filter(categorie=categorie)
        lecons=Lecon.objects.all()
        context={
            'subcategories':subcategories,
            'lecons':lecons,
            'categorie':categorie,
        }
    except CourseCategory.DoesNotExist:
        raise('This cours doesnot exist')
    return render(request,'cours/pages/cours.html',context)
 
 
def search_cours(request):
    query=request.GET["cours"]
    categories=CourseCategory.objects.filter(title__icontains=query).order_by('-updated')[:5] 
 
    context={
            'categories':categories,
            }
    return render(request,'cours/pages/search_cours.html',context)
 
   
# gestion des erreurs
def handler403(request,exception):
    return render(request,'main/pages/403.html')

def handler404(request, exception):
    return render(request,'main/pages/404.html',status=404)

def handler500(request):
    return render(request,'main/pages/500.html')

def handler503(request,exception):
    return render(request,'main/pages/503.html') 