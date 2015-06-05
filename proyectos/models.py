# coding=utf-8

from django.db import models
from django.contrib.auth.models import User
import os


class Proyecto(models.Model):
	creador = models.ForeignKey(User)
	nombre = models.CharField(max_length=200)
	fecha_pub = models.DateTimeField('Fecha de publicacion')
	terminado = models.BooleanField(default=False)

	def __str__(self):
		return self.nombre


"""# heroku puede dar problemas a la hora de crear ficheros
def upload_path_handler(instance, filename):	# Indica dónde subir archivo
    return "proyectos/{id_p}/{id_t}/{f}".format(id_p=instance.proyecto.id, id_t=instance.id, f=filename)
"""

class Tarea(models.Model):
	proyecto = models.ForeignKey(Proyecto)
	asignada_a = models.ForeignKey(User)
	nombre = models.CharField(max_length=50)
	comentario = models.CharField(max_length=300, null=True, blank=True)
	terminada = models.BooleanField(default=False)
	num_horas = models.IntegerField('Num. de horas estimado')
	original = models.FileField('Texto original', upload_to=upload_path_handler, null=True, blank=True)
	traducido = models.FileField('Texto traducido', upload_to=upload_path_handler, null=True, blank=True)
	TIPO_TAREA = (
		('T', 'Traducción'),
		('R', 'Revisión'),
	)
	tipo_tarea = models.CharField(max_length=15, choices = TIPO_TAREA, default = 'T')
	
	def _get_filename_o(self):
		return os.path.basename(self.original.name)
	
	def _get_filename_t(self):
		return os.path.basename(self.traducido.name)
	
	filename_o = property(_get_filename_o)
	filename_t = property(_get_filename_t)
	
	def __str__(self):
		return self.nombre
	
	def __str__(self):
		return self.comentario

		
