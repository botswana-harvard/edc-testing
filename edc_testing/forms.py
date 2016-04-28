from django import forms

from .models import TestModel, TestSubjectUuidModel, TestScheduledModel


class TestSubjectUuidModelForm (forms.ModelForm):

    class Meta:
        model = TestSubjectUuidModel
        fields = "__all__"


class TestModelForm (forms.ModelForm):

    class Meta:
        model = TestModel
        fields = "__all__"


class TestScheduledModelForm(forms.ModelForm):
    class Meta:
        model = TestScheduledModel
        fields = "__all__"
