from django.db import models

from edc_base.model.models.base_uuid_model import BaseUuidModel

from edc_locator.models import LocatorMixin

from .test_visit import TestVisit


class TestSubjectLocator(LocatorMixin, BaseUuidModel):

    test_visit = models.OneToOneField(TestVisit)

    def get_subject_identifier(self):
        return self.test_visit.get_subject_identifier()

    class Meta:
        app_label = 'edc_testing'
