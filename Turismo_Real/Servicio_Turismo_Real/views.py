from django.shortcuts import render
from django.urls import reverse_lazy
from .models import ArticuloDepartamento, Departamento, ImagenDepartamento, Funcionario, Cargo, DetalleCostoDepartamento, CostoDepartamento, Reserva
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView, FormView, View, DetailView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .forms import ArticuloDepartamentoForm, DepartamentoForm, ImagenDepartamentoForm, FuncionarioForm, DetalleCostoDepartamentoForm
from django.http import JsonResponse, HttpResponse
from .mixins import IsMixinDate, ValidatePermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
import json
from django.db import transaction
from user.models import User

import os
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect
from django.template.loader import get_template
from xhtml2pdf import pisa

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

class ListadoDepartamentosDisponibles(LoginRequiredMixin, IsMixinDate, ListView):
	model = Departamento
	template_name = 'DisponibilidadDepartamentos.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def get_queryset(self):
		queryset = self.model.objects.filter(dep_estado = True, dep_ocupacion__gte = 1)
		return queryset

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Departamentos Disponibles'
		return context

class DetalleDepartamentosDisponibles(LoginRequiredMixin, IsMixinDate, DetailView):
	model = Departamento
	template_name = 'DetalleDepartamentos.html'

class RegistrarReserva(LoginRequiredMixin, CreateView):
	model = Reserva
	success_url = reverse_lazy('listadodepartamentosdisponibles')

	def post(self, request, *args, **kwargs):
		if request.is_ajax():
			f_dep = Departamento.objects.filter(dep_id = request.POST.get('f_dep')).first()
			f_use = User.objects.filter(id = request.POST.get('f_use')).first()
			if f_dep and f_use:
				nuevareserva = self.model(
					f_dep = f_dep,
					f_use = f_use
				)
				nuevareserva.save()
				mensaje = 'Su reserva se guardo correctamente'
				error = 'Su reserva no guardo correctamente'
				response = JsonResponse({'mensaje': mensaje, 'error': error, 'url':self.success_url})
				response.status_code = 201
				return response
		return redirect('listadodepartamentosdisponibles')

class HomeView(LoginRequiredMixin, ValidatePermissionRequiredMixin, IsMixinDate, ListView):
	permission_required = 'user.is_funcionario'
	url_redirect = reverse_lazy('index')
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
	permission_required = 'Servicio_Turismo_Real.change_articulodepartamento'


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
	permission_required = 'Servicio_Turismo_Real.delete_articulodepartamento'

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

class DetalleCostoDepartamentoView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = DetalleCostoDepartamento
    form_class = DetalleCostoDepartamentoForm
    template_name = 'GastoDepartamento.html'
    success_url = reverse_lazy('index')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
    	data = {}
    	try:
    		action = request.POST['action']
    		if action == 'search_deptos':
    			data = []
    			term = request.POST['term']
    			deptos = Departamento.objects.filter()
    			if len(term):
    				deptos = deptos.filter(dep_nombre__icontains=term)
    			for i in deptos[0:10]:
    				item = i.toJSON()
    				item['value'] = i.dep_nombre
    				data.append(item)
    		elif action == 'add':
    			with transaction.atomic():
	    			det = json.loads(request.POST['det'])
	    			detalledep = DetalleCostoDepartamento()
	    			detalledep.pf_fun_id = det['pf_fun']
	    			detalledep.des_cos_dep_dia = det['des_cos_dep_dia']
	    			detalledep.des_cos_dep_semanal = det['des_cos_dep_semanal']
	    			detalledep.save()
	    			for i in det['deptos']:
	    				det = CostoDepartamento()
	    				det.des_cos_id = detalledep.id
	    				det.dep_id = i['dep_id']
	    				det.cos_mensual = int(i['dep_costo_mes'])
	    				det.cos_cant = int(i['cant'])
	    				det.cos_subtotal = int(i['subtotal'])
	    				det.save()
	    			data = {'id': detalledep.id}
    		elif action == 'crear_funcionario':
	    		with transaction.atomic():
	    			frmfuncionario = FuncionarioForm(request.POST)
	    			data = frmfuncionario.save()
    		else:
    			data['error'] = 'No ha ingresado a ninguna opción'
    	except Exception as e:
    			data['error'] = str(e)
    	return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Costos'
        context['home_url'] = reverse_lazy('home')
        context['lista_url'] = reverse_lazy('listadetallecostodepartamento')
        context['reporte_url'] = reverse_lazy('reportedetallecostodepartamento')
        context['crear_url'] = reverse_lazy('detallecostodepartamento')
        context['dashboard_url'] = reverse_lazy('dashboard')
        context['action'] = 'add'
        context['det'] = []
        context['frmfuncionario'] = FuncionarioForm()
        return context

class DetalleCostoDepartamentoListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, IsMixinDate, ListView):
	model = DetalleCostoDepartamento
	template_name = 'Listar-GastosDepartamento.html'

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
				for i in DetalleCostoDepartamento.objects.all():
					data.append(i.toJSON())
			elif action == 'search_details_depto':
				data = []
				for i in CostoDepartamento.objects.filter(des_cos_id=request.POST['id']):
					data.append(i.toJSON())
			else:
				data['error'] = 'Ha ocurrido un error'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data, safe=False)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Listado Detalle Costos Departamento'
		context['crear_url'] = reverse_lazy('detallecostodepartamento')
		return context

class DetalleCostoDepartamentoUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = DetalleCostoDepartamento
    form_class = DetalleCostoDepartamentoForm
    template_name = 'GastoDepartamento.html'
    success_url = reverse_lazy('index')

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
    	data = {}
    	try:
    		action = request.POST['action']
    		if action == 'search_deptos':
    			data = []
    			term = request.POST['term']
    			deptos = Departamento.objects.filter()
    			if len(term):
    				deptos = deptos.filter(dep_nombre__icontains=term)
    			for i in deptos[0:10]:
    				item = i.toJSON()
    				item['value'] = i.dep_nombre
    				data.append(item)
    		elif action == 'edit':
    			det = json.loads(request.POST['det'])
    			detalledep = self.get_object()
    			detalledep.pf_fun_id = det['pf_fun']
    			detalledep.des_cos_dep_dia = det['des_cos_dep_dia']
    			detalledep.des_cos_dep_semanal = det['des_cos_dep_semanal']
    			detalledep.save()
    			detalledep.costodepartamento_set.all().delete()
    			for i in det['deptos']:
    				det = CostoDepartamento()
    				det.des_cos_id = detalledep.id
    				det.dep_id = i['dep_id']
    				det.cos_mensual = int(i['dep_costo_mes'])
    				det.cos_cant = int(i['cant'])
    				det.cos_subtotal = int(i['subtotal'])
    				det.save()
    			data = {'id': detalledep.id}
    		else:
    			data['error'] = 'No ha ingresado a ninguna opción'
    	except Exception as e:
    			data['error'] = str(e)
    	return JsonResponse(data, safe=False)

    def get_details_departamento(self):
    	data = []
    	try:
    		for i in CostoDepartamento.objects.filter(des_cos_id=self.get_object().id):
    			item = i.dep.toJSON()
    			item['cant'] = i.cos_cant
    			data.append(item)
    	except:
    		pass
    	return data


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar'
        context['home_url'] = reverse_lazy('home')
        context['lista_url'] = reverse_lazy('listadetallecostodepartamento')
        context['action'] = 'edit'
        context['det'] = json.dumps(self.get_details_departamento())
        return context

class DetalleCostoDepartamentoDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
	model = DetalleCostoDepartamento
	form_class = DetalleCostoDepartamentoForm
	template_name = 'Eliminar-DetalleCostoDepartamento.html'
	success_url = reverse_lazy('listadetallecostodepartamento')

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
		context['title'] = 'Eliminar Detalle Costo Departamento'
		context['lista_url'] = reverse_lazy('listadetallecostodepartamento')
		context['home_url'] = reverse_lazy('home')
		return context

class DetalleCostoDepartamentoPdfView(View):

	def link_callback(self, uri, rel):
		
		sUrl = settings.STATIC_URL
		sRoot = settings.STATIC_ROOT
		mUrl = settings.MEDIA_URL
		mRoot = settings.MEDIA_ROOT
		if uri.startswith(mUrl):
			path = os.path.join(mRoot, uri.replace(mUrl, ""))
		elif uri.startswith(sUrl):
			path = os.path.join(sRoot, uri.replace(sUrl, ""))
		else:
			return uri

		if not os.path.isfile(path):
			raise Exception(
				'media URI must start with %s or %s' % (sUrl, mUrl)
				)
		return path

	def get(self, request, *args, **kwargs):
		try:
			template = get_template('invoice.html')
			context = {
				'detallecostodepartamento': DetalleCostoDepartamento.objects.get(pk=self.kwargs['pk']),
				'icon': '{}{}'.format(settings.MEDIA_URL, 'turismologopngicono.png')
			}
			html = template.render(context)
			response = HttpResponse(content_type='application/pdf')
			pisa_status = pisa.CreatePDF(
				html, dest=response,
				link_callback=self.link_callback
			)
			return response
		except:
			pass
		return HttpResponseRedirect(reverse_lazy('listadetallecostodepartamento'))

