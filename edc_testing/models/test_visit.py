from edc_base.model.models import BaseUuidModel
from edc_meta_data.models import CrfMetaDataMixin
from edc_offstudy.models import OffStudyMixin
from edc_visit_tracking.models import VisitModelMixin, PreviousVisitMixin


class TestVisit(OffStudyMixin, CrfMetaDataMixin, PreviousVisitMixin, VisitModelMixin, BaseUuidModel):

    off_study_model = ('edc_testing', 'TestOffStudy')

    death_report_model = ('edc_testing', 'TestDeathReport')

    REQUIRES_PREVIOUS_VISIT = True

    def get_requires_consent(self):
        return False

    class Meta:
        app_label = 'edc_testing'


class TestVisit2(CrfMetaDataMixin, OffStudyMixin, PreviousVisitMixin, VisitModelMixin):

    REQUIRES_PREVIOUS_VISIT = True

    off_study_model = ('edc_testing', 'TestOffStudy')

    death_report_model = ('edc_testing', 'TestDeathReport')

    def get_requires_consent(self):
        return False

    class Meta:
        app_label = 'edc_testing'


class TestSubjectVisit(VisitModelMixin):

    def get_requires_consent(self):
        return False

    class Meta:
        app_label = 'edc_testing'


class TestSubjectVisitTwo(VisitModelMixin):

    def get_requires_consent(self):
        return False

    class Meta:
        app_label = 'edc_testing'


class TestSubjectVisitThree(VisitModelMixin):

    def get_requires_consent(self):
        return False

    class Meta:
        app_label = 'edc_testing'
