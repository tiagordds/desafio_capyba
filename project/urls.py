
from django.contrib import admin
from django.urls import path, include
from capyba import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('usuarios/', views.lista_usuario),
    path('usuarios/<int:id>', views.informacao_usuario),
    path('summernote/', include('django_summernote.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
