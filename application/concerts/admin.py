from django.contrib import admin

from application.concerts.models import Concert


class ConcertAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Concert._meta.fields]

    class Meta:
        model = Concert


admin.site.register(Concert, ConcertAdmin)