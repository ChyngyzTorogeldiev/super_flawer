from PIL import Image
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class FlowerAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """<span style="color: red; font-size: 14px;">При загруске изображения с разрешением больше {}x{} оно будет обрезано!</span>
            """.format(
                *Product.MIN_RESOLUTION
            )
        )

    def clean_image(self):
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_height, min_width = Product.MIN_RESOLUTION
        max_height, max_width = Product.MAX_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationErro('Размер изображения не должен превышать 3MB!')
        if img.height < min_height or img.width < min_width:
            raise ValidationError('Разрешение изображения меньше минимального!')
        if img.height > max_height or img.width > max_width:
            raise ValidationError('Разрешение изображения больше максимального!')
        return image

class FlowerAdmin(admin.ModelAdmin):

    form = FlowerAdminForm

    def formfield_for_freignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='flower'))
        return super().formfield_for_freignkey(db_field, request, **kwargs)


class FlowerInPotAdmin(admin.ModelAdmin):

    form = FlowerAdminForm

    def formfield_for_freignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='flowerInPot'))
        return super().formfield_for_freignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Flower, FlowerAdmin)
admin.site.register(FlowerInPot, FlowerInPotAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)