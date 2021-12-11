from django.contrib import admin
from .models import navbar_items,background_hero,services,why_metro,customer_review,get_in_touch_items,footer_items
# Register your models here.
admin.site.register(navbar_items)
admin.site.register(background_hero)
admin.site.register(services)
admin.site.register(why_metro)
admin.site.register(customer_review)
admin.site.register(get_in_touch_items)
admin.site.register(footer_items)