from django.contrib.gis import admin


from .models import Campaign


class CampaignAdmin(admin.GeoModelAdmin):
    raw_id_fields = ("initial_ou",)


# Register your models here.
admin.site.register(Campaign, CampaignAdmin)
