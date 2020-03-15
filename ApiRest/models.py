from django.db import models

# Create your models here.

class Contact(models.Model):

    WebUrl = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)


class Coworking(models.Model):
     Contact = models.ForeignKey(Contact,on_delete=models.CASCADE)








class Person(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name

class Group(models.Model):
    name = models.CharField(max_length=128)
    members = models.ManyToManyField(Person, through='Membership')

    def __str__(self):
        return self.name

class Membership(models.Model):
    person = models.ForeignKey(Person, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    invite_reason = models.CharField(max_length=64)