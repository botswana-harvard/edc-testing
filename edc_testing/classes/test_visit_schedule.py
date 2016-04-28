from collections import OrderedDict

from edc_visit_schedule.classes import (
    VisitScheduleConfiguration, MembershipFormTuple, ScheduleTuple)

from ..models import TestVisit, TestVisit2, TestConsentWithMixin, TestAliquotType, TestPanel
from edc_testing.classes.entries import requisition_entries, crf_entries


class TestVisitSchedule(VisitScheduleConfiguration):
    """A visit schedule class for tests."""
    name = 'Test Visit Schedule'
    app_label = 'edc_testing'
    panel_model = TestPanel
    aliquot_type_model = TestAliquotType

    membership_forms = OrderedDict({
        'schedule-1': MembershipFormTuple('schedule-1', TestConsentWithMixin, True),
    })

    schedules = OrderedDict({
        'schedule-1': ScheduleTuple('schedule-1', 'schedule-1', None, None),
    })

    visit_definitions = OrderedDict(
        {'1000': {
            'title': '1000',
            'time_point': 0,
            'base_interval': 0,
            'base_interval_unit': 'D',
            'window_lower_bound': 0,
            'window_lower_bound_unit': 'D',
            'window_upper_bound': 0,
            'window_upper_bound_unit': 'D',
            'grouping': 'group1',
            'visit_tracking_model': TestVisit,
            'schedule': 'schedule-1',
            'instructions': None,
            'requisitions': requisition_entries,
            'entries': crf_entries},
         '2000': {
             'title': '2000',
             'time_point': 1,
             'base_interval': 0,
             'base_interval_unit': 'D',
             'window_lower_bound': 0,
             'window_lower_bound_unit': 'D',
             'window_upper_bound': 0,
             'window_upper_bound_unit': 'D',
             'grouping': 'group1',
             'visit_tracking_model': TestVisit,
             'schedule': 'schedule-1',
             'instructions': None,
             'requisitions': requisition_entries,
             'entries': crf_entries},
         '2000A': {
             'title': '2000A',
             'time_point': 0,
             'base_interval': 0,
             'base_interval_unit': 'D',
             'window_lower_bound': 0,
             'window_lower_bound_unit': 'D',
             'window_upper_bound': 0,
             'window_upper_bound_unit': 'D',
             'grouping': 'group2',
             'visit_tracking_model': TestVisit2,
             'schedule': 'schedule-1',
             'instructions': None,
             'requisitions': requisition_entries,
             'entries': crf_entries},
         '2010A': {
             'title': '2010A',
             'time_point': 1,
             'base_interval': 0,
             'base_interval_unit': 'D',
             'window_lower_bound': 0,
             'window_lower_bound_unit': 'D',
             'window_upper_bound': 0,
             'window_upper_bound_unit': 'D',
             'grouping': 'group2',
             'visit_tracking_model': TestVisit2,
             'schedule': 'schedule-1',
             'instructions': None,
             'requisitions': requisition_entries,
             'entries': crf_entries},
         '2020A': {
             'title': '2020A',
             'time_point': 2,
             'base_interval': 0,
             'base_interval_unit': 'D',
             'window_lower_bound': 0,
             'window_lower_bound_unit': 'D',
             'window_upper_bound': 0,
             'window_upper_bound_unit': 'D',
             'grouping': 'group2',
             'visit_tracking_model': TestVisit2,
             'schedule': 'schedule-1',
             'instructions': None,
             'requisitions': requisition_entries,
             'entries': crf_entries},
         '2030A': {
             'title': '2030A',
             'time_point': 3,
             'base_interval': 0,
             'base_interval_unit': 'D',
             'window_lower_bound': 0,
             'window_lower_bound_unit': 'D',
             'window_upper_bound': 0,
             'window_upper_bound_unit': 'D',
             'grouping': 'group2',
             'visit_tracking_model': TestVisit2,
             'schedule': 'schedule-1',
             'instructions': None,
             'requisitions': requisition_entries,
             'entries': crf_entries},
         },
    )
