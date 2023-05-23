from django import forms
from django.utils.safestring import mark_safe

class VisibleMultipleHiddenInput(forms.widgets.HiddenInput):
    def render(self, name, value, attrs=None, renderer=None):
        if not attrs:
            attrs = {}
        attrs['type'] = 'hidden'  # Change the input type to 'hidden'
        return mark_safe(super().render(name, value, attrs, renderer))

class ImageUploadForm(forms.Form):
    # css class for bootstrap 4
    image = forms.ImageField(
        label='Select a file',
        help_text='max. 42 megabytes',
        widget=VisibleMultipleHiddenInput(
            attrs={
                'multiple': True,
                'class': 'block w-full text-sm text-slate-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100 cursor-pointer',
                'id': 'image-field',
                'accept': 'image/*',
                'onchange': 'previewImage()',
                'type': 'file'
            },
        ),
        allow_empty_file=False,
        required=True,
        error_messages={'required': 'Please select an image file.'},
        disabled=False
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
        required=True,
        error_messages={'required': 'Please input your name.'},
        empty_value='Anonymous'
    )
    # nameImage
    nameImage = forms.CharField(
        max_length=100,
        label='Image Name',
        help_text='What is the name of this image?',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Input image name',
                'class': 'block w-full text-sm text-slate-500 rounded-md file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100',
                'id': 'nameImage'
                }
            ),
        required=True,
        error_messages={'required': 'Please input image name.'},
        empty_value='Anonymous'
    )
    # contrastEnhancement slider number select from 0.1 to 1.0
    scaleRatio = forms.FloatField(
        label='Scale Ratio',
        help_text='Scale ratio for image enhancement',
        widget=forms.NumberInput(
            attrs={
                'type': 'range',
                'min': '0.1',
                'max': '1.0',
                'step': '0.1',
                'value': '1.0',
                'class': 'block w-full text-sm text-slate-500 rounded-md file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100',
                'id': 'scaleRatio'
                }
            ),
        required=True,
        error_messages={'required': 'Please input contrast enhancement.'},
    )
    # contrastEnhancement slider number select from 0.1 to 1.0
    contrastEnhancement = forms.FloatField(
        label='Contrast Enhancement',
        help_text='Contrast enhancement for image enhancement',
        widget=forms.NumberInput(
            attrs={
                'type': 'range',
                'min': '0.1',
                'max': '1.0',
                'step': '0.1',
                'value': '1.0',
                'class': 'block w-full text-sm text-slate-500 rounded-md file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100',
                'id': 'contrastEnhancement'
                }
            ),
        required=True,
        error_messages={'required': 'Please input contrast enhancement.'},
    )
    # noiseReduction checkbox
    noiseReduction = forms.BooleanField(
        label='noiseReduction',
        help_text='noiseReduction for image enhancement',
        widget=forms.CheckboxInput(
            attrs={
                'type': 'checkbox',
                'class': 'block text-sm text-slate-500 rounded-md file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100',
                'id': 'noiseReduction'
                }
            ),
        required=False,
        error_messages={'required': 'Please input noiseReduction.'},
    )
    # backgroundDominantColor
    backgroundDominantColor = forms.CharField(
        max_length=100,
        label='Background Dominant Color',
        help_text='What is the background dominant color of this image?',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Input background dominant color',
                'class': 'block w-full text-sm text-slate-500 rounded-md file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100',
                'id': 'backgroundDominantColor'
                }
            ),
        required=True,
        error_messages={'required': 'Please input background dominant color.'},
        empty_value='White'
    )
    
    
    # distanceObject enter in cm
    distanceObject = forms.FloatField(
        label='Distance Object',
        help_text='Distance object in cm',
        widget=forms.NumberInput(
            attrs={
                'type': 'number',
                'min': '0',
                'max': '100',
                'step': '1',
                'value': '0',
                'class': 'block w-full text-sm text-slate-500 rounded-md file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-violet-50 file:text-violet-700 hover:file:bg-violet-100',
                'id': 'distanceObject'
                }
            ),
        required=True,
        error_messages={'required': 'Please input distance object.'},
    )
    
    