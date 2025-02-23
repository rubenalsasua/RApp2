from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth import login, authenticate, logout
from RApp2.forms import ProyectoForm, EtiquetaForm, RegistroUsuarioForm
from RApp2.models import Proyecto, Etiqueta
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin


def index(request):
    return render(request, "RApp2/index.html")


class ProyectoListView(LoginRequiredMixin, ListView):
    model = Proyecto
    context_object_name = 'proyectos'
    template_name = 'RApp2/proyectos/proyectos_list.html'

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)


class ProyectoDetailView(LoginRequiredMixin, DetailView):
    model = Proyecto
    context_object_name = 'proyecto'
    template_name = 'RApp2/proyectos/proyecto_detail.html'

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)


class ProyectoCreateView(LoginRequiredMixin, CreateView):
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

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class ProyectoUpdateView(LoginRequiredMixin, UpdateView):
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

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)


class ProyectoDeleteView(LoginRequiredMixin, DeleteView):
    model = Proyecto
    template_name = "RApp2/proyectos/proyecto_confirm_delete.html"
    success_url = reverse_lazy('proyectos-list')

    def get_queryset(self):
        return Proyecto.objects.filter(usuario=self.request.user)


class EtiquetaListView(LoginRequiredMixin, ListView):
    model = Etiqueta
    context_object_name = 'etiquetas'
    template_name = 'RApp2/etiquetas/etiquetas_list.html'

    def get_queryset(self):
        return Etiqueta.objects.filter(usuario=self.request.user)


class EtiquetaDetailView(LoginRequiredMixin, DetailView):
    model = Etiqueta
    context_object_name = 'etiqueta'
    template_name = 'RApp2/etiquetas/etiqueta_detail.html'

    def get_queryset(self):
        return Etiqueta.objects.filter(usuario=self.request.user)


class EtiquetaCreateView(LoginRequiredMixin, CreateView):
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

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        return super().form_valid(form)


class EtiquetaUpdateView(LoginRequiredMixin, UpdateView):
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

    def get_queryset(self):
        return Etiqueta.objects.filter(usuario=self.request.user)


class EtiquetaDeleteView(LoginRequiredMixin, DeleteView):
    model = Etiqueta
    template_name = "RApp2/etiquetas/etiqueta_confirm_delete.html"
    success_url = reverse_lazy('etiquetas-list')

    def get_queryset(self):
        return Etiqueta.objects.filter(usuario=self.request.user)


def registro(request):
    if request.method == "POST":
        form = RegistroUsuarioForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            login(request, user)
            return redirect('index')
    else:
        form = RegistroUsuarioForm()
    return render(request, "RApp2/usuarios/registro.html", {"form": form})


def iniciar_sesion(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, "RApp2/usuarios/login.html", {"form": form})


def cerrar_sesion(request):
    logout(request)
    return redirect('login')
