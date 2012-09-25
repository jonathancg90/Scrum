from django.db import models

class Project(models.Model): 
    nombre = models.CharField(verbose_name='nombre',max_length=50)
    descrip = models.TextField(verbose_name='Descripcion')
    
    
    def __unicode__(self):
        return self.nombre

class Sprint(models.Model):
    titulo = models.CharField(verbose_name='titulo',max_length=50)
    descrip = models.TextField(verbose_name='Descripcion')
    project    = models.ForeignKey(Project)
    
    def __unicode__(self):
        return self.titulo
    
class UserStory(models.Model):
    titulo = models.CharField(verbose_name='titulo',max_length=50)
    descrip = models.TextField(verbose_name='Descripcion')
    peso = models.IntegerField(verbose_name='Peso')
    sprint    = models.ForeignKey(Sprint)
    
    def __unicode__(self):
        return self.titulo