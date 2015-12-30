from datetime import datetime

from django.db import models

from edc.entry_meta_data.managers import EntryMetaDataManager
from edc.export.managers import ExportHistoryManager
from edc.export.models import ExportTrackingFieldsMixin
from edc_base.model.models import BaseUuidModel
from edc_constants.choices import YES_NO

from .test_visit import TestVisit


class TestScheduledModel(ExportTrackingFieldsMixin, BaseUuidModel):

    test_visit = models.OneToOneField(TestVisit)

    report_datetime = models.DateTimeField(default=datetime.today())

    f1 = models.CharField(max_length=10, null=True)

    f2 = models.CharField(max_length=10, null=True)

    f3 = models.CharField(max_length=10, null=True)

    f4 = models.CharField(max_length=10, choices=YES_NO, null=True)

    objects = models.Manager()

    export_history = ExportHistoryManager()

    def get_subject_identifier(self):
        return self.test_visit.get_subject_identifier()

    class Meta:
        app_label = 'edc_testing'


class TestScheduledModel1(ExportTrackingFieldsMixin, BaseUuidModel):

    test_visit = models.OneToOneField(TestVisit)

    report_datetime = models.DateTimeField(default=datetime.today())

    f1 = models.CharField(max_length=10, null=True)

    f2 = models.CharField(max_length=10, null=True)

    f3 = models.CharField(max_length=10, null=True)

    f4 = models.CharField(max_length=10, null=True)

    objects = models.Manager()

    export_history = ExportHistoryManager()

    entry_meta_data_manager = EntryMetaDataManager(TestVisit)

    def get_subject_identifier(self):
        return self.test_visit.get_subject_identifier()

    class Meta:
        app_label = 'edc_testing'


class TestScheduledModel2(ExportTrackingFieldsMixin, BaseUuidModel):

    test_visit = models.OneToOneField(TestVisit)

    report_datetime = models.DateTimeField(default=datetime.today())

    f1 = models.CharField(max_length=10, null=True)

    f2 = models.CharField(max_length=10, null=True)

    f3 = models.CharField(max_length=10, null=True)

    f4 = models.CharField(max_length=10, null=True)

    objects = models.Manager()

    export_history = ExportHistoryManager()

    entry_meta_data_manager = EntryMetaDataManager(TestVisit)

    def get_subject_identifier(self):
        return self.test_visit.get_subject_identifier()

    class Meta:
        app_label = 'edc_testing'


class TestScheduledModel3(ExportTrackingFieldsMixin, BaseUuidModel):

    test_visit = models.OneToOneField(TestVisit)

    report_datetime = models.DateTimeField(default=datetime.today())

    f1 = models.CharField(max_length=10, null=True)

    f2 = models.CharField(max_length=10, null=True)

    f3 = models.CharField(max_length=10, null=True)

    f4 = models.CharField(max_length=10, null=True)

    objects = models.Manager()

    export_history = ExportHistoryManager()

    entry_meta_data_manager = EntryMetaDataManager(TestVisit)

    def get_subject_identifier(self):
        return self.test_visit.get_subject_identifier()

    class Meta:
        app_label = 'edc_testing'
