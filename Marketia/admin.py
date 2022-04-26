from django.contrib import admin
from Marketia.models import Services
from tof.admin import TofAdmin, TranslationTabularInline
# Register your models here.


admin.site.register(Services)

# @admin.register(Services)
# class ServicesAdmin(TofAdmin):
#     list_display = ('name', 'description')
#     search_fields = ('name', )
#     inlines = (TranslationTabularInline, )
#
# admin.site.register(Services, TofAdmin)