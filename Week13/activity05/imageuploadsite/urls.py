
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from uploader import views

urlpatterns = [
    path('', views.upload_page, name='upload'),
    path('bmi', include('bmi.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
