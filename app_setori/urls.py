from django.urls import path,include,re_path
# from django.conf.urls import url,handler403

from .views import *

app_name = 'app_setori'

urlpatterns = [
    #alamat.namafunction
    path('', home.HomeViews.as_view(), name = 'home'),
    path('login/', auth.LoginViews.as_view(), name = 'login'),
    path('admin/', admin_index.Admin_indexViews.as_view(), name = 'adminindex'),
    path('master_user', master_user.Master_userViews.as_view(), name = 'master_user'),

    #userviewpath
     path('berita', berita.BeritaViews.as_view(), name = 'berita'),
     path('data', data_pokok.Data_pokokViews.as_view(), name = 'data'),
     path('potensi', potensi.PotensiViews.as_view(), name = 'potensi'),
     path('layanan', layanan.LayananViews.as_view(), name = 'layanan'),
     path('faq', faq.FaqViews.as_view(), name = 'faq'),
     path('tentang', tentang.TentangViews.as_view(), name = 'tentang'),
     path('kontak', kontak.KontakViews.as_view(), name = 'kontak'),
]