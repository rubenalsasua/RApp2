from django.urls import path
from RApp2 import views

urlpatterns = [
    path('', views.index, name='index'),
    path('proyectos', views.ProyectoListView.as_view(), name='proyectos-list'),
    path('proyectos/<int:pk>', views.ProyectoDetailView.as_view(), name='proyecto-detail'),
    path('proyectos/<int:id>/update', views.ProyectoUpdateView.as_view(), name='proyecto-update'),
    path('proyectos/<int:id>/delete', views.ProyectoDeleteView.as_view(), name='proyecto-delete'),
    path('proyectos/create', views.ProyectoCreateView.as_view(), name='proyecto-create'),
]
