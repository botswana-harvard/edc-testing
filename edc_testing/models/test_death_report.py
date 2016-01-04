from django.db import models
from django.utils import timezone

from edc_meta_data.managers import CrfMetaDataManager

from .test_visit import TestVisit


class TestDeathReport(models.Model):

    test_visit = models.OneToOneField(TestVisit)

    report_datetime = models.DateTimeField(
        verbose_name="Report Date",
        default=timezone.now)

    entry_meta_data_manager = CrfMetaDataManager(TestVisit)

    class Meta:
        app_label = "edc_testing"
