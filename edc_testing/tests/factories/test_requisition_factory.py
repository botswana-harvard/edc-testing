import factory


from ...models import TestRequisition

from edc_visit_tracking.tests.factories import TestVisitFactory


class TestRequisitionFactory(factory.DjangoModelFactory):

    class Meta:
        model = TestRequisition

    test_visit = factory.SubFactory(TestVisitFactory)
