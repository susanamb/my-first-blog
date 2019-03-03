from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    #esta línea define nuestro modelo (es un objeto)
    #class es una palabra clave que indica que estamos definiendo un objeto.
    #Post es el nombre de nuestro modelo. Podemos darle un nombre diferente(empieza en mayuscula)
    #models.Model significa que Post es un modelo de Django
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    #ForeignKey, este es una relación (link) con otro modelo.
    title = models.CharField(max_length=200)
    #.CharField, así es como defines un texto con un número limitado de caracteres.
    text = models.TextField()
    #TextField, este es para texto largo sin límite.(p/entrada blog)
    created_date = models.DateTimeField(
            default=timezone.now)
            #DateTimeField fecha y hora
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
