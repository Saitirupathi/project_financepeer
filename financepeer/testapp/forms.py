from django import forms
from testapp.models import Upload


class UploadForm(forms.ModelForm):
    class Meta:
        model=Upload
        fields=('file',)
