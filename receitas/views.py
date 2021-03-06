from django.shortcuts import get_object_or_404, render
from .models import Receita

# Create your views here.
def index(request):
    receitas = Receita.objects.all()

    dados = {
        'receitas': receitas
    }
    return render(request, 'index.html', dados)

def receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    receita_exibir = {
        'receita_ex': receita
    }
    return render(request, 'receita.html', receita_exibir)    
