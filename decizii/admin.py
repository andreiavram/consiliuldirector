from django.contrib import admin

from decizii.models import Registru, IntrareRegistru, MembruConsiliulDirector, Decizie, ConsiliulDirector

admin.site.register(ConsiliulDirector)
admin.site.register(Registru)
admin.site.register(IntrareRegistru)
admin.site.register(MembruConsiliulDirector)
admin.site.register(Decizie)
