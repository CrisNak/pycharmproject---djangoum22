from django.db import models

'''
USUARIO NÃO COSTUMIZAVEL

from django.contrib.auth.models import User

class Post(models.Model):
    autor = models.ForeignKey(User, verbose_name='Autor', on_delete=,models.CASCADE)
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)
    
    def __str__(self):
        return self.titulo
'''

'''
USUARIO COSTUMIZAVEL 1

from django.conf import settings

class Post(models.Model):
    autor = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name='Autor', on_delete=,models.CASCADE)
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo
'''
#USUARIO COSTUMIZAVEL 2

from django.contrib.auth import get_user_model

class Post(models.Model):
    autor = models.ForeignKey(get_user_model(), verbose_name='Autor', on_delete=models.CASCADE)
    titulo = models.CharField('Título', max_length=100)
    texto = models.TextField('Texto', max_length=400)

    def __str__(self):
        return self.titulo