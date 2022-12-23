
from django.urls import path 
from . import views
urlpatterns = [
    path('',views.home),
    path('registrarCriterio/',views.registrarCriterio),
    path('eliminarCriterio/<codigo>', views.eliminarCriterio),
    path('editarCriterio/<codigo>', views.editarCriterio),
    path('editarCriterio2/', views.editarCriterio2),
     
    path('gestionIndicador/', views.gestionIndicador),
    path('registrarIndicador/',views.registrarIndicador),
    path('eliminarIndicador/<codigo>', views.eliminarIndicador),
    path('editarIndicador/<codigo>', views.editarIndicador),
    path('editarIndicador2/', views.editarIndicador2),
    
    path('gestionDimension/', views.gestionDimension),
    path('registrarDimension/',views.registrarDimension),
    path('eliminarDimension/<codigo>', views.eliminarDimension),
    path('editarDimension/<codigo>', views.editarDimension),
    path('editarDimension2/', views.editarDimension2),
]   