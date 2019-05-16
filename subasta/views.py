from django.shortcuts import render

# Create your views here.
def ListarSubasta(request):
    return render(request, 'subasta/subasta_Listar.html')