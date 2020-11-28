from django.db import models

# Create your models here.

class OpenSlidesInstance(models.Model):
    name_text = models.CharField(max_length=16)
    pub_date = models.DateTimeField('date published')
    admin_name = models.CharField(max_length=20)
    admin_email = models.CharField(max_length=200)
    meet_room = models.CharField(max_length=20)
