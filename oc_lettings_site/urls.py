from django.contrib import admin
from django.urls import path, include
from . import views
from .views import handler_404, handler_500


handler404 = handler_404
handler400 = handler_500


urlpatterns = [
    path('', views.index, name='index'),
    path('lettings/', include('lettings.urls', namespace='lettings')),
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('admin/', admin.site.urls),
]
