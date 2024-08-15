from django.shortcuts import render, get_object_or_404, redirect
from .models import Cultural_Event
from .forms import EventForm

def homepage(request):
    return render(request, 'home.html')

# view da lista dos eventos
def event_list(request):
    events = Cultural_Event.objects.all()
 
    return render(request, 'event_list.html', {'events': events})

# view dos detalhes do evento
def event_detail(request, pk):
    event = get_object_or_404(Cultural_Event, pk=pk)

    
    if request.method == "POST":
        #deleta o evento
        if 'delete' in request.POST:
            event.delete()
            return redirect('lista_eventos')
    
    return render(request, 'event_detail.html', {'event': event})

# View para criar um evento
def event_new(request):
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save()
            return redirect('detalhe_evento', pk=event.pk)
    else:
        form = EventForm()
    return render(request, 'event_edit.html', {'form': form})

# view para editar um evento
def event_edit(request, pk):
    event = get_object_or_404(Cultural_Event, pk=pk)
    if request.method == "POST":
        form = EventForm(request.POST, request.FILES, instance=event)
        if form.is_valid():
            event = form.save()
            return redirect('detalhe_evento', pk=event.pk)
    else:
        form = EventForm(instance=event)
    return render(request, 'event_edit.html', {'form': form})

# view para a pagina de sobre
def about(request):
    return render(request, 'about.html')