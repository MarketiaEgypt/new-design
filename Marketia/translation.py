from modeltranslation.translator import TranslationOptions, translator
from Marketia.models import Services


class ServicesTranslationOptions(TranslationOptions):
    fields = ('name','description',)


translator.register(Services, ServicesTranslationOptions)