from django.forms import ModelForm, DateField, CharField
from openslides_cfg.models import OpenSlidesInstance

class OpenSlidesForm(ModelForm):
    name_text = CharField(label="OpenSlides Domain Prefix", help_text='Bestimmt wie die Addresse vom openslides lautet: https://&lt;prefix&gt;.slides.adfc-intern.de/')
    meet_room = CharField(label="Welcher Jitsi-Meet Raum soll mit Openslides verbunden werden", help_text='Wenn die Meet-URL https://meet.adfc-intern.de/Hamburg lautet, muss hier: Hamburg hin')
    class Meta:
        model = OpenSlidesInstance
        fields = (
            'id',
            'name_text',
            'meet_room',
        )
