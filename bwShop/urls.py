from django.contrib import admin
from django.urls import path, include
from django.views.static import serve

import xadmin

from bwShop.settings import MEDIA_ROOT

urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    path('media/<path:path>', serve, {'document_root': MEDIA_ROOT}),
]
