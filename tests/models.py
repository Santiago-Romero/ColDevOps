from django.db import models

class Test(models.Model):
    nombre = models.CharField(max_length=50)
    valor = models.BigIntegerField()
    fecha=models.DateTimeField(auto_now=False, auto_now_add=False)
    def __str__(self):
        return self.nombre