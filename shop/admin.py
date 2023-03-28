from django.contrib import admin
from django.utils.safestring import mark_safe

from .models import Product, Manufacturer, Category, dollarRate


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'dollarRate', 'price',
                    'available', 'updated', 'category', 'manufacturer', 'hender', 'get_image', 'id']
    list_filter = ['available', 'created', 'updated']
    list_editable = ['price', 'available', 'hender']
    search_fields = ('name', 'manufacturer__name', 'category__name')
    radio_fields = {"dollarRate": admin.VERTICAL,
                    "manufacturer": admin.HORIZONTAL}
    fieldsets = (
        ('Автоматическое добавление', {
            'fields': ('hender', 'category', 'manufacturer', 'url', 'dollarRate')
        }),)
    actions = ['update_price', 'publish', 'unpublish']
    # actions = ['publish', 'unpublish']

    def get_image(self, obj):
        # return mark_safe(f'<img src="{obj.image_urs.image1}" width="100px" />'.format(obj.image_urs[0]))
        return mark_safe(f'<img src={obj.image_urs["image1"]} width="50px" height="50px"')

    get_image.short_description = 'Изображение'

    def update_price(self, request, queryset):
        """ Обновление цены товара """

        rows_updated = len(queryset)
        print(rows_updated)
        for item in queryset:
            item.update_product_price()
            item.save()
        # queryset.update
        if rows_updated == 1:
            message_bit = "1 товар был обновлен"
        else:
            message_bit = f"{rows_updated} товаров были обновлены".format(rows_updated)
        self.message_user(request, f"{message_bit}")

    update_price.short_description = "Обновить цену"

    def publish (self, request, queryset):
        """ Опубликовать товар """
        rows_updated = queryset.update(available=True)
        if rows_updated == 1:
            message_bit = "1 товар был опубликован"
        else:
            message_bit = f"{rows_updated} товаров были опубликованы".format(rows_updated)
        self.message_user(request, f"{message_bit}")

    publish.short_description = "Опубликовать товар"

    def unpublish (self, request, queryset):
        """ Снять с публикации товар """
        rows_updated = queryset.update(available=False)
        if rows_updated == 1:
            message_bit = "1 товар был снят с публикации"
        else:
            message_bit = f"{rows_updated} товаров были сняты с публикации".format(rows_updated)
        self.message_user(request, f"{message_bit}")

    unpublish.short_description = "Снять с публикации товар"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


@admin.register(dollarRate)
class DollarRateAdmin(admin.ModelAdmin):
    list_display = ['rate']


admin.site.site_title = 'Manifest Store Admin'
admin.site.site_header = 'Manifest Store Admin'
