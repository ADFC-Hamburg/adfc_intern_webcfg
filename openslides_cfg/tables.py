
from django_tables2 import Table, Column
from django.utils.html import format_html
from django.utils.timezone import datetime

from openslides_cfg.models import OpenSlidesInstance

class OpenSlidesInstanceTable(Table):
    id = Column(visible=False)
    created_by = Column(visible=False)
    created_at = Column(visible=False)
    updated_by = Column(visible=False)
    #created_at = Column(visible=False)

    def render_name_text(self, record, value):
        url = OpenSlidesInstance.objects.get(pk=record.id).get_absolute_url()
        html = format_html('<a href="{}">{}</a>', url, value)
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
