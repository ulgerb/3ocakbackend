
# url linklerimizi yazarken kullanıyoruz
# path('url', fonksiyon),

from django.contrib import admin
from django.urls import path
from appMy.views import indexPage

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', indexPage),
]
