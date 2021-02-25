from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView


urlpatterns = [
    path('', TemplateView.as_view(template_name='images/index.html'), name='index'),
    path('admin/', admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('image/', include('images.urls')),
]
