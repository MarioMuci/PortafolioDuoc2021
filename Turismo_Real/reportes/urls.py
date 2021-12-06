from django.urls import path

from reportes.views import *
urlpatterns = [
    path('ReporteDetalleCostoDepartamento/', ReportDetalleCostoDepartamentoView.as_view(), name='reportedetallecostodepartamento'),
    path('Dashboard/', DashboardView.as_view(), name='dashboard'),

]