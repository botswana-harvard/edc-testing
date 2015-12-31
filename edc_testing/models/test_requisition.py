from django.db import models

from edc_base.audit_trail import AuditTrail
from edc_lab.lab_requisition.models import RequisitionModelMixin
from edc.entry_meta_data.managers import RequisitionMetaDataManager

from .test_visit import TestVisit
from .test_panel import TestPanel
from .test_aliquot_type import TestAliquotType
from edc_visit_tracking.models.crf_model_mixin import CrfModelMixin


class TestRequisition(CrfModelMixin, RequisitionModelMixin):

    test_visit = models.ForeignKey(TestVisit)

    panel = models.ForeignKey(TestPanel)

    aliquot_type = models.ForeignKey(TestAliquotType)

    history = AuditTrail()

    entry_meta_data_manager = RequisitionMetaDataManager(TestVisit)

    class Meta:
        app_label = 'edc_testing'
