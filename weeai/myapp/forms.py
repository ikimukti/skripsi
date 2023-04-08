from django import forms

class ImageUploadForm(forms.Form):
    image = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes',
        widget=forms.ClearableFileInput(attrs={'multiple': True}),
    )
    uploader = forms.CharField(
        max_length=100,
        label='Uploader',
        help_text='Who upload this image?',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Uploader'
                }
            ),

        )