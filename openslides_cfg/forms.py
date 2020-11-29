from django.db.models.fields import EmailField
from django.forms import ModelForm, CharField, ChoiceField
from openslides_cfg.models import OpenSlidesInstance
import logging
class OpenSlidesForm(ModelForm):
    name_text = CharField(label="OpenSlides Domain Prefix", help_text='Bestimmt wie die Addresse vom openslides lautet: https://&lt;prefix&gt;.slides.adfc-intern.de/')
    meet_room = CharField(label="Welcher Jitsi-Meet Raum soll mit Openslides verbunden werden", help_text='Wenn die Meet-URL https://meet.adfc-intern.de/Hamburg lautet, muss hier: Hamburg hin')
    install_status = ChoiceField(disabled=True, choices=OpenSlidesInstance.INSTALL_STATUSES)
    def save(self, commit=True):
        if (self.instance.install_status!='0'):
          self.instance.install_status='2'
        return super().save(commit)
    class Meta:
        model = OpenSlidesInstance
        exclude = ()
#        fields = (
#            'id',
#            'name_text',
#            'meet_room',
#            'meet_password',
##            'created_by',
##            'created_at',
##            'modified_by',
##            'modified_at',
#            'reset_password_verbose',
#            'email_server',
#            'email_server_port',
#            'email_username',
#            'email_password',
#            'enable_electronic_voting',
