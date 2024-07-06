from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('client/', include('users.urls')),
    path('brand/', include('brands.urls')),
    path('car/', include('cars.urls')),
    path('cars/<slug:brand_slug>/', views.home, name = 'brand_wise_filtering'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)