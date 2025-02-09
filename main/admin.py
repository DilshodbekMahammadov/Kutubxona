from django.contrib import admin
from .models import *

class KitobInline(admin.StackedInline):
    model = Kitob
    extra = 1

class MuallifAdmin(admin.ModelAdmin):
    list_display = ['ism', 'davlat', 'kitob_soni', 'tirik']
    search_fields = ['ism']
    search_help_text = 'Muallif ismini kiriting'
    list_filter = ['tirik']
    list_display_links = ['ism']
    list_editable = ['kitob_soni', 'tirik']
    date_hierarchy = 't_sana'
    inlines = [KitobInline]

class KitobAdmin(admin.ModelAdmin):
    list_display = ['nom', 'muallif', 'sahifa']
    list_display_links = ['nom', 'muallif']
    list_filter = ['muallif', 'janr']
    list_per_page = 10
    list_editable = ['sahifa']
    search_fields = ['nom', 'janr']
    search_help_text = 'Kitob nomi yoki janrni kiriting'

class KutubxonachiAdmin(admin.ModelAdmin):
    list_display = ['ism', 'ish_vaqti']
    list_filter = ['ish_vaqti']
    search_fields = ['ism']
    search_help_text = 'Kutubxonachi ismini kiriting'

class RecordAdmin(admin.ModelAdmin):
    list_display = ['talaba', 'kitob', 'kutubxonachi']
    search_fields = ['talaba', 'kitob', 'kutubxonachi']

admin.site.register(Kitob, KitobAdmin)
admin.site.register(Muallif, MuallifAdmin)
admin.site.register(Kutubxonachi, KutubxonachiAdmin)
admin.site.register(Record, RecordAdmin)
