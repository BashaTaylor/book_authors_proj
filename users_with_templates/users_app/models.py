from django.db import models

# Create your models here.
class User(models.Model):

    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'<{self.first_name}, {self.last_name})>'
        # return '{} {}'.format(self.first_name, self.last_name)
