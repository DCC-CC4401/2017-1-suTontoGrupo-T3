"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    # app/
    url(r'^$', views.index, name='index'),
    # app/login/
    url(r'^login/$', views.login, name='login'),
    url(r'^gestion_productos/$', views.gestion_productos, name='gestion_productos'),
    url(r'^home/$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^vendedor_profile$', views.vendedor_profile, name='vendedor_profile'),
    url(r'^vendedor_profileAlumno$', views.vendedor_profileAlumno, name='vendedor_profileAlumno'),
    url(r'^vendedor_edit$', views.vendedor_edit, name='vendedor_edit'),
    url(r'^editar_producto/$', views.editar_producto, name='editar_producto'),
    url(r'^add_item/$', views.add_item, name='add_item'),

]
