"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path("talabalar/", talaba_view, name='talabalar'),
    path('mualliflar/', muallif_view, name='mualliflar'),
    path('talabalar/<int:talaba_id>/', talaba_details_view),
    path('mualliflar/<int:muallif_id>/', muallif_details_view),
    path('kitoblar/', kitob_view, name='kitoblar'),
    path('kitoblar/<int:kitob_id>/', kitob_details_view),
    path('recordlar/', recordlar_view, name='recordlar'),
    path('tirik_mualliflar/', tirik_mualliflar_view),
    path('kitobi_kop/', kitobi_kop_view),
    path('oxirgi_recordlar/', oxirgi_recordlar_view),
    path('muallif_kitobi/', muallif_kitobi_view),
    path('badiy_kitoblar/', badiy_kitoblar_view),
    path('kitob_soni/', kitob_soni_view),
    path('record_details/<int:record_id>/', record_details_view),
    path("talabalar/<int:pk>/o'chirish/", talaba_delete_view),
    path("talabalar/<int:pk>/tahrirlash/", talaba_update_view),
    path("recordlar/<int:pk>/tahrirlash/", record_update_view),
    path("mualliflar/<int:pk>/tahrirlash/", muallif_update_view),
    path("talabalar/<int:pk>/o'chirish/tasdiqlash/", talaba_delete_confirm_view),
    path("kitoblar/<int:pk>/o'chirish/",kitob_delete_view),
    path("kitoblar/<int:pk>/o'chirish/tasdiqlash/",kitob_delete_confirm_view),
    path('muallif-qoshish/', muallif_qoshish_view, name='muallif-qoshish'),
    path("kitoblar/<int:pk>/tahrirlash/", kitob_update_view),
    path("kutubxonachilar/", kutubxonachi_view, name='kutubxonachilar'),
    path("kutubxonachi/", kutubxonachi_qoshish_view),
    path("kutubxonachi/", kutubxonachi_update_view)
]
