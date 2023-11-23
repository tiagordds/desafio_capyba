
from django.contrib import admin
from django.urls import path, include, re_path
from capyba import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('register/', views.register, name='register'),
    re_path('signup', views.signup),
    re_path('login', views.login),
    re_path('test_token', views.test_token),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
