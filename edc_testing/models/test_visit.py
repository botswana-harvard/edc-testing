from edc_meta_data.models import CrfMetaDataMixin
from edc_visit_tracking.models import VisitModelMixin, PreviousVisitMixin


class TestVisit(CrfMetaDataMixin, PreviousVisitMixin, VisitModelMixin):

    REQUIRES_PREVIOUS_VISIT = True

    def custom_post_update_crf_meta_data(self):
        pass

    def get_requires_consent(self):
        return False

    class Meta:
        app_label = 'edc_testing'


class TestVisit2(CrfMetaDataMixin, PreviousVisitMixin, VisitModelMixin):

    REQUIRES_PREVIOUS_VISIT = True

    def custom_post_update_crf_meta_data(self):
        pass

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
