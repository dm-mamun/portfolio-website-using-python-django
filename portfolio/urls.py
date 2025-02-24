from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from myportfolio import views  # Import views from your app


urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel
    path('', views.home, name='home'),  # Home page view
    path('contact/', views.contact, name='contact'),
    path('cv/', views.cv, name='cv'),

]

# Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
