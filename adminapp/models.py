from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
from django.db import models

class Task(models.Model):
    title = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def str(self):
        return self.title

from django.db import models


class StudentList(models.Model):
    Register_Number = models.CharField(max_length=20,unique=True)
    Name = models.CharField(max_length=100)

    def str(self):
        return self.Register_Number


from django.db import models

class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    description = models.TextField()

    def __str__(self):
        return self.name
