#from django.contrib import admin
##from django.urls import path
##from core.views import index, contact
from django.conf import settings
from django.conf.urls.static import static
from django.contrib  import admin 
from django.urls import path,include


app_name = 'core'

urlpatterns = [
    path('', include ('core.urls')),
    path('items/', include('item.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('admin/', admin.site.urls ),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)