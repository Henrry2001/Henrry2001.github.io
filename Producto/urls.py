from django.urls import path, include
from Producto import views
from . import views
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static

urlpatterns = [
    path('',login_required(views.Tendencia), name="Inicio"),
]

urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)