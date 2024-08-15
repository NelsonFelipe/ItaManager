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
            'location': 'Local',
            'time': 'Horário',
            'city': 'Cidade',
            'seats': 'Vagas Disponíveis'
        }

        widgets = {
            'image': forms.FileInput(),
            'title': forms.TextInput(attrs={'placeholder': 'Digite o título do evento'}),
            'event_type': forms.Select(attrs={'placeholder': 'Selecione o tipo de evento'}),
            'start_date': forms.DateInput(attrs={'placeholder': 'Data de início', 'type': 'date'}),
            'end_date': forms.DateInput(attrs={'placeholder': 'Data de fim', 'type': 'date'}),
            'price': forms.NumberInput(attrs={'placeholder': 'Digite o preço'}),
            'location': forms.TextInput(attrs={'placeholder': 'Digite o local'}),
            'time': forms.TimeInput(attrs={'placeholder': 'Digite o horário', 'type': 'time'}),
            'city': forms.TextInput(attrs={'placeholder': 'Digite a cidade'}),
            'seats': forms.NumberInput(attrs={'placeholder': 'Digite o número de vagas'}),
        }

 