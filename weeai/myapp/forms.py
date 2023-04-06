from django import forms

class ImageUploadForm(forms.Form):
    title = forms.CharField(max_length=100)
    file = forms.FileField()
    uploader = forms.CharField(max_length=100)