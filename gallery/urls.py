from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from gallery import views

urlpatterns = [
    path('', views.index, name="index"),
    #path('category', views.category_list, name='category')
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
