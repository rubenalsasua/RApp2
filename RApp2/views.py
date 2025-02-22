from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from RApp2.forms import ProyectoForm, EtiquetaForm
from RApp2.models import Proyecto, Etiqueta


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
        return render(request, "RApp2/proyectos/proyecto_create.html", {"formulario": formulario})


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
    template_name = "RApp2/proyectos/proyecto_confirm_delete.html"
    success_url = reverse_lazy('proyectos-list')


class EtiquetaListView(ListView):
    model = Etiqueta
    context_object_name = 'etiquetas'
    template_name = 'RApp2/etiquetas/etiquetas_list.html'


class EtiquetaDetailView(DetailView):
    model = Etiqueta
    context_object_name = 'etiqueta'
    template_name = 'RApp2/etiquetas/etiqueta_detail.html'


class EtiquetaCreateView(CreateView):
    def get(self, request):
        formulario = EtiquetaForm()
        context = {'formulario': formulario}
        return render(request, "RApp2/etiquetas/etiqueta_create.html", context)

    def post(self, request):
        formulario = EtiquetaForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("etiquetas-list")
        return render(request, "RApp2/etiquetas/etiqueta_create.html", {"formulario": formulario})


class EtiquetaUpdateView(UpdateView):
    model = Etiqueta

    def get(self, request, pk):
        etiqueta = Etiqueta.objects.get(id=pk)
        formulario = EtiquetaForm(instance=etiqueta)
        context = {'formulario': formulario, 'etiqueta': etiqueta}
        return render(request, "RApp2/etiquetas/etiqueta_update.html", context)

    def post(self, request, pk):
        etiqueta = Etiqueta.objects.get(id=pk)
        formulario = EtiquetaForm(instance=etiqueta, data=request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect("etiquetas-list")
        else:
            formulario = EtiquetaForm(instance=etiqueta)
        return render(request, "RApp2/etiquetas/etiqueta_update.html", {"formulario": formulario})


class EtiquetaDeleteView(DeleteView):
    model = Etiqueta
    template_name = "RApp2/etiquetas/etiqueta_confirm_delete.html"
    success_url = reverse_lazy('etiquetas-list')
