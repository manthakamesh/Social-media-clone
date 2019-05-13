from django import forms
from groups.models import Group
class sampleform(forms.ModelForm):
    class Meta():
        model=Group
        fields=('name','description')
