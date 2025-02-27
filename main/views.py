from django.shortcuts import render, get_object_or_404, redirect
from django.template.context_processors import request

from .models import *
from django import forms
from .form import *

def home_view(request):
    return render(request, 'index.html')


def talaba_view(request):
    form = TalabaForm
    if request.method == "POST":
        talaba_form = TalabaForm(request.POST)
        if talaba_form.is_valid():
            talaba_form.save()
        return redirect('talabalar')
    talabalar = Talaba.objects.all()
    search = request.GET.get('search')
    if search is not None:
        talabalar = talabalar.filter(ism__contains=search)
    kurs = request.GET.get('kurs')
    if kurs is not None:
        if kurs != 'all':
            talabalar = talabalar.filter(kurs=kurs)
    guruh = request.GET.get('guruh')
    if guruh is not None:
        if guruh != 'all':
            talabalar = talabalar.filter(guruh=guruh)
    guruhlar = Talaba.objects.order_by('guruh').values_list('guruh', flat=True).distinct()
    kurslar = [1, 2, 3, 4]
    context = {
        'talabalar': talabalar,
        'search': search,
        'guruhlar': guruhlar,
        'kurs_query': kurs,
        'guruh_query': guruh,
        'kurslar': kurslar,
        'form' : form
    }
    return render(request, 'talabalar.html', context)


def muallif_view(request):
    mualliflar = Muallif.objects.all()
    search = request.GET.get('search')
    if search is not None:
        mualliflar = mualliflar.filter(ism__contains=search)
    context = {
        'mualliflar': mualliflar,
        'search': search,
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
    if request.method == "POST":
        Kitob.objects.create(
            nom=request.POST.get('nom'),
            annotatsiya=request.POST.get('annotatsiya'),
            janr=request.POST.get('janr'),
            sahifa=request.POST.get('sahifa'),
            muallif=request.POST.get('muallif')
        )
        return redirect('kitoblar')
    kitoblar = Kitob.objects.all()
    search = request.GET.get('search')
    if search is not None:
        kitoblar = kitoblar.filter(nom__contains=search)
    context = {
        'kitoblar': kitoblar,
        'search': search,
    }
    return render(request, 'kitoblar.html', context)


def kitob_details_view(request, kitob_id):
    kitob = Kitob.objects.get(id=kitob_id)
    context = {
        'kitob': kitob
    }
    return render(request, 'kitob_details.html', context)

def record_update_view(request, pk):
    form = RecordForm
    if request.method == 'POST':
        record_form = RecordForm(request.POST)
        if record_form.is_valid():
            record_form.save()
        return redirect('recordlar')
    record = get_object_or_404(Record, id=pk)
    context = {
        'form' : form,
        'record' : record,
    }
    return render(request, 'record_update.html', context)

def recordlar_view(request):
    kutubxonachilar = Kutubxonachi.objects.all()
    talabalar = Talaba.objects.all()
    kitoblar = Kitob.objects.all()
    if request.POST.get('olingan_sana') == '':
        olingan_sana = None
    else:
        olingan_sana = request.POST.get('olingan_sana')
    if request.POST.get('qaytarilgan_sana') == '':
        qaytarilgan_sana = None
    else:
        qaytarilgan_sana = request.POST.get('qaytarilgan_sana')
    if request.method == 'POST':
        Record.objects.create(
            talaba_id=request.POST.get('talaba_id'),
            kitob_id=request.POST.get('kitob_id'),
            kutubxonachi_id=request.POST.get('kutubxonachi_id'),
            olingan_sana=request.POST.get('olingan_sana'),
            qaytarilgan_sana=request.POST.get('qaytarilgan_sana'),
            qaytardi=request.POST.get('qaytardi')
        )
        return redirect('recordlar')
    recordlar = Record.objects.all()
    context = {
        'recordlar': recordlar,
        'kutubxonachilar': kutubxonachilar,
        'talabalar': talabalar,
        'kitoblar': kitoblar
    }
    return render(request, 'recordlar.html', context)


def tirik_mualliflar_view(request):
    mualliflar = Muallif.objects.filter(tirik=True)
    context = {
        'mualliflar': mualliflar
    }
    return render(request, 'tirik_mualliflar.html', context)


def sahifasi_katta_vievs(request):
    kitoblar = Kitob.objects.order_by('-sahifa')[:3]
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'sahifasi_katta.html', context)


def kitobi_kop_view(request):
    mualliflar = Muallif.objects.all().order_by('-kitob_soni')[:3]
    context = {
        'mualliflar': mualliflar
    }
    return render(request, 'kitobi_kop.html', context)


def oxirgi_recordlar_view(request):
    recordlar = Record.objects.order_by('-olingan_sana')[:3]
    context = {
        'recordlar': recordlar
    }
    return render(request, 'oxirgi_olingan.html', context)


