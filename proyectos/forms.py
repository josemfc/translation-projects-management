from django import forms
from django.contrib.auth.models import User
from proyectos.models import Proyecto, Tarea
from djangoformsetjs.utils import formset_media_js

class LoginForm (forms.Form):
	name = forms.CharField (label      = 'Nombre de usuario', 
                            max_length = 30, 
                            required   = True,
                            )
                             
	password = forms.CharField ( label = 'Contraseña',
	                             max_length = 20,
	                             widget=forms.PasswordInput(),
	)


class NuevoUsuarioForm (forms.Form):
	username = forms.CharField(label  = 'Nombre de usuario',
								max_length = 30,
								required   = True,
								)
	nombre = forms.CharField(label = 'Nombre',
								max_length = 30,
								)
	apellidos = forms.CharField(label = 'Apellidos',
								max_length = 30,
								)
	email = forms.EmailField(label='Correo electrónico',
								required   = True,
								)
	"""password = forms.CharField (label = 'Contraseña',
								max_length = 20,
								widget=forms.PasswordInput(),
								)"""
	es_pm = forms.BooleanField(label = 'Project Manager',
								required = False)
				
	def clean(self):
		username = self.cleaned_data['username']
		if User.objects.all().filter(username=username).exists():
			raise forms.ValidationError('El usuario \'%s\' ya existe.' % username)


class NewPassForm(forms.Form):
	old_pass = forms.CharField (label = 'Contraseña actual',
								max_length = 20,
								widget=forms.PasswordInput(),
								)
	new_pass = forms.CharField (label = 'Nueva contraseña',
								max_length = 20,
								widget=forms.PasswordInput(),
								)
	new_pass2 = forms.CharField (label = 'Repita la nueva contraseña',
								max_length = 20,
								widget=forms.PasswordInput(),
								)
								
	def clean (self):
		cleaned_data = super(NewPassForm, self).clean()
		c  = cleaned_data.get("new_pass")
		c2 = cleaned_data.get("new_pass2")
		if c != c2:
			raise forms.ValidationError ('Las contraseñas no coinciden')


class ProyectoForm(forms.ModelForm):
	class Meta:
		model = Proyecto
		fields = ['nombre']
		
	def clean(self):		# Comprobar si el nombre de proyecto es único
		cleaned_data = super(ProyectoForm, self).clean()
		n = cleaned_data.get("nombre")
		if Proyecto.objects.all().filter(nombre=n).exists():
			raise forms.ValidationError('Ya existe un proyecto con ese nombre, elija otro')


class TareaForm(forms.ModelForm):
	class Media(object):
		js = formset_media_js
	
	class Meta:
		model = Tarea
		exclude = ('proyecto', 'terminada', 'original', 'traducido', 'id') # Con formset es necesario excluir id
		
	def clean(self):		# Comprobar que el número de horas no sea negativo
		cleaned_data = super(TareaForm, self).clean()
		n = cleaned_data.get("num_horas")
		if n < 0:
			raise forms.ValidationError('El número de horas no puede ser negativo')


class FilesForm(forms.Form):
	original = forms.FileField(
		label='Selecciona un archivo',
		required = False,
		)
		
	traducido = forms.FileField(
		label='Selecciona un archivo',
		required = False,
		)


