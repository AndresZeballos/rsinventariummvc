from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^inventario/$', 'inventario.views.consultar'),
    url(r'^inventario/filtrar/$', 'inventario.views.filtrar'),
    url(r'^inventario/(?P<art_id>\d+)/$', 'inventario.views.detalle'),
    
    url(r'^stock/$', 'inventario.views.stock'),
    
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'inventario.views.index'),

)
