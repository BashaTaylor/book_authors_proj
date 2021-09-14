from django.db import models
import re

# Create your models here.

class UserManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        #valicate the length of the first name, last name, password
        if len(reqPOST['first_name']) < 2:
            errors['first_name'] = 'First name does not have enough characters'
        if len(reqPOST['last_name']) < 2:
            errors['last_name'] = 'Last name does not have enough characters'    
        if len(reqPOST['email']) < 6:
            errors['email'] = 'Email is too short'
        if len(reqPOST['password']) < 8:
            errors['password'] = 'Password is too short'
        if reqPOST['password'] != reqPOST['confirm_pw']:
            errors['match']='Incorrect password or confirmation'
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqPOST['email']):
            errors['regex']=("Invalid email address!")
        users_with_email=User.objects.filter(email=reqPOST['email'])
        # this would return a list
        # you can't use the same email
        if len(users_with_email) >= 1:
            errors['dup']='Email taken, use other email'
        return errors


class User(models.Model):
    first_name=models.TextField()
    last_name=models.TextField()
    email=models.TextField()
    password=models.TextField()
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
