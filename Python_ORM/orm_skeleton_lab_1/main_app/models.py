from django.db import models

# Create your models here.


class Person(models.Model):
    full_name = models.CharField(max_length=50)
    age = models.IntegerField(null=True)


class Animal(models.Model):
    name = models.CharField(20)


class Dog(Animal):
    breed = models.CharField(20)
    owner = models.ForeignKey(Person, on_delete=models.CASCADE)