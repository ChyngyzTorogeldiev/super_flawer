from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin

from .models import *


class FlowerInPotAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and not instance.sd:
            self.fields['sd_volume_max'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgray;'
            })

    def clean(self):
        if not self.cleaned_data['sd']:
            self.cleaned_data['sd_volume_max'] = None
        return self.cleaned_data


class FlowerAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='flower'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class FlowerInPotAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = FlowerInPotAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='flowerInPot'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Flower, FlowerAdmin)
admin.site.register(FlowerInPot, FlowerInPotAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)