from django.db import models


class Course(models.Model):
    name = models.CharField(max_length=40)
    code = models.IntegerField()

    def __str__(self):
        return f'{self.name} course --'


class Student(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()

    def __str__(self):
        return f'Nombre del Estudiante: {self.name} {self.last_name} -- e-mail: {self.email}'


class Profesor(models.Model):
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    email = models.EmailField()
    profession = models.CharField(max_length=40)

    def __str__(self):
        return f'Nombre del Profesor: {self.name} {self.last_name} -- e-mail: {self.email} -- profesión: {self.profession} --'


class Copas (models.Model):
    
    name = models.CharField(max_length=20)
    pais = models.CharField(max_length=20)
    
       
class Clubes(models.Model):
    
    name = models.CharField(max_length=20)
    division = models.CharField(max_length=30)
    liga = models.CharField(max_length=30)
   
    
class Ligas(models.Model):
    
    name = models.CharField(max_length=25)
    pais = models.CharField(max_length=30)
    