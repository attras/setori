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
]