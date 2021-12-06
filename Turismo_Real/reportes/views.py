from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from .forms import ReporteForm
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from Servicio_Turismo_Real.models import DetalleCostoDepartamento, Departamento, CostoDepartamento
from django.db.models.functions import Coalesce
from django.db.models import Sum
from datetime import datetime
from random import randint

class ReportDetalleCostoDepartamentoView(TemplateView):
    template_name = 'reporte.html'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
    	data = {}
    	try:
    		action = request.POST['action']
    		if action == 'search_reporte':
    			data = []
    			start_date = request.POST.get('start_date', '')
    			end_date = request.POST.get('end_date', '')
    			search = DetalleCostoDepartamento.objects.all()
    			if len(start_date) and len(end_date):
    				search = search.filter(des_cos_fecha_ingreso__range=[start_date, end_date])
    			for s in search:
    				data.append([
    					s.id,
    					s.des_cos_fecha_ingreso.strftime('%Y-%m-%d'),
    					s.pf_fun.fun_nombre,
    					s.des_cos_dep_dia,
    					s.des_cos_dep_semanal
    				])

    			des_cos_dep_dia = search.aggregate(r=Coalesce(Sum('des_cos_dep_dia'), 0)).get('r')
    			des_cos_dep_semanal = search.aggregate(r=Coalesce(Sum('des_cos_dep_semanal'), 0)).get('r')

    			data.append([
    				'---',
    				'---',
    				'---',
    				des_cos_dep_dia,
    				des_cos_dep_semanal,

    			])
    		else:
    			data['error'] = 'No ha ingresado a ninguna opción'
    	except Exception as e:
    			data['error'] = str(e)
    	return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Reporte de Costos Departamentos'
        context['lista_url'] = reverse_lazy('reportedetallecostodepartamento')
        context['form'] = ReporteForm()
        return context

class DashboardView(TemplateView):
	template_name = 'dashboard.html'

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'get_graficos_cost_dep':
				data = {
					'name': 'Total de costos',
                    'showInLegend': False,
                    'colorByPoint': True,
                    'data': self.get_graficos_cost_dep()
				}
			elif action == 'get_graficos_cost_dep_porcent':
				data = {
					'name': 'Porcentaje',
        			'colorByPoint': True,
        			'data': self.get_graficos_cost_dep_porcent()
				}
			elif action == 'get_graficos_online':
				data = {'y': randint(1, 100)}
				print(data)
			else:
				data['error'] = 'No ha ingresado a ninguna opción'
		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data, safe=False)

	def get_graficos_cost_dep(self):
		data = []
		try:
			year = datetime.now().year
			for m in range(1, 13):
				total = DetalleCostoDepartamento.objects.filter(des_cos_fecha_ingreso__year=year, des_cos_fecha_ingreso__month=m).aggregate(r=Coalesce(Sum('des_cos_dep_dia'), 0)).get('r')
				data.append(total)
		except:
			pass
		return data

	def get_graficos_cost_dep_porcent(self):
		data = []
		year = datetime.now().year
		month = datetime.now().month
		try:
			for p in Departamento.objects.all():
				total = CostoDepartamento.objects.filter(des_cos__des_cos_fecha_ingreso__year=year, des_cos__des_cos_fecha_ingreso__month=month, dep_id=p.dep_id).aggregate(r=Coalesce(Sum('cos_mensual'), 0)).get('r')
				if total > 0:
					data.append({
						'name': p.dep_nombre,
	            		'y': float(total)
					})
		except:
			pass
		return data

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context['title'] = 'Reporte de Costos Departamentos'
		context['graficos_cost_dep'] = self.get_graficos_cost_dep()
		return context