from django.db import models
from django.core.validators import FileExtensionValidator

class Filme(models.Model):
    titulo = models.CharField(max_length=100)
    produtor = models.CharField(max_length=100)
    ator = models.CharField(max_length=100,blank=True)
    capa = models.ImageField(upload_to='capas/', validators=[FileExtensionValidator(['png', 'jpg', 'jpeg'])])

    def __str__(self):
        return f"{self.titulo} {self.produtor}"

class Playlist(models.Model):
    nome = models.CharField(max_length=100)
    filmes = models.ManyToManyField(Filme)  

    def __str__(self):
        return self.nome


