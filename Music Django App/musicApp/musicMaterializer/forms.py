from django import forms

from .models import FileModel

class FileForm(forms.ModelForm):
    # detect_bpm = forms.BooleanField()
    # record = forms.BooleanField()
    
    class Meta:
        model = FileModel
        fields = ('title', 'file', 'apikey', 'detect_bpm', 'record') 

