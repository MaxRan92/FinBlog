from . import views
from django.urls import path

urlpatterns = [
    path('', views.AssetList.as_view(), name='home'),
    path('<slug:slug>/', views.AssetDetail.as_view(), name='asset_detail'),
]