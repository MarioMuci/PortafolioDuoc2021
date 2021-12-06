from django.forms import *
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django import forms

class UserForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['rut'].widget.attrs['autofocus'] = True

	class Meta:
		model = User
		fields = 'rut', 'first_name', 'apellido_paterno', 'apellido_materno', 'direccion', 'numero_contacto', 'username', 'email', 'password', 'groups'
		widgets = {
			'rut': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su rut sin puntos y con guión',
					'minlength': 9
				}
			),
			'first_name': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese sus nombres'
				}
			),
			'apellido_paterno': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su apellido paterno'
				}
			),
			'apellido_materno': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su apellido materno'
				}
			),
			'username': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su nombre de usuario'
				}
			),
			'email': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su correo electronico'
				}
			),
			'password': PasswordInput(render_value=True,
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su contraseña'
				}
			),
			'numero_contacto': NumberInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su telefono de contacto'
				}
			),
			'direccion': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su direccion'
				}
			),
			'groups': SelectMultiple(
				attrs={
					'class': 'form-control select2',
					'style': 'width: 100%',
					'multiple': 'multiple'
				}
			),		
		}
		exclude = ['user_permissions', 'last_login', 'date_joined', 'last_name', 'is_superuser', 'is_active', 'is_staff']

	def save(self, commit=True):
		data = {}
		form = super()
		try:
			if form.is_valid():
				pwd = self.cleaned_data['password']
				u = form.save(commit=False)
				if u.pk is None:
					u.set_password(pwd)
				else:
					user = User.objects.get(pk=u.pk)
					if user.password != pwd:
						u.set_password(pwd)
				u.save()
				u.groups.clear()
				for g in self.cleaned_data['groups']:
					u.groups.add(g)
			else:
				data['error'] = form.errors
		except Exception as e:
			data['error'] = str(e)
		return data

class UserCreationForm(UserCreationForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['rut'].widget.attrs['autofocus'] = True

	class Meta:
		model = User
		fields = ['rut', 'first_name', 'apellido_paterno', 'apellido_materno', 'direccion', 'numero_contacto', 'username', 'email', 'password1', 'password2']
		widgets = {
			'rut': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su rut sin puntos y con guión'
				}
			),
			'first_name': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese sus nombres'
				}
			),
			'apellido_paterno': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su apellido paterno'
				}
			),
			'apellido_materno': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su apellido materno'
				}
			),
			'username': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su nombre de usuario'
				}
			),
			'email': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su correo electronico'
				}
			),
			'password1': PasswordInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su contraseña'
				}
			),
			'password2': PasswordInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su contraseña'
				}
			),
			'numero_contacto': NumberInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su telefono de contacto'
				}
			),
			'direccion': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su direccion'
				}
			),		
		}
		exclude = ['groups', 'user_permissions', 'last_login', 'date_joined', 'last_name', 'is_superuser', 'is_active', 'is_staff']

class UserProfileForm(ModelForm):
	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.fields['rut'].widget.attrs['autofocus'] = True

	class Meta:
		model = User
		fields = 'rut', 'first_name', 'apellido_paterno', 'apellido_materno', 'direccion', 'numero_contacto', 'username', 'email', 'password'
		widgets = {
			'rut': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su rut sin puntos y con guión'
				}
			),
			'first_name': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese sus nombres'
				}
			),
			'apellido_paterno': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su apellido paterno'
				}
			),
			'apellido_materno': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su apellido materno'
				}
			),
			'username': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su nombre de usuario'
				}
			),
			'email': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su correo electronico'
				}
			),
			'password': PasswordInput(render_value=True,
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su contraseña'
				}
			),
			'numero_contacto': NumberInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su telefono de contacto'
				}
			),
			'direccion': TextInput(
				attrs={
					'class': 'form-control',
					'placeholder': 'ingrese su direccion'
				}
			),		
		}
		exclude = ['user_permissions', 'last_login', 'date_joined', 'last_name', 'is_superuser', 'is_active', 'is_staff', 'groups']

	def save(self, commit=True):
		data = {}
		form = super()
		try:
			if form.is_valid():
				pwd = self.cleaned_data['password']
				u = form.save(commit=False)
				if u.pk is None:
					u.set_password(pwd)
				else:
					user = User.objects.get(pk=u.pk)
					if user.password != pwd:
						u.set_password(pwd)
				u.save()
			else:
				data['error'] = form.errors
		except Exception as e:
			data['error'] = str(e)
		return data

class ResetPasswordForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder': 'Ingrese su usuario',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    def clean(self):
    	cleaned = super().clean()
    	if not User.objects.filter(username=cleaned['username']).exists():
    		raise forms.ValidationError('El usuario no existe')
    	return cleaned

    def get_user(self):
        username = self.cleaned_data.get('username')
        return User.objects.get(username=username)

class ChangePasswordForm(forms.Form):
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Ingrese una constraseña',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    confirmpassword = forms.CharField(widget=forms.PasswordInput(attrs={
        'placeholder': 'Repita la contraseña',
        'class': 'form-control',
        'autocomplete': 'off'
    }))

    def clean(self):
        cleaned = super().clean()
        password = cleaned['password']
        confirmpassword = cleaned['confirmpassword']
        if password != confirmpassword:
            raise forms.ValidationError('Las contraseñas deben ser iguales')
        return cleaned