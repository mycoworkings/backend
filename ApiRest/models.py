from django.db import models

# Create your models here.



class facebook(models.Model):
     facebookUrl = models.CharField(max_length=128)

class instagram(models.Model):
     instagramUrl = models.CharField(max_length=128)

class twitter(models.Model):
     twitterUrl = models.CharField(max_length=128)

class linkedin(models.Model):
     linkedinUrl = models.CharField(max_length=128)

class socialMedia(models.Model):
     facebook = models.ForeignKey(facebook,on_delete=models.CASCADE,null=True)
     instagram = models.ForeignKey(instagram,on_delete=models.CASCADE,null=True)
     twitter = models.ForeignKey(twitter,on_delete=models.CASCADE,null=True)
     linkedin = models.ForeignKey(linkedin,on_delete=models.CASCADE,null=True)

class Contact(models.Model):

    WebUrl = models.CharField(max_length=50)
    phoneNumber = models.CharField(max_length=50)
    Email = models.CharField(max_length=100)
    socialMedia = models.ForeignKey(socialMedia,on_delete=models.CASCADE,null=True)

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