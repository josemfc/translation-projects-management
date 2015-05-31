from django.test import TestCase
from django.test import Client
import unittest

from django.core import mail
from django.contrib.auth.models import User
from django.conf import settings
from proyectos.models import *
import datetime


# Comprobar envío de email
class EmailTest(TestCase):
	def test_send_email(self):
		
		mail.send_mail('Asunto', 'Mensaje',
			settings.DEFAULT_FROM_EMAIL, ['josemfc@correo.ugr.es'],
			fail_silently=False)
			
		self.assertEqual(len(mail.outbox), 1) # Test that one message has been sent
		self.assertEqual(mail.outbox[0].subject, 'Asunto') # Verify that the subject of the first message is correct


# Pruebas en Proyecto y Tarea
class ProyectoTestCase(TestCase):
	def setUp(self):
		u = User.objects.create(username="user_test")
		p = Proyecto.objects.create(creador=u, nombre="test", fecha_pub=datetime.datetime.now())
		Tarea.objects.create(proyecto=p, asignada_a=u, nombre="tarea_test", num_horas=-1)
		
	def test_horas_no_negativo(self):
		#num_horas no puede ser negativo
		t = Tarea.objects.get(nombre="tarea_test")
		
		self.assertTrue(t.num_horas > -1)

##################### TESTs CON EL SHELL ###########################
"""
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
>>> from django.test import Client
>>> c = Client()
>>> response = client.get('/')

>>> response = c.get('/')
>>> response.status_code
200
>>> response.content
b'<!DOCTYPE html>\n<html>\n<head>...

"""
########################################################################
# Comprobar si el proyecto acaba al acabar las tareas
"""
>>> from django.test.utils import setup_test_environment
>>> setup_test_environment()
>>> from django.test import Client
>>> c = Client()

>>> response = c.post('/proyectos/login/', {'name': "usuario2", 'password': "1234"}, follow = True)

>>> with open('/home/jose/get-pip.py') as f:
...   response = c.post('/proyectos/22/19/', {'traducido': f})
... 

# Para comprobar: Siendo proyect manager, ir a la página del proyecto y buscar 'Sí' en la tabla de la página
>>> response = c.get('/proyectos/22/')
>>> response.content
...S\xc3\xad...

# O también ir a la página de proyectos terminados y buscar el nombre del proyecto
>>> response = c.get('/proyectos/terminados/')
>>> response.content

"""
