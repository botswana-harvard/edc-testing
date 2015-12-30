import factory

from django.utils import timezone

from edc_constants.choices import IDENTITY_TYPE
from edc_constants.constants import YES, NO

from ...models import TestConsent, TestConsentWithMixin


class BaseConsentBasicsFactory(factory.DjangoModelFactory):
    class Meta:
        abstract = True

    consent_reviewed = YES
    study_questions = YES
    assessment_score = YES
    consent_copy = YES


class BaseConsentFactory(BaseConsentBasicsFactory):
    class Meta:
        abstract = True

    study_site = '40'
    consent_datetime = timezone.now()
    may_store_samples = YES
    is_incarcerated = NO


class BaseTestConsentFactory(BaseConsentFactory):
    class Meta:
        abstract = True

    user_provided_subject_identifier = None
    identity = factory.Sequence(lambda n: '{0}2{1}'.format(str(n).rjust(4, '0'), str(n).rjust(4, '0')))
    identity_type = factory.Iterator(IDENTITY_TYPE, getter=lambda c: c[0])
    confirm_identity = factory.Sequence(lambda n: '{0}2{1}'.format(str(n).rjust(4, '0'), str(n).rjust(4, '0')))
    first_name = factory.Sequence(lambda n: 'ERIK{0}'.format(n))
    initials = factory.Sequence(lambda n: 'E{0}W'.format(n))


class TestConsentFactory(BaseConsentFactory):
    class Meta:
        model = TestConsent


class TestConsentWithMixinFactory(BaseConsentFactory):

    is_literate = YES

    class Meta:
        model = TestConsentWithMixin
