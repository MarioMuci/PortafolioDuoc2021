from django.forms import *
from .models import ArticuloDepartamento, ImagenDepartamento, Departamento, Funcionario, Cargo, DetalleCostoDepartamento

class ArticuloDepartamentoForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['art_dep_nombre'].widget.attrs['autofocus'] = True

	class Meta:
		model = ArticuloDepartamento
		fields = '__all__'
		widgets = {
			'art_dep_nombre': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese el nombre del articulo'
				}
			),
			'art_dep_estado': CheckboxInput(
				attrs={
					'class': 'form-check-input',
					'type': 'checkbox'
				}
			),
			'art_dep_precio': NumberInput(
				attrs={
					'class': 'form-control'
				}
			),
			'f_cat_art': Select(
				attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
			),
			'res_fecha_hasta': DateInput(
				attrs={
					'class': 'form-control',
					'type': 'date'
				}
			),		
		}
		exclude = ['user_updated', 'user_creation']

	def save(self, commit=True):
		data = {}
		form = super()
		try:
			if form.is_valid():
				form.save()
			else:
				data['error'] = form.errors
		except Exception as e:
			data['error'] = str(e)
		return data

	#def clean(self):
		#cleaned = super().clean()
		#if len(cleaned['art_dep_nombre']) == NumberInput:
			#self.add_error('art_dep_nombre', 'Faltan caracteres')
		#return cleaned

class DepartamentoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['dep_nombre'].widget.attrs['autofocus'] = True

    class Meta:
        model = Departamento
        fields = '__all__'
        widgets = {
        	'dep_nombre': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese el nombre del departamento'
				}
			),
			'dep_ubicacion': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese la ubicación del departamento'
				}
			),
			'dep_capacidad': NumberInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese la capacidad del departamento'
				}
			),
            'dep_acondicionado': CheckboxInput(
				attrs={
					'class': 'form-check-input',
					'type': 'checkbox'
				}
			),
			'dep_canon_renta': NumberInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese la renta del departamento'
				}
			),
			'dep_ocupacion': NumberInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese el stock'
				}
			),
			'dep_estado': CheckboxInput(
				attrs={
					'class': 'form-check-input',
					'type': 'checkbox'
				}
			),
			'dep_costo_mes': NumberInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese el costo mensual del departamento'
				}
			),
			'f_zona': Select(
            	attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
            'dep_tipologia': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese la tipologia del departamento'
				}
			),
			'dep_piso': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese la cantidad de pisos del departamento'
				}
			),
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
    	data = {}
    	form = super()
    	try:
    		if form.is_valid():
    			form.save()
    		else:
    			data['error'] = form.errors
    	except Exception as e:
    		data['error'] = str(e)
    	return data

class ImagenDepartamentoForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
	
	class Meta:
		model = ImagenDepartamento
		fields = '__all__'

class FuncionarioForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fun_rut'].widget.attrs['autofocus'] = True

    class Meta:
        model = Funcionario
        fields = '__all__'
        widgets = {
            'fun_rut': TextInput(
                attrs={
                    'placeholder': 'Ingrese el rut',
                }
            ),
            'fun_nombre': TextInput(
                attrs={
                    'placeholder': 'Ingrese el nombre',
                }
            ),
            'fun_apellido_paterno': TextInput(
                attrs={
                    'placeholder': 'Ingrese su apellido paterno',
                }
            ),
            'fun_apellido_materno': TextInput(
                attrs={
                    'placeholder': 'Ingrese su apellido materno',
                }
            ),
            'f_car': Select(
            	attrs={
                    'class': 'form-control'
                }
            ),
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                instance = form.save()
                data = instance.toJSON()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

class DetalleCostoDepartamentoForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = DetalleCostoDepartamento
        fields = '__all__'
        widgets = {
        	'des_cos_dep_dia': NumberInput(
				attrs={
					'class': 'form-control',
					'readonly': True
				}
			),
			'des_cos_dep_semanal': NumberInput(
				attrs={
					'class': 'form-control',
					'readonly': True
				}
			),
			'pf_fun': Select(
            	attrs={
                    'class': 'form-select select2'
                }
            ),
        }
