from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=256)
    description = models.TextField()
    technology = models.CharField(max_length=256)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.title
