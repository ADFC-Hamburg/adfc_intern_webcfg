from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse
from django_userforeignkey.models.fields import UserForeignKey

class OpenSlidesInstance(models.Model):
    name_text = models.CharField(max_length=16, verbose_name="OpenSlides Name")
    meet_room = models.CharField(max_length=20)
    created_by = UserForeignKey(auto_user_add=True, verbose_name="Created by", related_name="mymodels")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created on")
    updated_by = UserForeignKey(auto_user=True, verbose_name="Updated by", related_name="mymodels2")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last update on")
    def __str__(self):
        return self.name_text + '.slides.adfc-intern.de -> meet.adfc-intern.de/'+self.meet_room
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk })
