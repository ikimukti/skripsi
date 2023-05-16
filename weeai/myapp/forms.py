from django import forms

class ImageUploadForm(forms.Form):
    # css class for bootstrap 4
    image = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes',
        widget=forms.ClearableFileInput(
            attrs={
                'multiple': True,
                'class': 'block w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100 cursor-pointer',
                'id': 'image-field',
                'accept': 'image/*',
                'onchange': 'previewImage()'
            }
        ),

    )
    uploader = forms.CharField(
        max_length=100,
        label='Uploader',
        help_text='Who upload this image?',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Input your name',
                'class': 'block w-full text-sm text-slate-500 rounded-md file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100',
                'id': 'uploader'
                }
            ),
    )