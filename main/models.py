from django.db import models
from django.template.defaultfilters import slugify
import uuid
from django_quill.fields import QuillField
from django.urls import reverse
from app_auth.models import *

# Create your models here.
# la class de base 
class BaseModel(models.Model):
    uid=models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False)
    created=models.DateField(auto_now_add=True,blank=True,null=True,verbose_name='Create date')
    updated=models.DateTimeField(auto_now=True,verbose_name='Update date')
    statut=models.BooleanField(default=False,verbose_name="Statut")

    class Meta:
        abstract=True

# la class BaseCourse
class BaseCourse(BaseModel):
    CHOIX_ICONE=(
        ('fa-tools','fas fa-tools'),
        ('fa-laptop-code','fas fa-laptop-code'),
        ('fa-tablet-alt','fas fa-tablet-alt'),
        ('fa-book-reader','fas fa-book-reader'),
        ('fa-lightbulb','fas fa-lightbulb'),
        ('fa-map-signs','fas fa-map-signs'),
        ('fa-arrow-down','fas fa-arrow-down'),
        ('fa-box fa-fw','fas fa-box fa-fw'),
        ('fa-cogs fa-fw','fas fa-cogs fa-fw'),
    )
    title=models.CharField(max_length=200,verbose_name="Title")
    slug=models.SlugField(max_length=200,verbose_name='Slug',blank=True,null=True)
    icone=models.CharField(max_length=200,choices=CHOIX_ICONE,default='fa-book-reader')
   
    class Meta:
        abstract=True
    
    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        
        super().save(*args,**kwargs) 
    
    def __str__(self) -> str:
        return self.title 

# la class coursecategory    
class CourseCategory(BaseCourse):
    description=models.TextField(blank=True,null=True,verbose_name="Description")

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

# la class subcoursecategory    
class SubCourseCategory(BaseCourse):
    categorie=models.ForeignKey(CourseCategory,
                                on_delete=models.SET_NULL,null=True,
                                blank=True,related_name='fk_categorie_subcategorie')

    class Meta:
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categorys'

# la class Lecon    
class Lecon(BaseModel):
    title=models.CharField(max_length=200,verbose_name="Title")
    slug=models.SlugField(max_length=200,verbose_name='Slug',blank=True,null=True)
    contenu=QuillField(blank=True,null=True)
    categorie=models.ForeignKey(SubCourseCategory,
                                on_delete=models.SET_NULL,null=True,
                                blank=True,related_name='fk_categorie_lecon')

    class Meta:
        verbose_name = 'Lecon'
        verbose_name_plural = 'Lecons'

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        
        super().save(*args,**kwargs) 
    
    def __str__(self) -> str:
        return self.title 

# la class Exercice    
class Exercice(BaseModel):
    title=models.CharField(max_length=200,verbose_name="Title")
    slug=models.SlugField(max_length=200,verbose_name='Slug',blank=True,null=True)
    enonce=QuillField(blank=True,null=True)
    corige=QuillField(blank=True,null=True)
    categorie=models.ForeignKey(SubCourseCategory,
                                on_delete=models.SET_NULL,null=True,
                                blank=True,related_name='fk_categorie_exercice')

    class Meta:
        verbose_name = 'Exercice'
        verbose_name_plural = 'Exercices'

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        
        super().save(*args,**kwargs) 
    
    def __str__(self) -> str:
        return self.title 

# la class Docs    
class Docs(BaseModel):
    title=models.CharField(max_length=200,verbose_name="Title")
    slug=models.SlugField(max_length=200,verbose_name='Slug',blank=True,null=True)
    file = models.FileField(upload_to='media/docs', null=True, blank=True)
    categorie=models.ForeignKey(SubCourseCategory,
                                on_delete=models.SET_NULL,null=True,blank=True,
                                related_name='fk_categorie_docs')

    class Meta:
        verbose_name = 'Doc'
        verbose_name_plural = 'Docs'

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug=slugify(self.title)
        
        super().save(*args,**kwargs) 
    
    def __str__(self) -> str:
        return self.title 
