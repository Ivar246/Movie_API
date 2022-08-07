from django.db import models

# Create your models here.
class Moviedata(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rating = models.FloatField()
    genre = models.CharField(max_length=200, default='action')
    images = models.ImageField(upload_to='Images/', default='Images/None/Noimg.jpg')
    
    def __str__(self):
        return self.name