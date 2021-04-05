from django import forms
from .models import Logs

class LogsForm(forms.ModelForm):
    exercise = forms.CharField(max_length=200)#, help_text="title.")
    date = forms.CharField(max_length=200)#, help_text="text.")      #could be slider, buttons, etc
    duration = forms.CharField(max_length=200)#, help_text="text.")      #could be slider, buttons, etc.        ##also includes reps.
    intensity = forms.CharField(max_length=200)#, help_text="text.")     #could be slider, buttons, etc
    area = forms.CharField(max_length=200)#, help_text="text.")     #could be slider, buttons, etc
    ## can include other relevant info we want to encourage
    class Meta:
        model = Logs
        fields = ('exercise', 'date', 'duration', 'intensity', 'area')