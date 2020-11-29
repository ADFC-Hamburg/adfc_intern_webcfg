
from django_tables2 import Table, Column, TemplateColumn
from django.utils.html import format_html
from django.utils.timezone import datetime
from django_tables2 import columns

from openslides_cfg.models import OpenSlidesInstance

class OpenSlidesInstanceTable(Table):
    id = Column(visible=False)
    created_by = Column(visible=False)
    created_at = Column(visible=False)
    updated_by = Column(visible=False)
    #created_at = Column(visible=False)
    aktionen = TemplateColumn(
                                template_name='my_col.html',
                                orderable=False) # orderable not sortable
    def render_name_text(self, record, value):
        url = OpenSlidesInstance.objects.get(pk=record.id).get_openslides_url()
        html = format_html('<a href="{}">meet.adfc-intern.de/<b>{}</b></a>', url, value.lower())
        return html
    def render_meet_room(self, record, value):
        url = OpenSlidesInstance.objects.get(pk=record.id).get_meet_url()
        html = format_html('<a href="{}"><b>{}</b>.adfc-intern.de</a>', url, value.lower())
        return html

    class Meta:
        model = OpenSlidesInstance
        per_page = 20
        order_by = ('id',)
        attrs = {"class": "table table-striped",
                 "thead": {
                     "class": "thead-light"
                    }
                 }
        fields= ( 'name_text', 'meet_room', 'install_status', 'aktionen')