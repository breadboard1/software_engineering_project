from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name = 'home'),
    path('category/<slug:category_slug>/', views.home, name = 'category_wise_post'),
    path('author/', include('authors.urls')),
    path('post/', include('posts.urls')),
    path('category/', include('categories.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)