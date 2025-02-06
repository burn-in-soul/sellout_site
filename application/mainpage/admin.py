from django.contrib import admin

from application.mainpage.models import MainpageImages


class MainpageImagesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in MainpageImages._meta.fields]

    class Meta:
        model = MainpageImages


admin.site.register(MainpageImages, MainpageImagesAdmin)