def muallif_kitobi_view(request):
    kitoblar = Kitob.objects.filter(muallif__tirik=True)
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'muallif_kitobi.html', context)


def badiy_kitoblar_view(request):
    kitoblar = Kitob.objects.filter(janr='Badiiy')
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'badiy_kitoblar.html', context)


def kitob_soni_view(request):
    mualliflar = Muallif.objects.filter(kitob_soni__lt=10)
    kitoblar = Kitob.objects.filter(muallif__in=mualliflar)
    context = {
        'kitoblar': kitoblar
    }
    return render(request, 'kitob_soni.html', context)


def record_details_view(request, record_id):
    record = Record.objects.get(id=record_id)
    context = {
        'record': record
    }
    return render(request, 'record_details.html', context)


def talaba_update_view(request, pk):
    if request.method == 'POST':
        talaba = Talaba.objects.filter(pk=pk)
        talaba.update(
            ism=request.POST.get('ism'),
            kurs=request.POST.get('kurs'),
            guruh=request.POST.get('guruh'),
            yosh=request.POST.get('yosh'),
            kitob_soni=request.POST.get('kitob_soni')
        )
        return redirect('talabalar')
    talaba = get_object_or_404(Talaba, id=pk)
    context = {
        'talaba': talaba
    }
    return render(request, 'talaba_update.html', context)


def talaba_delete_view(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)
    talaba.delete()
    return redirect('talabalar')


def talaba_delete_confirm_view(request, pk):
    talaba = get_object_or_404(Talaba, id=pk)
    context = {
        'talaba': talaba
    }
    return render(request, 'talaba_delete_confirm.html', context)


def kitob_delete_view(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)
    kitob.delete()
    return redirect('kitoblar')


def kitob_delete_confirm_view(request, pk):
    kitob = get_object_or_404(Kitob, id=pk)
    context = {
        'kitob': kitob
    }
    return render(request, 'kitob_delete_confirm.html', context)


def muallif_qoshish_view(request):
    form = MuallifForm
    if request.method == "POST":
        if request.POST.get('kitob_soni') == '':
            kitob_soni = None
        else:
            kitob_soni = int(request.POST.get('kitob_soni'))
        if request.POST.get('t_sana') == '':
            t_sana = None
        else:
            t_sana = request.POST.get('t_sana')
        muallif_form = MuallifForm(request.POST)
        if muallif_form.is_valid():
            muallif_form.save()
        return redirect('mualliflar')
    context = {
        'form' : form
    }
    return render(request, 'muallif_qoshish.html', context)


def muallif_update_view(request, pk):
    form = MuallifForm
    if request.method == 'POST':
        muallif_form = MuallifForm(request.POST)
        if muallif_form.is_valid():
            muallif_form.save()
        return redirect('mualliflar')
    muallif = get_object_or_404(Muallif, id=pk)
    context = {
        'form': form,
    }
    return render(request, 'muallif_update.html', context)


def kitob_update_view(request, pk):
    if request.method == 'POST':
        kitob = Kitob.objects.filter(pk=pk)
        kitob.update(
            nom=request.POST.get('nom'),
            annotatsiya=request.POST.get('annotatsiya'),
            janr=request.POST.get('janr'),
            sahifa=request.POST.get('sahifa'),
            muallif=Muallif.objects.get(id=request.POST.get('muallif_id'))
        )
        return redirect('kitoblar')
    kitob = get_object_or_404(Kitob, id=pk)
    mualliflar = Muallif.objects.exclude(id=kitob.muallif.id).order_by('ism')
    context = {
        'kitob': kitob,
        'mualliflar': mualliflar
    }
    return render(request, 'kitob_update.html', context)


def kutubxonachi_view(request):
    kutubxonachi = Kutubxonachi.objects.all()
    context = {
        'kutubxonachi': kutubxonachi,
    }
    return render(request, 'kutubxonachi.html', context)


def kutubxonachi_update_view(request, pk):
    if request.method == 'POST':
        kutubxonachi = Kutubxonachi.objects.filter(pk=pk)
        kutubxonachi.update(
            ism=request.POST.get('ism'),
            ish_vaqti=request.POST.get('ish_vaqti')
        )
        return redirect('kutubxonachilar')
    return render(request, 'kutubxonachi_update.html')


def kutubxonachi_qoshish_view(request):
    form = KutubxonachiForm
    if request.method == 'POST':
        kutubxonachi_form = KutubxonachiForm(request.POST)
        if kutubxonachi_form.is_valid():
            kutubxonachi_form.save()
        return redirect('kutubxonachilar')
    kutubxonachi = Kutubxonachi.objects.all()
    context = {
        'form': form
    }
    return render(request, 'kutubxonachi_qoshish.html', context)
