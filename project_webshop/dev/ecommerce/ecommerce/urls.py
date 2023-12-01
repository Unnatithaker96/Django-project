#from xml.dom.minidom import Document
from django.contrib import admin
from django.urls import path, include

from django.conf import settings

from django.conf.urls.static import static  #It helps to create a unique url path for our images

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)