# -*- coding: utf-8 -*-
from django.contrib.auth import authenticate, login 
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from apps.proyecto.forms import MessageForm

def loginUser(request):
    #import pdb;pdb.set_trace();
    # This view is missing all form handling logic for simplicity of the example
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Login correcto
                return  HttpResponseRedirect('/scrum/proy/list/')
                #return render(request, lista)
            else:
                # Usuario desactivado
                return render(request, 'home/identify.html', {'form': MessageForm(),
                                                              'msj':'El usuario esta desactivado'})
        else:
            # Campos de texto vacios
            return render(request, 'home/identify.html', {'form': MessageForm(),
                                                          'msj':'Usuario o contraseña incorrect'})    
    else:
        # No es POST
        return render(request, 'home/identify.html', {'form': MessageForm()})
    
        
def logout(request):
    auth.logout(request)
    return HttpResponseRedirect("/scrum/login/")
