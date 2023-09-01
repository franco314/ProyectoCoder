from django.http import HttpResponse , HttpRequest
from django.shortcuts import render
from .models import Estudiante, Entregable, Curso
from .forms import CursoFormulario

# Create your views here.
def curso (req, nombre, camada):
    curso = Curso(nombre=nombre, camada=camada)
    curso.save()

    return HttpResponse(f"""
                        <p>Curso: {curso.nombre} - Camada: {curso.camada} agregado!<p>
                      """  )


def lista_cursos (request):
    
    lista = Curso.objects.all()

    return render(request, "lista_cursos.html", {"lista_cursos": lista})


def incio(request):

   return render(request, "inicio.html")
   

def cursos(request):
   return render(request, "cursos.html")

def profesores(request):
   return render(request, "profesores.html")

def estudiantes(request):
   return render(request, "estudiantes.html")

def entregables(request):

   estudiante_id = 1
   estudiante = Estudiante.objects.get(id=estudiante_id)
   entregables = Entregable.objects.filter(estudiante=estudiante)

   return render(request, "entregables.html" , {"entregables" : entregables})

def curso_formulario (request:HttpRequest):
  print('method' , request.method)
  print('post' , request.POST)

  if request.method =='POST':
     
     miFormulario = CursoFormulario(request.POST)

     if miFormulario.is_valid():
        
        print(miFormulario.cleaned_data)
        data = miFormulario.cleaned_data

        curso = Curso(nombre=data["curso"], camada=data["camada"])
        curso.save()
        return render(request, "inicio.html", {"mensaje": "Curso creado con exito"})
     else: 
        return render(request, "inicio.html", {"mensaje": "Formulario invalido"})
     
  else:
      miFormulario = CursoFormulario()
      return render(request, "curso_formulario.html" , {"miFormulario": miFormulario})
  

def busqueda_camada (req):
   return render(req, "busquedaCamada.html") 

def buscar (req):
   
     if req.GET["camada"]:
        camada = req.GET["camada"]
        cursos = Curso.objects.filter(camada__icontains=camada)
        if cursos:
            return render(req, "resultadoBusqueda.html" , {"cursos": cursos})
     else:
         return HttpResponse("No escribiste ninguna camada")
















