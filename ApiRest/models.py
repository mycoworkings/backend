from django.db import models

# Create your models here.



class facebook(models.Model):
     facebookUrl = models.CharField(max_length=128)

class instagram(models.Model):
     instagramUrl = models.CharField(max_length=128)

class twitter(models.Model):
     twitterUrl = models.CharField(max_length=128)

class linkedin(models.Model):
     linkedinUrl = models.CharField(max_length=130)

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



class description(models.Model):
     name = models.CharField(max_length=128)
     openingDate = models.CharField(max_length=128)
     description = models.CharField(max_length=128)


class location(models.Model):
     provinceCode = models.IntegerField()
     munipalityCode = models.IntegerField()
     streetCode = models.IntegerField()
     postalCode = models.CharField(max_length=128)
     latitude = models.FloatField()
     longitude = models.FloatField()


class basicServices(models.Model):
     hasWifi = models.BooleanField(default=False)
     hasClimatization = models.BooleanField(default=False)
     is24h = models.BooleanField(default=False)
     hasCoffe = models.BooleanField(default=False)

class communityServices(models.Model):
     hasEvents = models.BooleanField(default=False)
     hasWorkshops = models.BooleanField(default=False)
     hasAccelerator = models.BooleanField(default=False)
     hasIncubator = models.BooleanField(default=False)

class relaxServices(models.Model):
     hasTerrace = models.BooleanField(default=False)
     hasChillOutArea = models.BooleanField(default=False)

class services(models.Model):
     basicServices = models.ForeignKey(basicServices,on_delete=models.CASCADE,null=True)
     communityServices = models.ForeignKey(communityServices,on_delete=models.CASCADE,null=True)
     relaxServices = models.ForeignKey(relaxServices,on_delete=models.CASCADE,null=True)






class meetingRoom(models.Model):


     name = models.CharField(max_length=128)
     capacity = models.IntegerField(null=True)
     pricePerDay = models.IntegerField(null=True)
     pricePerWeek = models.IntegerField(null=True)
     pricePerMonth = models.IntegerField(null=True)
     description = models.CharField(max_length=128)
     openingHours = models.CharField(max_length=128)

class meetingRooms(models.Model):
      rooms = models.ManyToManyField(meetingRoom)


class desk(models.Model):
     deskTypeName = models.CharField(max_length=128)
     totalPlaces = models.IntegerField(null=True)
     pricePerDay = models.IntegerField(null=True)
     pricePerWeek = models.IntegerField(null=True)
     pricePerMonth = models.IntegerField(null=True)
     description = models.CharField(max_length=128)
     openingHours = models.CharField(max_length=128)

class desks(models.Model):
      rooms = models.ManyToManyField(desk)

class conferenceRoom(models.Model):
     conferenceRoomName = models.CharField(max_length=128)
     totalPlaces = models.IntegerField(null=True)
     pricePerDay = models.IntegerField(null=True)
     pricePerWeek = models.IntegerField(null=True)
     pricePerMonth = models.IntegerField(null=True)
     description = models.CharField(max_length=128)
     openingHours = models.CharField(max_length=128)

class conferenceRooms(models.Model):
      rooms = models.ManyToManyField(conferenceRoom)




class Coworking(models.Model):
     Contact = models.ForeignKey(Contact,on_delete=models.CASCADE)
     description = models.ForeignKey(description,on_delete=models.CASCADE,default=None,null=True)
     location = models.ForeignKey(location,on_delete=models.CASCADE,default=None,null=True)
     services = models.ForeignKey(services,on_delete=models.CASCADE,default=None,null=True)
     meetingRooms = models.ForeignKey(meetingRooms,on_delete=models.CASCADE,default=None,null=True)
     desks = models.ForeignKey(desks,on_delete=models.CASCADE,default=None,null=True)
     conferenceRooms = models.ForeignKey(conferenceRooms,on_delete=models.CASCADE,default=None,null=True)

##############
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