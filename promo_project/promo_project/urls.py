from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('products/', include('products.urls')),
    path('promotions/', include('promotions.urls')),
    path('stores/', include('stores.urls')),
    path('map/', include('map.urls')),
    path('social/', include('social_django.urls', namespace='social')),
    path('logout/', auth_views.LogoutView.as_view(template_name='home/index.html'), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
