from django.urls import path,include
from .views import *

urlpatterns = [
    path('',index,name='index'),
    path('cours/(?P<pk>[0-9]+)/$',detail_cours,name='detail_cours'),
    path('cours/recherche',search_cours,name='search_cours'),
]
