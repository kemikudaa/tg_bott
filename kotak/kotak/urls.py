from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.conf import settings
from django.conf.urls.static import static

def home(request):
    return HttpResponse("Welcome to the Cat Bot!")

urlpatterns = [
    path('', home),  # Главная страница
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
