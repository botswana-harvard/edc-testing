from django.db import models

from edc_meta_data.managers import CrfMetaDataManager

from edc_base.model.models import BaseUuidModel
from edc_visit_tracking.models import CrfModelMixin

from .test_visit import TestVisit


class TestDeathReport(CrfModelMixin, BaseUuidModel):

    test_visit = models.OneToOneField(TestVisit)

    entry_meta_data_manager = CrfMetaDataManager(TestVisit)

    class Meta:
        app_label = "edc_testing"
