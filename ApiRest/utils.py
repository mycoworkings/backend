import pymysql
from ApiRest.models import *
from django.core import serializers
import json



#con = GetMysqlConn()

class MySql():

    def __init__(self):
        try:
            self._conn = pymysql.connect('localhost',
                             'root',
                             'espinete',
							'mycoworkings',charset='utf8', 
							use_unicode=True)
            self._cursor = self._conn.cursor()
        except Exception:
            print ('error: no me pude conectar 1!')
            return False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.commit()
        self.connection.close()

    @property
    def connection(self):
        return self._conn

    @property
    def cursor(self):
        return self._cursor

    def commit(self):
        self.connection.commit()

    def execute(self, sql, params=None):
        return self.cursor.execute(sql, params or ())

    def fetchall(self):
        return self.cursor.fetchall()

    def fetchone(self):
        return self.cursor.fetchone()

    def query(self, sql, params=None):
        self.cursor.execute(sql, params or ())
        return self.fetchall()



def GetCoworking_function(token):

    Coworking_instance_search = Coworking.objects.filter(pk=token)

    Coworking_search = Coworking_instance_search.first()

    serialized_obj = serializers.serialize('json', [ Coworking_search, ])

    

    Final_response = json.loads(serialized_obj)[0]["fields"]

    # LOOK FOR LOCATION

    location_instance_search = Coworking_search.location

    serialized_location = serializers.serialize('json', [ location_instance_search, ])
    Final_response["location"]= json.loads(serialized_location)[0]["fields"]
    
    # LOOK FOR description

    description_search = Coworking_search.description

    serialized_description = serializers.serialize('json', [ description_search, ])
    Final_response["description"]= json.loads(serialized_description)[0]["fields"]

    # look for contact

    contact_search = Coworking_search.Contact

    serialized_contact = json.loads(serializers.serialize('json', [ contact_search, ]))[0]["fields"]

    socialMedia_search = contact_search.socialMedia

    serialized_socialMedia = json.loads(serializers.serialize('json', [ socialMedia_search, ]))[0]["fields"]

    ##social Media

    facebook_search = socialMedia_search.facebook

    twitter_search = socialMedia_search.twitter

    linkedin_search = socialMedia_search.linkedin

    instagram_search = socialMedia_search.instagram

    if facebook_search is not None:

        serialized_facebook = json.loads(serializers.serialize('json', [ facebook_search, ]))[0]["fields"]

        serialized_socialMedia["facebook"] = serialized_facebook

    if twitter_search is not None:

        serialized_twitter = json.loads(serializers.serialize('json', [ twitter_search, ]))[0]["fields"]

        serialized_socialMedia["twitter"] = serialized_twitter

    if linkedin_search is not None:

        serialized_linkedin = json.loads(serializers.serialize('json', [ linkedin_search, ]))[0]["fields"]

        serialized_socialMedia["linkedin"] = serialized_linkedin

    if instagram_search is not None:

        serialized_instagram = json.loads(serializers.serialize('json', [ instagram_search, ]))[0]["fields"]

        serialized_socialMedia["instagram"] = serialized_instagram

    serialized_contact["socialMedia"] = serialized_socialMedia

    Final_response["Contact"]= serialized_contact
    

    # look for services

    services_search = Coworking_search.services

    serialized_services = json.loads(serializers.serialize('json', [ services_search, ]))[0]["fields"]



    communityServices_search = services_search.communityServices

    serialized_communityServices = json.loads(serializers.serialize('json', [ communityServices_search, ]))[0]["fields"]

    serialized_services["communityServices"]=serialized_communityServices
    

    
    Final_response["services"]= serialized_services


    ##

    basicServices_search = services_search.basicServices

    serialized_basicServices = json.loads(serializers.serialize('json', [ basicServices_search, ]))[0]["fields"]

    serialized_services["basicServices"]=serialized_basicServices
    
    ##

    relaxServices_search = services_search.relaxServices

    serialized_relaxServices = json.loads(serializers.serialize('json', [ relaxServices_search, ]))[0]["fields"]

    serialized_services["relaxServices"]=serialized_relaxServices
    
    
    Final_response["services"]= serialized_services

    # Get Conference rooms

    #conferenceRooms_search = Coworking_search.conferenceRooms

    conferenceRooms_search = conferenceRooms.objects.filter(pk=Coworking_search.conferenceRooms.pk)
    Array_pk_conferenceroom = json.loads(serializers.serialize('json', [ conferenceRooms_search.first(), ]))[0]["fields"]["rooms"]
    conferenceRooms_final = []

    for room in Array_pk_conferenceroom:

        Room = conferenceRoom.objects.filter(pk=room)
        serialized_room = json.loads(serializers.serialize('json', [ Room.first(), ]))[0]["fields"]
        conferenceRooms_final.append(serialized_room)
        

    Final_response["conferenceRooms"]= conferenceRooms_final

    # Get meetingRooms


    meetingRooms_search = meetingRooms.objects.filter(pk=Coworking_search.meetingRooms.pk)
    Array_pk_meetingRooms = json.loads(serializers.serialize('json', [ meetingRooms_search.first(), ]))[0]["fields"]["rooms"]
    meetingRooms_final = []

    for room in Array_pk_meetingRooms:

        Room = meetingRoom.objects.filter(pk=room)
        serialized_room = json.loads(serializers.serialize('json', [ Room.first(), ]))[0]["fields"]
        meetingRooms_final.append(serialized_room)
        

    Final_response["meetingRooms"]= meetingRooms_final


    # Get desks


    desks_search = desks.objects.filter(pk=Coworking_search.desks.pk)
    Array_pk_desks = json.loads(serializers.serialize('json', [ desks_search.first(), ]))[0]["fields"]["rooms"]
    desks_final = []

    for room in Array_pk_desks:

        Room = desk.objects.filter(pk=room)
        serialized_room = json.loads(serializers.serialize('json', [ Room.first(), ]))[0]["fields"]
        desks_final.append(serialized_room)
        

    Final_response["desks"]= desks_final

    return Final_response