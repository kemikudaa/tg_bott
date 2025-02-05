from django.db import models

class Cat(models.Model):
    image = models.ImageField(upload_to='cats/')
    message = models.CharField(max_length=255)

    def __str__(self):
        return self.message
