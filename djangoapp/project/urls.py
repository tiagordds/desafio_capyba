
from django.contrib import admin
from django.urls import path, include
from capyba import views


urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('usuarios/', views.lista_usuario),
    path('usuarios/<int:id>', views.informacao_usuario),
    path('summernote/', include('django_summernote.urls')),
]
