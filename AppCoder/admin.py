from django.contrib import admin
from .models import Curso, Entregable, Estudiante, Profesor

class CursoAdmin(admin.ModelAdmin):
    list_display = ["nombre" , "camada"]
    search_fields = ["nombre"]
    

admin.site.register(Curso)
admin.site.register(Entregable)
admin.site.register(Estudiante)
admin.site.register(Profesor)