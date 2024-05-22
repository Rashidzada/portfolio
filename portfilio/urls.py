
from django.contrib import admin
from django.urls import path,include
admin.site.site_title = "My Portfilio"
admin.site.site_header = "My Portfilio"
from django.conf.urls.static import static , settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app.urls')),
]+static(settings.MEDIA_URL , document_root = settings.MEDIA_ROOT)
