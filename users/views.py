from django.shortcuts import render, redirect
from .models import Persona 
from .form import PersonaForms

#create your views here.

def registerUser(request):
    if request.method == 'POST':
        form = PersonaForms(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listarUsuarios')
    else:
        form = PersonaForms()
        
    return render(request,
                  template_name= 'registroUsuario.html', context={'form': form}) 
    
    

