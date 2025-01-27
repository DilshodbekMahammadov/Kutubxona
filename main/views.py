from django.shortcuts import render
from .models import *
from django.utils import timezone

def home_view(request):
    return render(request, 'index.html')
def talaba_view(request):
    talabalar = Talaba.objects.all()
    context = {
        'talabalar': talabalar,
    }
    return render(request, 'talabalar.html', context)
def muallif_view(request):
    mualliflar = Muallif.objects.all()
    context = {
        'mualliflar': mualliflar,
    }
    return render(request, 'mualliflar.html', context)
def talaba_details_view(request, talaba_id):
    talaba = Talaba.objects.get(id=talaba_id)
    context = {
        'talaba': talaba
    }
    return render(request, 'talaba_details.html', context)
def muallif_details_view(request, muallif_id):
    muallif = Muallif.objects.get(id=muallif_id)
    context = {
        'muallif': muallif
    }
    return render(request, 'muallif_details.html', context)
def kitob_view(request):
    kitoblar = Kitob.objects.all()
    context = {
        'kitoblar' : kitoblar
    }
    return render(request, 'kitoblar.html', context)
def kitob_details_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
        'kitob' : kitob
    }
    return render(request, 'kitob_details.html', context)
def recordlar_view(request):
    recordlar = Record.objects.all()
    context = {
        'recordlar' : recordlar
    }
    return render(request, 'recordlar.html', context)
def tirik_mualliflar_view(request):
    mualliflar = Muallif.objects.filter(tirik=True)
    context = {
        'mualliflar' : mualliflar
    }
    return render(request, 'tirik_mualliflar.html',context)
def sahifasi_katta_vievs(request):
    kitoblar = Kitob.objects.order_by('-sahifa')[:3]
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'sahifasi_katta.html', context)
def kitobi_kop_view(request):
    mualliflar = Muallif.objects.all().order_by('-kitob_soni')[:3]
    context = {
        'mualliflar' : mualliflar
    }
    return render(request, 'kitobi_kop.html', context)
def oxirgi_recordlar_view(request):
    recordlar = Record.objects.order_by('-olingan_sana')[:3]
    context = {
        'recordlar' : recordlar
    }
    return render(request, 'oxirgi_olingan.html', context)
def muallif_kitobi_view(request):
    kitoblar = Kitob.objects.filter(muallif__tirik=True)
    context = {
        'kitoblar' : kitoblar
    }
    return render(request, 'muallif_kitobi.html', context)
def badiy_kitoblar_view(request):
    kitoblar = Kitob.objects.filter(janr='Badiiy')
    context = {
        'kitoblar' : kitoblar
    }
    return render(request, 'badiy_kitoblar.html', context)
def kitob_soni_view(request):
    mualliflar = Muallif.objects.filter(kitob_soni__lt=10)
    kitoblar = Kitob.objects.filter(muallif__in=mualliflar)
    context = {
        'kitoblar' : kitoblar
    }
    return render(request, 'kitob_soni.html', context)
def record_details_view(request, record_id):
    record = Record.objects.get(id=record_id)
    context = {
        'record' : record
    }
    return render(request, 'record_details.html', context)
