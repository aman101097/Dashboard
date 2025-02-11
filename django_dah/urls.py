from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include

from django.views.generic import TemplateView

from django.conf import settings
from django.conf.urls.static import static

# Loading plotly Dash apps script
import django_dah.dash_app_code

#from django_plotly_dash.views import add_to_session

urlpatterns = [
    path('admin/', admin.site.urls),
	
	path('', include('django.contrib.auth.urls')),
	url('^dash_plot$', TemplateView.as_view(template_name='dash_plot.html'), name="dash_plot"),
	url('^django_plotly_dash/', include('django_plotly_dash.urls')),
	path('', TemplateView.as_view(template_name='home.html'), name='home'),
	path('click/',include('demo.urls')),
	path('plot/', include('demo.urls')),
]