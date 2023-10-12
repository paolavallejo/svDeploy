"""
URL configuration for sasvar project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from sasvar_app import views as sasvarViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', sasvarViews.home),
    path('about/', sasvarViews.about),
    path('bienvenida/', sasvarViews.bienvenida),
    path('inicio/', sasvarViews.inicio, name='inicio'),
    path('intro_1/', sasvarViews.intro_1, name='intro_1'),
    path('escaneo/', sasvarViews.escaneo, name='escaneo'),
    path('intro_6/', sasvarViews.intro_6, name='intro_6'),
    path('categorias/', sasvarViews.categorias, name='categorias'),
    path('detalle_reci_q1/', sasvarViews.detalle_reci_q1, name='detalle_reci_q1'),
    path('detalle-reci-2/', sasvarViews.detalle_reci_2, name='detalle-reci-2'),
    path('detalle-no-aprov/', sasvarViews.detalle_no_aprov, name='detalle-no-aprov'),
    path('detalle-org/', sasvarViews.detalle_org, name='detalle-org'),
    path('carga/', sasvarViews.carga, name='carga'),
    path('resultado/', sasvarViews.resultado, name='resultado'),
    path('clasificar/', sasvarViews.clasificar, name='clasificar'),

    path('guardar_imagen/', sasvarViews.guardar_imagen, name='guardar_imagen'),

    #path('classify_garbage/', sasvarViews.classify_garbage_image, name='classify_garbage'),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
