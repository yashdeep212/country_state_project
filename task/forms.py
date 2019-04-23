from django import forms
from .models import Person, State, City
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ('name', 'birthdate', 'country', 'state','city')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['state'].queryset = State.objects.none()
    #     self.fields['city'].queryset = City.objects.none()