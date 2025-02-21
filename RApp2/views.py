from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from RApp2.forms import ProyectoForm
from RApp2.models import Proyecto


def index(request):
    return render(request, "RApp2/index.html")


class ProyectoListView(ListView):
    model = Proyecto
    context_object_name = 'proyectos'
    template_name = 'RApp2/proyectos/proyectos_list.html'


class ProyectoDetailView(DetailView):
    model = Proyecto
    context_object_name = 'proyecto'
    template_name = 'RApp2/proyectos/proyecto_detail.html'


class ProyectoCreateView(CreateView):
    def get(self, request):
        formulario = ProyectoForm()
        context = {'formulario': formulario}
        return render(request, "RApp2/proyectos/proyecto_create.html", context)

    def post(self, request):
        formulario = ProyectoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("proyectos-list")
        return request, "RApp2/proyectos/proyecto_create.html", {"formulario": formulario}


class ProyectoUpdateView(UpdateView):
    model = Proyecto

    def get(self, request, pk):
        proyecto = Proyecto.objects.get(id=pk)
        formulario = ProyectoForm(instance=proyecto)
        context = {'formulario': formulario, 'proyecto': proyecto}
        return render(request, "RApp2/proyectos/proyecto_update.html", context)

    def post(self, request, pk):
        proyecto = Proyecto.objects.get(id=pk)
        formulario = ProyectoForm(instance=proyecto, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("proyectos-list")
        else:
            formulario = ProyectoForm(instance=proyecto)
        return render(request, "RApp2/proyectos/proyecto_update.html", {"formulario": formulario})


class ProyectoDeleteView(DeleteView):
    model = Proyecto
    success_url = reverse_lazy('proyectos-list')
