from django.contrib import admin

from decizii.models import Registru, IntrareRegistru, MembruConsiliulDirector, Decizie, ConsiliulDirector, \
    ActiuneDecizie

admin.site.register(ConsiliulDirector)
admin.site.register(Registru)
admin.site.register(IntrareRegistru)
admin.site.register(MembruConsiliulDirector)


class DecizieAdmin(admin.ModelAdmin):
    list_display = ["titlu", "text", "initiator", "get_status_display", "data_creata"]
    list_filter = ["initiator"]


class ActiuneDecizieAdmin(admin.ModelAdmin):
    list_display = ["membru", "get_vot_display", "decizie"]


admin.site.register(ActiuneDecizie, ActiuneDecizieAdmin)
admin.site.register(Decizie, DecizieAdmin)
