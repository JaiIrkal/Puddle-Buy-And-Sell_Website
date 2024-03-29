from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from core.views import index
from core.views import contact

#Consists of all URL definitions
urlpatterns = [
    path('', include('core.urls')),
    path('item/', include('item.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
    path('dashboard/', include('dashboard.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
