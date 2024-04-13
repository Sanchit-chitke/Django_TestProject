from django import forms
from .models import FirstModel, SecondModel, ThirdModel

class FirstModelForm(forms.ModelForm):
    class Meta:
        model = FirstModel
        fields = ['first_field']

class SecondModelForm(forms.ModelForm):
    first_model = forms.ModelChoiceField(queryset=FirstModel.objects.all())

    class Meta:
        model = SecondModel
        fields = ['second_field']


class ThirdModelForm(forms.ModelForm):
    second_model = forms.ModelChoiceField(queryset=SecondModel.objects.all())

    class Meta:
        model = ThirdModel
        fields = ['third_field']
