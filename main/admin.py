from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(CourseCategory)
class CourseCategoryAdmin(admin.ModelAdmin):
    list_display=('title','icone')
    list_filter=('title',)
    prepopulated_fields={'slug':('title',)}

@admin.register(SubCourseCategory)
class SubCourseCategoryAdmin(admin.ModelAdmin):
    list_display=('title','icone')
    list_filter=('title',)
    prepopulated_fields={'slug':('title',)}

@admin.register(Lecon)
class LeconAdmin(admin.ModelAdmin):
    list_display=('title','categorie')
    list_filter=('title',)
    prepopulated_fields={'slug':('title',)}


@admin.register(Exercice)
class ExerciceAdmin(admin.ModelAdmin):
    list_display=('title','categorie')
    list_filter=('title',)
    prepopulated_fields={'slug':('title',)}

