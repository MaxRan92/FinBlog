from . import views
from django.urls import path

urlpatterns = [
    path('', views.AssetList.as_view(), name='home')
]