from django.db import models

# Create your models here.
class Show(models.Model):

    name = models.CharField(max_length=255)
    network = models.CharField(max_length=255)
    release_date = models.DateField()
    description = models.CharField(max_length=255)
    # objects = ShowManager()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f'<{self.title}, {self.network}, {self.release_date}, {self.description})>'