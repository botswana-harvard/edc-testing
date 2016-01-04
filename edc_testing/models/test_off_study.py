from django.db import models

from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_meta_data.managers.crf_meta_data_manager import CrfMetaDataManager
from edc_offstudy.models import OffStudyModelMixin
from edc_visit_tracking.models import CrfModelMixin

from .test_visit import TestVisit


class TestOffStudy(CrfModelMixin, OffStudyModelMixin, BaseUuidModel):

    test_visit_model = models.OneToOneField(TestVisit)

    entry_meta_data_manager = CrfMetaDataManager(TestVisit)

    class Meta:
        app_label = 'edc_testing'
