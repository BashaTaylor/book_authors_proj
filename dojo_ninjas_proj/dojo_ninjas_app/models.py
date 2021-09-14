from django.db import models

# Create your models here.
class Dojo(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    description = models.TextField(default='old dojo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.name} {self.city} {self.state} {self.description}"

class Ninja(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name='ninjas',on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"{self.first_name} {self.last_name} {self.dojo}"





# from django.db import models

# class dojo(models.Model):
#     name = models.CharField(max_length=255)
#     city = models.CharField(max_length=255)
#     state = models.CharField(max_length=255)
#     desc = models.TextField(default="old dojo")
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
#     #ninjas = A list of ninjas at the dojo

#     def __repr__ (self):
#         return (f"Dojo Object: Id #:{self.id}, Name:{self.name}, City:{self.city}, State:{self.state}, Type:{self.desc}, Created at:{self.created_at}")

# class ninja (models.Model):
#     dojo = models.ForeignKey(dojo, related_name="ninjas", on_delete=models.CASCADE)
#     first_name = models.CharField(max_length=255)
#     last_name = models.CharField(max_length=255)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)    
    
#     def __repr__ (self):
#         return (f"Ninja Object: Id #:{self.id}, First Name:{self.first_name}, Last_Name:{self.last_name}, Dojo:{self.dojo}, Created at:{self.created_at}")