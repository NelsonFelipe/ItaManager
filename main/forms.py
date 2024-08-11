from django import forms
from .models import Cultural_Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Cultural_Event
        fields = [
            'image',
            'title',
            'event_type',
            'start_date',
            'end_date',
            'price',
            'is_free',
            'location',
            'time',
            'city',
            'seats'
        ]


        labels = {
            'image': 'Imagem do Evento',
            'title': 'Título',
            'event_type': 'Tipo do Evento',
            'start_date': 'Data de Início',
            'end_date': 'Data de Fim',
            'price': 'Preço',
            'is_free': 'É Gratuito',
            'location': 'Local',
            'time': 'Horário',
            'city': 'Cidade',
            'seats': 'Vagas Disponíveis'
        }

 