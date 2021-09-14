from django.db import models
from django.db.models.deletion import CASCADE
import re

# Create your models here.
class UserManager(models.Manager):
    def basic_validator(self, postdata):
        errors = {}
        email_checker = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postdata['pw']) < 8:
            errors['pw'] = "Your password must be at least 8 characters"
        if len(postdata['fname']) < 2 or len(postdata['lname']) < 2:
            errors['name'] = "Your name must be at least 2 characters"
        if not email_checker.match(postdata['email']):
            errors['email'] = 'Email must be valid'
        if postdata['pw'] != postdata['confpw']:
            errors['pw'] = 'Password and Confirm Password do not match'
        return errors
        

class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()
    # MTM
    # favorite_quotes = a list of quotes favorited by users
    # OTM
    # submitter = a person who submitted a quote

class QuoteManager(models.Manager):
    def quote_validator(self,postData):
        errors = {}
        if len(postData['quoted_by']) < 2:
            errors['quoted_by'] = 'Quoted by requires at least 2 characters.'
        if len(postData['message']) < 10:
            errors['message'] = 'Message requires at least 10 characters.'
        return errors

class Quote(models.Model):
    message = models.CharField(max_length=255)
    quoted_by = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()
    # OTM: a given user who posted a quote
    posted_by = models.ForeignKey(User, related_name='submitter', on_delete=CASCADE)
    # MTM: a list of users who favorited quotes
    list_of_favorites = models.ManyToManyField(User, related_name='favorite_quotes')
    user_likes = models.ManyToManyField(User, related_name='liked_posts')









