from django.shortcuts import render
from django.http import HttpResponse
from .models import Produk
from django.shortcuts import redirect


# Create your views here.
def index(request):
    barangs = Produk.objects.all()
    data_barang = {'barangs': barangs}
    return render(request, 'barang/index.html', data_barang)
def addBarang(request):
    return render(request, 'barang/add-barang.html')
def postBarang(request):
    nama_produk = request.POST['nama_produk']
    harga_produk = request.POST['harga_produk']
    deskripsi_produk = request.POST['deskripsi_produk']
    img_produk = request.POST['img_produk']
    post = Produk(nama_produk=nama_produk, harga_produk=harga_produk, deskripsi_produk=deskripsi_produk, img_produk=img_produk)
    post.save()
    barangs = Produk.objects.all()
    return redirect('barang')
def detailBarang(request, id_barang):
    barangs = Produk.objects.get(pk=id_barang)
    return render(request, 'barang/barang-detail.html', {'barang': barangs})