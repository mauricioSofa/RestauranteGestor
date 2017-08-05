from django.conf.urls import include, url
from . import views
from django.contrib.auth.views import login


urlpatterns = [
    url(r'^$', login,{'template_name':'gestor/login.html'}, name = 'login'),
    url(r'^regventa/$', views.venta_new,name = 'Servicio'),
    url(r'^regfecha/$', views.fecha_new,name = 'Fecha'),
    url(r'^regcliente/$', views.cliente_new,name = 'Cliente'),
    url(r'^tablaventa/$', views.tabla_new,name = 'TablaVenta'),
]
