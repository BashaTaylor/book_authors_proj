from django.db import models
import re
from django.db.models.deletion import CASCADE

# Create your models here.

class UserManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        #validate the length of the first name, last name, password
        if len(reqPOST['first_name']) < 2:
            errors['first_name'] = 'First name requires at least 2 characters.'
        if len(reqPOST['last_name']) < 2:
            errors['last_name'] = 'Last name requires at least 2 characters.'    
        if len(reqPOST['email']) < 6:
            errors['email'] = 'Email requires at least 6 characters.'
        if len(reqPOST['password']) < 8:
            errors['password'] = 'Password requires at least 8 characters.'
        if reqPOST['password'] != reqPOST['confirm_pw']:
            errors['match']='Incorrect password or confirmation.'
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqPOST['email']):
            errors['regex']=("Invalid email address!")
        users_with_email=User.objects.filter(email=reqPOST['email'])
        # this would return a list
        # you can't use the same email
        if len(users_with_email) >= 1:
            errors['dup']='Email taken, use other email'
        return errors
class TripManager(models.Manager):
    def trip_validator(self, reqPOST):
        errors = {}
        if len(reqPOST['destination']) < 3:
            errors['destination'] = 'destination requires at least 3 characters.'
        if len(reqPOST['start_date']) == 0:
            errors['start_date'] = 'Start_date requires a dd/mm/yyy format, should not be blank and cannot be in the past and must be provided'   
        if len(reqPOST['end_date']) == 0:
            errors['end_date'] = 'End_date requires a dd/mm/yyy format, should not be blank and cannot be in the past and must be provided.' 
        if len(reqPOST['plan']) < 3:
            errors['plan'] = 'Plan requires at least 3 characters.'
        
        return errors


class User(models.Model):
    first_name=models.TextField()
    last_name=models.TextField()
    email=models.TextField()
    password=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

#Note to self; may need to include email below:
    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

class Trip(models.Model):
    destination=models.TextField()
    start_date=models.DateTimeField(auto_now_add=True)
    end_date=models.DateTimeField(auto_now_add=True)
    plan=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    created_by=models.ForeignKey(User, related_name='trip_submitter', on_delete=CASCADE)
    objects=TripManager()
    user_joined=models.ManyToManyField(User, related_name='trip_joined')

    def __str__(self):
        return f'{self.destination}, {self.start_date}, {self.end_date}, {self.plan}, {self.created_by}'

# class OthersTrip(models.Model):
#     other_destination=models.TextField()
#     otherstart_date=models.DateTimeField(auto_now_add=True)
#     otherend_date=models.DateTimeField(auto_now_add=True)
#     other_plan=models.TextField()
#     othercreated_at=models.DateTimeField(auto_now_add=True)
#     otherupdated_at=models.DateTimeField(auto_now=True)
#     join=models.ForeignKey(Trip, related_name='join_trip_submitter', on_delete=CASCADE)
#     # created_by=models.ForeignKey(User, related_name='trip_submitter', on_delete=CASCADE)

#     objects=TripManager() 


#     def __str__(self):
#         return f'{self.other_destination}, {self.otherstart_date}, {self.otherend_date}, {self.otherplan}, {self.join}'