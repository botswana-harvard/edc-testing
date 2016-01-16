import factory

from django.utils import timezone

from edc_visit_tracking.tests.factories import TestVisitFactory

from ...models import TestRequisition


class TestRequisitionFactory(factory.DjangoModelFactory):

    requisition_datetime = timezone.now()

    class Meta:
        model = TestRequisition

    test_visit = factory.SubFactory(TestVisitFactory)
