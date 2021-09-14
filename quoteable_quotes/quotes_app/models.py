from django.db import models
import re
# Create your models here.
class UserManager(models.Manager):
    # def basic_validator(self, postdata):
    def register_validator(self, postdata):
        errors = {}
        email_checker = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postdata['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters"
        if not email_checker.match(postdata['email']):
            errors['email'] = 'Email must be valid'
        if postdata['password'] != postdata['confirm_password']:
            errors['password'] = 'Password and Confirm Password do not match'
        return errors
        
    def login_validator(self, postData):
        errors = {}
        users = User.objects.filter(email=postData['email'])
        if len(postData['email']) < 1:
            errors['email'] = 'Email can not be blank.'
        if len(postData['password']) < 8:
            errors['password'] = 'Password requires at least 8 characters.'
    def edit_validator(self, postData, logged_user_id):
        errors = {}
        users = User.objects.filter(email=postData['email'])
        user_tied_to_email = users[0]
        if users:
            my_user = User.objects.get(id=logged_user_id)
            if my_user.email != user_tied_to_email:
                errors['email'] = 'Email is already in use.'
        if len(postData['first_name']) < 2:
            errors['first_name'] = 'First name requires at least 2 characters.'
        
        if len(postData['password']) < 8:
            errors['password'] = 'Password requires at least 8 characters.'
        if postData['password'] != postData['confirm_password']:
            errors['confirm_password']='Password must match.'
        return errors

class User(models.Model):
    first_name=models.CharField(max_length=45)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
    

class QuoteManager(models.Manager):
    #define BookManager:
    def quote_validator(self,postData):
        errors = {}
        if len(postData['quoted_by']) < 2:
            errors['quoted_by'] = 'Quoted by requires at least 2 characters.'
        if len(postData['message']) < 5:
            errors['message'] = 'Message requires at least 10 characters.'
        return errors


class Quote(models.Model):
    quote = models.CharField(max_length = 255)
    description = models.CharField(max_length = 255)
    uploaded_by = models.ForeignKey(User, related_name="quotes_uploaded", on_delete=models.CASCADE)
    users_who_like = models.ManyToManyField(User, related_name = "liked_quotes")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = QuoteManager()

class Wall_Message(models.Model):
    message = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_messages', on_delete=models.CASCADE)
    user_likes = models.ManyToManyField(User, related_name='liked_posts')

class Comment(models.Model):
    comment = models.CharField(max_length=255)
    poster = models.ForeignKey(User, related_name='user_comments', on_delete=models.CASCADE)
    wall_message = models.ForeignKey(Wall_Message, related_name="post_comments", on_delete=models.CASCADE)

