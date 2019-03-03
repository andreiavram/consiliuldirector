from django.contrib import admin

# Register your models here.
from decont.models import LinieDecont, LinieAvans, Decont


class LinieAvansInlineAdmin(admin.TabularInline):
    model = LinieAvans


class LinieDecontInlineAdmin(admin.TabularInline):
    model = LinieDecont


class DecontAdmin(admin.ModelAdmin):
    list_display = ["activitate", "titular", "centrul_local", "data_decont", "valuta"]
    list_filter = ["activitate", "titular"]

    inlines = [LinieAvansInlineAdmin, LinieDecontInlineAdmin]


admin.site.register(Decont, DecontAdmin)
