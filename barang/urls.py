from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('barang/<int:id_barang>/', views.detailBarang, name='barang-detail'),
    path('barang/tambah/', views.addBarang, name='add-barang'),
    path('post-barang/', views.postBarang, name='post-barang'),
]