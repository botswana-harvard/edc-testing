from datetime import datetime, date

from django.db import models

from edc_base.model.models import BaseUuidModel
from edc_constants.choices import YES_NO

from edc.export.managers import ExportHistoryManager


class ExportTest(BaseUuidModel):

    f_char = models.CharField(
        max_length=64,
        default='character')

    f_choice = models.CharField(
        max_length=64,
        choices=YES_NO,
        default='Yes')

    f_integer = models.IntegerField(default=123)

    f_date = models.DateField(default=date.today())

    f_datetime = models.DateField(default=datetime.today())

    f_text = models.TextField(default='Space, the final frontier. These are the voyages of the starship enterprise')

    export_history = ExportHistoryManager()

    objects = models.Manager()

    def is_serialized(self):
        return False

    class Meta:
        app_label = 'edc_testing'
