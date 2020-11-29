from django.db import models
from django.contrib.auth.models import User
# Create your models here.
from django.urls import reverse
from django_userforeignkey.models.fields import UserForeignKey

class OpenSlidesInstance(models.Model):
    INSTALL_STATUSES= (
        ('0', 'warte auf Installation'),
        ('1', 'installiert'),
        ('2', 'Änderungen ausstehend'),
    )
    name_text = models.CharField(max_length=30, verbose_name="OpenSlides Name")
    meet_room = models.CharField(max_length=30, verbose_name="Jitsi Meet Raumname")
    meet_password = models.CharField(max_length=40,verbose_name="Jitsi Meet Raumpasswort (sofern vergeben)",blank=True)
    enable_electronic_voting = models.BooleanField(default=True, verbose_name="Elektronische Wahlen erlauben")
    reset_password_verbose = models.BooleanField(default=True, verbose_name="Aussagekrägtige Fehlermeldung beim Passwort zurücksetzen")
    created_by = UserForeignKey(auto_user_add=True, verbose_name="Created by", related_name="mymodels")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created on")
    updated_by = UserForeignKey(auto_user=True, verbose_name="Updated by", related_name="mymodels2")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Last update on")
    email_server = models.CharField(max_length=255, verbose_name="E-Mail Server")
    email_server_port = models.IntegerField(default=587, verbose_name='E-Mail Server-Portnummer')
    email_username = models.CharField(max_length=255, verbose_name='E-Mail Server Benutzername')
    email_password = models.CharField(max_length=255, verbose_name='E-Mail Server Passwort')
    email_default_from = models.EmailField(verbose_name='E-Mail default Absender')
    admin_email = models.EmailField(verbose_name='E-Mail Addresse des OpenSlides Administrators (admin)')
    install_status = models.CharField(verbose_name='Status', default="0", choices=INSTALL_STATUSES, max_length=1)

    def __str__(self):
        return self.name_text + '.slides.adfc-intern.de -> meet.adfc-intern.de/'+self.meet_room
    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk })
    def get_meet_url(self):
        return 'https://meet.adfc-intern.de/'+ self.meet_room.lower()
    def get_openslides_url(self):
        return 'https://'+self.name_text.lower()+'.adfc-intern.de/'
