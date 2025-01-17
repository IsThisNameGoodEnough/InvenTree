# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from import_export.admin import ImportExportModelAdmin

from .models import Currency


class CurrencyAdmin(ImportExportModelAdmin):
    list_display = ('symbol', 'suffix', 'description', 'value', 'base')


admin.site.register(Currency, CurrencyAdmin)
