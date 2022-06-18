from datetime import datetime
from xml.dom.minidom import Attr
from django import forms
from .models import DwCampanias


class FileFieldForm(forms.Form):
    file_field = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))

class UploadFileForm(forms.Form):
    file = forms.FileField(
        
        widget=forms.ClearableFileInput(
            attrs={
                'id': 'file',
                'name': 'file',
                'type': 'file',
                'enctype': 'multipart/form-data',
                'accept': '.csv, text/csv',
                'required': '',
                'class': 'form-control'
            }
        )
    )

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
                format='%Y-%m-%d',
                attrs= {
                    'type': 'date',
                    'value': datetime.now().strftime("%Y-%m-%d"),
                    'class': 'form-control',
                    'required': ''
                }
            ),
            'vigencia_hasta': forms.DateInput(
                format='%Y-%m-%d',
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
                format='%Y-%m-%d',
                attrs= {
                    'type': 'hidden',
                    'value': datetime.now().strftime("%Y-%m-%d"),
                    'class': 'form-select',
                }
            ),

        }
    #validations
    ''' def clean_control_group(self):
        cg = self.changed_data['x']
        if not cg > -1:
            raise forms.ValidationError('Ingrese numero mayor a -1') '''