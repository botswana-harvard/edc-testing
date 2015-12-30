from django.db import models

from edc_offstudy.models import OffStudyMixin

from ..managers import TestRegistrationManager


class TestRegistration(OffStudyMixin, models.Model):

    off_study_model = None

    objects = TestRegistrationManager()

    class Meta:
        app_label = 'edc_testing'
