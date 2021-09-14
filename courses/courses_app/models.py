from __future__ import unicode_literals
from django.db import models

# Create your models here.
class CommentManager(models.Manager):
    # def validator(self,postData):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['content']) < 5:
            errors['content'] = "Comment must be at least 5 characters"
        return errors

class CourseManager(models.Manager):
    # def validator(self, postData):
    def basic_validator(self,postData):
        errors = {}
        # add keys and values to errors dictionary for each invalid field
        #Ensure that the name entered is more than 5 characters, and the description is more than 15 characters
        if len(postData['course_name']) < 5:
            errors["title"] = "Course name should be at least 5 characters"
        if len(postData['description']) < 15:
            errors['description'] = "Course description should be at least 15 characters"
        return errors

# class Description(models.Model):
#     content = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Course(models.Model):
    course_name = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

# class Course(models.Model):
    # course_name = models.TextField()
    # description = models.TextField()
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)

    # course_name = models.CharField(max_length=255)
    # created_at = models.DateTimeField(auto_now_add=True)
    # updated_at = models.DateTimeField(auto_now=True)
    # description = models.OneToOneField(Description,related_name="course", null=True,on_delete=models.CASCADE)

    objects = CourseManager()

class Comment(models.Model):
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, related_name="has_comments",on_delete=models.CASCADE)

    objects = CommentManager()