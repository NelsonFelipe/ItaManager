from django.urls import path
from . import views

urlpatterns = [
    path('', views.event_list, name='lista_eventos'),
    path('event/<int:pk>/', views.event_detail, name='detalhe_evento'),
    path('event/new/', views.event_new, name='criar_evento'),
    path('event/<int:pk>/edit/', views.event_edit, name='editar_evento'),
    path('about/', views.about, name='sobre'),
]   