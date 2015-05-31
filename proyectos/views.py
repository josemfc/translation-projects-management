# coding=utf-8

from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, Permission
from django.contrib.auth.decorators import login_required, permission_required, user_passes_test
from django.forms.formsets import formset_factory
from django.core.mail import send_mail
from django.conf import settings

import string
import datetime
from random import choice

from proyectos.forms import *


# Página de inicio. Se muestran tareas y proyectos pendientes
def index(request):
	proyectos_pendientes = None
	tareas_pendientes = Tarea.objects.filter(
							asignada_a = request.user.id
							).filter(
							terminada = False
							)
							
	if request.user.groups.filter(name='Project Managers').exists():
		proyectos_pendientes = Proyecto.objects.filter(
							creador = request.user.id
							).filter(
							terminado = False
							)

	context = {
			'tareas_pendientes': tareas_pendientes,
			'proyectos_pendientes': proyectos_pendientes
	}

	return render(request, 'proyectos/index.html', context)


# Información de un proyecto
@login_required
def proyecto(request, id_proyecto):
	proyecto = get_object_or_404(Proyecto, pk=id_proyecto)
	context = {
		'proyecto': proyecto,
    }

	return render(request, 'proyectos/proyecto.html', context)


# Página con formulario para crear nuevo proyecto
@login_required
@permission_required('auth.es_project_manager', login_url="proyectos:index")
def nuevo_proyecto(request):
	TareaFormSet = formset_factory(TareaForm)	# Set de formularios para un número indefinido de tareas
	
	if request.method == 'GET':
		pform = ProyectoForm(prefix='pform')
		tforms = TareaFormSet(prefix='tforms')

		context = {
			'pform': pform,
			'formset': tforms
	    }

		return render(request, 'proyectos/nuevo_proyecto.html', context)
	
	else:	# POST
		pform = ProyectoForm(request.POST, prefix='pform')
		tforms = TareaFormSet(request.POST, prefix='tforms')

		if tforms.is_valid() and pform.is_valid():
			nuevo_proyecto = pform.save(commit=False)	# False: no guardar hasta que el objeto esté completo
			nuevo_proyecto.creador = request.user
			nuevo_proyecto.fecha_pub = datetime.datetime.now()
			nuevo_proyecto.terminado = False
			nuevo_proyecto.save()
			
			for tf in tforms:
				if tf.cleaned_data.get('nombre'):	# Si un formulario (formset) está completamente vacío, Django no lo valida
					nueva_tarea = tf.save(commit=False)
					nueva_tarea.proyecto = nuevo_proyecto
					nueva_tarea.terminada = False
					nueva_tarea.save()
			
			return redirect('proyectos:proyecto', nuevo_proyecto.id) 
			
		else:	# Algún formulario no válido
			context = {
				'pform': pform,
				'formset': tforms
			}
			
			return render(request, 'proyectos/nuevo_proyecto.html', context)


# Lista de proyectos del PM terminados
@login_required
@permission_required('auth.es_project_manager', login_url="proyectos:index")
def terminados(request):
	lista_proyectos = Proyecto.objects.filter(
							creador = request.user.id
							).filter(
							terminado = True
							)

	context = {
			'lista_proyectos': lista_proyectos
	}

	return render(request, 'proyectos/terminados.html', context)


# Información de una tarea y formulario para subir fichero
@login_required
def tarea(request, id_proyecto, id_tarea):
	tarea = get_object_or_404(Tarea, pk=id_tarea)
	proyecto = get_object_or_404(Proyecto, pk=id_proyecto)

	if request.method == 'GET':
		form = FilesForm()
		
		context = {
			'proyecto': proyecto,
			'tarea': tarea,
			'form': form
		}
		
		return render(request, 'proyectos/tarea.html', context)

	else:				# POST (se envía un fichero)	
		form = FilesForm(request.POST, request.FILES)

		if form.is_valid():
			subido = subido_trad = False
			
			if 'original' in request.FILES:
				tarea.original = request.FILES['original']
				subido = True
				
				"""# Enviar notificación a quien tiene la tarea asignada
				path = 'http://127.0.0.1:8000/proyectos/' + id_proyecto + '/' + id_tarea + '/'
				mensj = "Le informamos de que tiene disponible los archivos de una tarea asignada a usted. Puede seguir el siguiente enlace para verlos:\n\n" + path
				email_dest = tarea.asignada_a.email
				
				send_mail('Tarea disponible', mensj, settings.DEFAULT_FROM_EMAIL, [email_dest], fail_silently=False)"""
				
			if 'traducido' in request.FILES:
				tarea.traducido = request.FILES['traducido']
				subido = subido_trad = True
				
				"""# Notificar al PM que se ha terminado la tarea
				path = 'http://127.0.0.1:8000/proyectos/' + id_proyecto + '/' + id_tarea + '/'
				mensj = "Le informamos de que tiene disponible los archivos de una tarea terminada. Puede seguir el siguiente enlace para verlos:\n\n" + path
				email_dest = proyecto.creador.email
				
				send_mail('Tarea disponible', mensj, settings.DEFAULT_FROM_EMAIL, [email_dest], fail_silently=False)"""
			
			if subido:
				if subido_trad:
					tarea.terminada = True
					
				tarea.save()

				if not proyecto.tarea_set.filter(terminada=False):	# Si no quedan tareas sin terminar, se termina el proyecto
					proyecto.terminado = True
					proyecto.save()
			
			return redirect('proyectos:index')

		else:	# if form not valid
			context = {
				'proyecto': proyecto,
				'tarea': tarea,
				'form': form,
			}

			return render(request, 'proyectos/tarea.html', context)
			

