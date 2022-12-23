
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home),
    path('registrarCriterio/',views.registrarCriterio),
    path('eliminarCriterio/<codigo>', views.eliminarCriterio),
     path('editarCriterio/<codigo>', views.editarCriterio),
     path('editarCriterio2/', views.editarCriterio2)
]   