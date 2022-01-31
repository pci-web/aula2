from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Tarefa
from .forms import TarefaForm
# Create your views here.

def index_view(request):
    tarefas = Tarefa.objects.all()
    nome = 'Lucio'
    contexto = {'tarefas': tarefas, 'nome': nome}
    return render(request, "tarefas/index.html", contexto)

def form_view(request):
    form = TarefaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('index'))

    contexto = {'form': form}
    return render(request, "tarefas/form.html", contexto)

def apagar_view(request, tarefa_id):
    Tarefa.objects.get(id = tarefa_id).delete()
    return redirect(reverse('index'))