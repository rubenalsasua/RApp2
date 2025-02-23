from django.urls import path
from RApp2 import views

urlpatterns = [
    path('', views.index, name='index'),
    path("registro/", views.registro, name="registro"),
    path("login/", views.iniciar_sesion, name="login"),
    path("logout/", views.cerrar_sesion, name="logout"),
    path('proyectos', views.ProyectoListView.as_view(), name='proyectos-list'),
    path('proyectos/<int:pk>', views.ProyectoDetailView.as_view(), name='proyecto-detail'),
    path('proyectos/<int:pk>/update', views.ProyectoUpdateView.as_view(), name='proyecto-update'),
    path('proyectos/<int:pk>/delete', views.ProyectoDeleteView.as_view(), name='proyecto-delete'),
    path('proyectos/create', views.ProyectoCreateView.as_view(), name='proyecto-create'),
    path('etiquetas', views.EtiquetaListView.as_view(), name='etiquetas-list'),
    path('etiquetas/<int:pk>', views.EtiquetaDetailView.as_view(), name='etiqueta-detail'),
    path('etiquetas/create', views.EtiquetaCreateView.as_view(), name='etiqueta-create'),
    path('etiquetas/<int:pk>/update', views.EtiquetaUpdateView.as_view(), name='etiqueta-update'),
    path('etiquetas/<int:pk>/delete', views.EtiquetaDeleteView.as_view(), name='etiqueta-delete'),
]
