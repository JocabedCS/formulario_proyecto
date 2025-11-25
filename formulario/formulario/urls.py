from django.contrib import admin
from django.urls import path
from formulario_app.views import registro_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registro/', registro_view, name='registro'),
]
