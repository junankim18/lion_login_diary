from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('diary.urls')),
    path('account', include('account.urls')),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'helpers.views.page_not_found'