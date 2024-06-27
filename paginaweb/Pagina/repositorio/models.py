from django.db import models

class usuarios(models.Model):
    primary=models.AutoField(primary_key=True)
    nombre=models.CharField(max_length=50,null=False)
    password=models.CharField(max_length=20,null=False)
    email=models.CharField(max_length=40,null=False)



    def __str__(self):
            return f"Nombre: {self.nombre}, Email:  {self.email}"

# Create your models here.
