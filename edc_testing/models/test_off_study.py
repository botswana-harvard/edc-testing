from django.db import models

from edc_base.model.models.base_uuid_model import BaseUuidModel
from edc_meta_data.managers import CrfMetaDataManager
from edc_offstudy.models import OffStudyModelMixin
from edc_visit_tracking.models import CrfModelMixin

from .test_visit import TestVisit


class TestOffStudy(CrfModelMixin, OffStudyModelMixin, BaseUuidModel):

    visit_model_attr = 'test_visit_model'

    test_visit_model = models.OneToOneField(TestVisit)

    entry_meta_data_manager = CrfMetaDataManager(TestVisit, visit_attr_name='test_visit_model')

    class Meta:
        app_label = 'edc_testing'
