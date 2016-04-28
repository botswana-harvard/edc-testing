from edc_visit_schedule.classes import RequisitionPanelTuple, CrfTuple
from edc_constants.constants import REQUIRED, NOT_ADDITIONAL


crf_entries = (
    CrfTuple(10, u'edc_testing', u'TestScheduledModel1', REQUIRED, NOT_ADDITIONAL),
    CrfTuple(20, u'edc_testing', u'TestScheduledModel2', REQUIRED, NOT_ADDITIONAL),
    CrfTuple(30, u'edc_testing', u'TestScheduledModel3', REQUIRED, NOT_ADDITIONAL),
)


requisition_entries = (
    RequisitionPanelTuple(
        10, u'edc_testing', u'testrequisition', 'Research Blood Draw', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        20, u'edc_testing', u'testrequisition', 'Viral Load', 'TEST', 'WB', REQUIRED, NOT_ADDITIONAL),
    RequisitionPanelTuple(
        30, u'edc_testing', u'testrequisition', 'Microtube', 'STORAGE', 'WB', REQUIRED, NOT_ADDITIONAL)
)