# Lista de tareas del usuario finalizadas
@login_required
def tareas_terminadas(request):
	lista_tareas = tareas_pendientes = Tarea.objects.filter(
							asignada_a = request.user.id
							).filter(
							terminada = True
							)

	context = {
			'mensaje': 'Tareas terminadas',
			'lista_tareas': lista_tareas
	}

	return render(request, 'proyectos/tareas_terminadas.html', context)


###-------------------Gestión de usuarios----------------------------###
# Formulario de login
def web_login(request):

	if request.method == 'GET':
		form = LoginForm()
		context = {
			'form': form,
	    }

		return render(request, 'proyectos/login.html', context)

	else:
		form = LoginForm (request.POST)

		if form.is_valid ():
			usuario = form.cleaned_data['name']
			contrasenia = form.cleaned_data['password']

			user = authenticate(username = usuario, password = contrasenia)	# Verificar usuario y contraseña

			if user is not None and user.is_active:
				login (request, user)	# Éxito

				return redirect('proyectos:index')

			else:
				context = {
					'mensaje':'Usuario o contraseña no válido',
					'form': form,
	            }
				return render (request, 'proyectos/login.html', context)
		
		else:	# Formulario no válido (campo vacío)
			context = {
				'form': form,
	        }
			return render (request, 'proyectos/login.html', context)


# Desconectarse de la página 
@login_required
def web_logout(request):
    logout(request)
    return redirect('proyectos:index')


# Listar usuarios y formulario para añadir nuevo
@login_required
def usuarios(request):
	lista_usuarios = User.objects.all()
	
	if request.method == 'GET':
		form = NuevoUsuarioForm()
		context = {
			'lista_usuarios':lista_usuarios,
			'form': form,
		}

		return render(request, 'proyectos/usuarios.html', context)
		
	else:		# POST
		form = NuevoUsuarioForm(request.POST)
		
		if form.is_valid():
			# Generamos contraseña aleatoria
			num_caracteres_pass = 10
			p = ''.join([choice(string.ascii_letters + string.digits) for i in range(num_caracteres_pass)])
			
			new_user = User.objects.create_user(form.cleaned_data['username'],
                                  form.cleaned_data['email'],
                                  #password=p,)
                                  form.cleaned_data['password']) # QUITAR y descomentar lo de encima
			new_user.first_name = form.cleaned_data['nombre']
			new_user.last_name = form.cleaned_data['apellidos']
			new_user.save()
			
			if form.cleaned_data['es_pm']:
				g = Group.objects.get(name='Project Managers') 
				g.user_set.add(new_user)
			
			"""# Enviar notificación y contraseña al nuevo usuario
			path = "http://127.0.0.1:8000"
			mensj = "Le informamos de que se ha completado su registro en la web: \n\nUsuario: " + form.cleaned_data['username'] + "\nContraseña: " + p + "\n\nSe recomienda cambiar de contraseña. Puede seguir el siguiente enlace para acceder a la plataforma:\n\n" + path				
			send_mail('Bienvenido a la web de proyectos de traducción', mensj, settings.DEFAULT_FROM_EMAIL, [form.cleaned_data['email']], fail_silently=False)
			"""
			return redirect('proyectos:index')

		else:
			context = {
				'lista_usuarios': lista_usuarios,
				'form': form,
	        }
	        
			return render (request, 'proyectos/usuarios.html', context)


# Datos de un usuario y contraseña
@login_required
def usuario(request, id_usuario):
	usuario = get_object_or_404(User, pk=id_usuario)
	tareas_pendientes = Tarea.objects.filter(
							asignada_a = id_usuario
							).filter(
							terminada = False
							).count()
	
	if request.method == 'GET':
		form = NewPassForm()
		context = {
			'usuario': usuario,
			'num_tareas': tareas_pendientes,
			'form': form,
		}
		
		return render(request, 'proyectos/usuario.html', context)
	
	else:		# POST
		form = NewPassForm(request.POST)
		
		if form.is_valid():
			contrasenia = form.cleaned_data['old_pass']
			nueva_c = form.cleaned_data['new_pass']
			
			if usuario.check_password(contrasenia):
				usuario.set_password(nueva_c)
				usuario.save()
				
				return redirect('proyectos:usuarios')
			else:
				context = {
					'mensaje':'Error, la contraseña no es correcta',
					'usuario': usuario,
					'num_tareas': tareas_pendientes,
					'form': form,
				}
				return render (request, 'proyectos/usuario.html', context)
		
		else:
			context = {
				'mensaje':'Error, las contraseñas no coinciden',
				'usuario': usuario,
				'num_tareas': tareas_pendientes,
				'form': form,
	        }
			return render (request, 'proyectos/usuario.html', context)


# Borrar usuario
@login_required
@permission_required('auth.es_project_manager', login_url="proyectos:usuarios")
def baja(request, id_usuario):
    u = get_object_or_404(User, pk=id_usuario)
    u.delete()

    return redirect('proyectos:usuarios')

