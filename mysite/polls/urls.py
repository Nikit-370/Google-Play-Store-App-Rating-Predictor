from django.urls import path
from .views import index_func

urlpatterns = [
    path('', index_func, name='homepage'),
    ]