from django.forms import ModelChoiceField
from django.contrib import admin

from .models import *


class FlowersAdmin(admin.ModelAdmin):

    def formfield_for_freignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='flowers'))
        return super().formfield_for_freignkey(db_field, request, **kwargs)


class FlowersInPotsAdmin(admin.ModelAdmin):

    def formfield_for_freignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='flowersInPots'))
        return super().formfield_for_freignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Flowers, FlowersAdmin)
admin.site.register(FlowersInPots, FlowersInPotsAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)