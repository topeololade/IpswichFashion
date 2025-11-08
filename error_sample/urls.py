from django.urls import path
from . import views

urlpatterns = [
    path('sentry-debug/', views.trigger_error, name='sentry-debug'),
]