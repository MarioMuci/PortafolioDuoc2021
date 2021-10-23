from django.shortcuts import render
from django.urls import reverse_lazy
from .models import ArticuloDepartamento, Departamento, ImagenDepartamento, Funcionario, Cargo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, FormView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import ArticuloDepartamentoForm, DepartamentoForm, ImagenDepartamentoForm, FuncionarioForm, TestForm
from django.http import JsonResponse
from .mixins import IsMixinDate, ValidatePermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

#Llamando aun HttpResponse
#def myfirstview(request):
	#return HttpResponse('Hola Mundo')

#Llamando aun JsonResponse
#def myfirstview(request):
	#data = {
		#'name': 'Matias'
	#}
	#return JsonResponse(data)
class ProntoView(TemplateView):
	template_name = 'pronto.html'

class HomeView(LoginRequiredMixin, ValidatePermissionRequiredMixin, IsMixinDate, ListView):
	permission_required = 'Servicio_Turismo_Real.is_funcionario'
	url_redirect = reverse_lazy('pronto')
	model = Departamento
	template_name = 'home.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Departamentos'
		return context

class IndexView(TemplateView):
	template_name = 'index.html'

class ArticuloDepartamentoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, IsMixinDate, ListView):
	model = ArticuloDepartamento
	template_name = 'Listar-ArticuloDepartamento.html'
	permission_required = 'Servicio_Turismo_Real.view_articulodepartamento'

	#def get_queryset(self):
		#return ArticuloDepartamento.objects.filter(art_dep_nombre__startswith='M')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'searchdata':
				data = []
				for i in ArticuloDepartamento.objects.all():
					data.append(i.toJSON())
			else:
				data['error'] = 'Ha ocurrido un error'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data, safe=False)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Listado de Articulos'
		context['crear_url'] = reverse_lazy('creararticulo')
		context['home_url'] = reverse_lazy('home')
		context['lista_url'] = reverse_lazy('listadoarticulo')
		return context

class ArticuloDepartamentoCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
	model = ArticuloDepartamento
	form_class = ArticuloDepartamentoForm
	template_name = 'Crear-ArticuloDepartamento.html'
	permission_required = 'Servicio_Turismo_Real.add_articulodepartamento'
	url_redirect = reverse_lazy('listadoarticulo')


	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'add':
				form = self.get_form()
				data = form.save()
			else:
				data['error'] = 'No ha ingresado a ninguna opción'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Crear Articulo'
		context['lista_url'] = reverse_lazy('listadoarticulo')
		context['home_url'] = reverse_lazy('home')
		context['action'] = 'add'
		return context

class ArticuloDepartamentoUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
	model = ArticuloDepartamento
	form_class = ArticuloDepartamentoForm
	template_name = 'Crear-ArticuloDepartamento.html'

	def dispatch(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'edit':
				form = self.get_form()
				data = form.save()
			else:
				data['error'] = 'No ha ingresado a ninguna opción'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Actualizar Articulo'
		context['lista_url'] = reverse_lazy('listadoarticulo')
		context['home_url'] = reverse_lazy('home')
		context['action'] = 'edit'
		return context

class ArticuloDepartamentoDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
	model = ArticuloDepartamento
	form_class = ArticuloDepartamentoForm
	template_name = 'Eliminar-ArticuloDepartamento.html'
	success_url = reverse_lazy('listadoarticulo')

	def dispatch(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			self.object.delete()
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Eliminar Articulo'
		context['lista_url'] = reverse_lazy('listadoarticulo')
		context['home_url'] = reverse_lazy('home')
		return context

class DepartamentoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, IsMixinDate, ListView):
	model = Departamento
	template_name = 'Listar-Departamento.html'

	#def get_queryset(self):
		#return ArticuloDepartamento.objects.filter(art_dep_nombre__startswith='M')

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'searchdata':
				data = []
				for i in Departamento.objects.all():
					data.append(i.toJSON())
			else:
				data['error'] = 'Ha ocurrido un error'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data, safe=False)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Listado de Departamento'
		context['crear_url'] = reverse_lazy('creardepartamento')
		context['home_url'] = reverse_lazy('home')
		context['lista_url'] = reverse_lazy('listadodepartamento')
		return context

class DepartamentoCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Departamento
    form_class = DepartamentoForm
    template_name = 'Crear-Departamento.html'
    success_url = reverse_lazy('listadodepartamento')

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
    	data = {}
    	try:
    		action = request.POST['action']
    		if action == 'add':
    			form = self.get_form()
    			data = form.save()
    		else:
    			data['error'] = 'No ha ingresado a ninguna opción'
    	except Exception as e:
    			data['error'] = str(e)
    	return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Departamento'
        context['lista_url'] = reverse_lazy('listadodepartamento')
        context['action'] = 'add'
        return context

class DepartamentoUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
	model = Departamento
	form_class = DepartamentoForm
	template_name = 'Crear-Departamento.html'
	success_url = reverse_lazy('listadodepartamento')

	def dispatch(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'edit':
				form = self.get_form()
				data = form.save()
			else:
				data['error'] = 'No ha ingresado a ninguna opción'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Actualizar Departamento'
		context['lista_url'] = reverse_lazy('listadodepartamento')
		context['home_url'] = reverse_lazy('home')
		context['action'] = 'edit'
		return context

class DepartamentoDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
	model = Departamento
	form_class = DepartamentoForm
	template_name = 'Eliminar-Departamento.html'
	success_url = reverse_lazy('listadodepartamento')

	def dispatch(self, request, *args, **kwargs):
		self.object = self.get_object()
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			self.object.delete()
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Eliminar Departamento'
		context['lista_url'] = reverse_lazy('listadodepartamento')
		context['home_url'] = reverse_lazy('home')
		return context

class ImagenDepartamentoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
	model = ImagenDepartamento
	template_name = 'imagenes.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Departamentos'
		context['lista_url'] = reverse_lazy('imagenesdepartamentos')
		return context

class FuncionarioView(LoginRequiredMixin, ValidatePermissionRequiredMixin, IsMixinDate, TemplateView):
    template_name = 'Listar-Funcionario.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Funcionario.objects.all():
                    data.append(i.toJSON())
            elif action == 'add':
            	fun = Funcionario()
            	fun.fun_rut = request.POST['fun_rut']
            	fun.fun_nombre = request.POST['fun_nombre']
            	fun.fun_apellido_paterno = request.POST['fun_apellido_paterno']
            	fun.fun_apellido_materno = request.POST['fun_apellido_materno']
            	fun.f_car = Cargo.objects.get(car_id=request.POST["f_car"])
            	fun.save()
            elif action == 'edit':
            	fun = Funcionario.objects.get(pk=request.POST['fun_id'])
            	fun.fun_rut = request.POST['fun_rut']
            	fun.fun_nombre = request.POST['fun_nombre']
            	fun.fun_apellido_paterno = request.POST['fun_apellido_paterno']
            	fun.fun_apellido_materno = request.POST['fun_apellido_materno']
            	fun.f_car = Cargo.objects.get(car_id=request.POST["f_car"])
            	fun.save()
            elif action == 'delete':
            	fun = Funcionario.objects.get(pk=request.POST['fun_id'])
            	fun.delete()
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Funcionarios'
        context['list_url'] = reverse_lazy('listadofuncionario')
        context['form'] = FuncionarioForm()
        return context

class TestView(TemplateView):
    template_name = 'test.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_product_id':
                data = [{'id': '', 'text': '------------'}]
                for i in Funcionario.objects.filter(f_car_id=request.POST['id']):
                    data.append({'id': i.fun_id, 'text': i.fun_nombre, 'data': i.f_car.toJSON()})
            elif action == 'autocomplete':
                data = []
                for i in Funcionario.objects.filter(fun_nombre__icontains=request.POST['term'])[0:10]:
                    item = i.toJSON()
                    item['text'] = i.fun_nombre
                    data.append(item)
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Select Aninados | Django'
        context['form'] = TestForm()
        return context
