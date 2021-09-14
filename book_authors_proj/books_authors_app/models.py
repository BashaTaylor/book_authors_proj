from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=255)
    desc = models.TextField((''))
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __repr__(self):
        return f'{self.title}, {self.desc}'

class Author(models.Model):
    books = models.ManyToManyField(Book, related_name="Authors")
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    notes = models.CharField(max_length=45, default='NotesDefault')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'{self.first_name},{self.last_name}'



# , {self.notes}

# class Movie(models.Model):
#     title = models.CharField(max_length=45)
#     description = models.TextField()
#     release_date = models.DateTimeField()
#     duration = models.IntegerField()
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

