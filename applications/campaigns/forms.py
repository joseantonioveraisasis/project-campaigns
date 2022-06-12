from datetime import datetime
from xml.dom.minidom import Attr
from django import forms
from .models import DwCampanias


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class UploadFileForm(forms.Form):
    file = forms.FileField()

class CreateForm(forms.ModelForm):

    class Meta:
        model = DwCampanias

        fields = (
            'nombre_campania',
            'vigencia_desde',
            'vigencia_hasta',
            'id_clasificacion',
            'tracking_id',
            'fecha_creacion',
            
        )

        widgets = {
            'nombre_campania': forms.TextInput(
                attrs= {
                    'placeholder': '',
                    'class': 'form-control',
                    'required': ''
                }
            ),
            'vigencia_desde': forms.DateInput(
                attrs= {
                    'type': 'date',
                    'class': 'form-control',
                    'required': ''
                }
            ),
            'vigencia_hasta': forms.DateInput(
                attrs= {
                    'type': 'date',
                    'class': 'form-control',
                    'required': ''
                }
            ),
            'id_clasificacion': forms.Select(
                attrs= {
                    'class': 'form-select',
                    'required': ''
                }
            ),
            'tracking_id': forms.Select(
                attrs= {
                    'class': 'form-select',
                }
            ),
            'fecha_creacion': forms.DateInput(
                attrs= {
                    'type': 'hidden',
                    'value': datetime.now().strftime("%Y-%m-%d"),
                    'class': 'form-select',
                }
            ),

        }