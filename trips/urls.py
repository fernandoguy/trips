from django.conf.urls import url 
from trips import views 
from rest_framework_swagger.views import get_swagger_view

schema_view=get_swagger_view(title='API')

 
urlpatterns = [ 
    url(r'^docs$', schema_view,name='swagger'),
    url(r'^trips$', views.trip_list),
    url(r'^trips/(?P<pk>[0-9]+)$', views.trip_detail),
    url(r'^trips/total$', views.trip_total_viajes),
    url(r'^trips/totalxciudad/(?P<pk>[0-9]+)$', views.trip_total_viajes_ciudad),
    
        
]