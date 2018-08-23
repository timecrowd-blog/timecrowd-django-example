from django.urls import include, path

from . import views

urlpatterns = [
    path('', views.index),
    path('dashboard', views.dashboard),
    path('', include(('django.contrib.auth.urls', 'auth'))),
    path('', include(('social_django.urls', 'social'))),
]
