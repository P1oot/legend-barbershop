from django.contrib import admin

from .models import Services, Haircuts, Promotions


@admin.register(Services)
class ServicesAdmin(admin.ModelAdmin):
    list_display = ['name', 'price']


@admin.register(Promotions)
class PromotionsAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Haircuts)
