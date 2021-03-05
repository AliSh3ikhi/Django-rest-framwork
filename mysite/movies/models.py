from django.db import models

# Create your models here.



class MovieData(models.Model):
    name = models.CharField(max_length=200)
    duration = models.FloatField()
    rate = models.FloatField()
    mode = models.CharField(max_length=200,default='action')
    image = models.ImageField(upload_to='Images/',default='Images/None/none.jpg')

    def __str__(self):
        return self.name
