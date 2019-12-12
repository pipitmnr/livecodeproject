from django.db import models

# Create your models here.
class Produk(models.Model):
    nama_produk = models.CharField(max_length=50)
    harga_produk = models.IntegerField()
    deskripsi_produk = models.CharField(max_length=1000)
    img_produk = models.CharField(max_length=1000)
    def __str__(self):
        return "Produk %s" %(self.nama_produk)