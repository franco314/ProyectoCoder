from django.urls import path
from AppCoder.views import *

urlpatterns = [
    path('agrega-curso/<nombre>/<camada>', curso),
    path('lista-cursos/', lista_cursos , name="Lista-cursos"),
    path('', incio , name="Inicio"),
    path('cursos/', cursos , name="Cursos"),
    path('estudiantes/', estudiantes , name="Estudiantes"),
    path('profesores/', profesores , name="Profesores"),
    path('entregables/', entregables , name="Entregables"),
    path('curso-formulario/', curso_formulario , name="CursoFormulario"),
    path('busqueda-camada/', busqueda_camada , name="busquedaCamada"),
    path('buscar/', buscar , name="Buscar"),


    
]