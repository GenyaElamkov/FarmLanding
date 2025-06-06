from django.contrib import admin
from django.contrib.admin import AdminSite
from django.utils.translation import gettext_lazy as _
from django.utils.safestring import mark_safe
from import_export import resources
from import_export.admin import ImportExportModelAdmin

from django_summernote.admin import SummernoteModelAdmin

from .models import *


# Настройка заголовков админки
AdminSite.site_title = _('Админка Эко Фермы "Солнечная"')
AdminSite.site_header = _('Администрация Эко Фермы "Солнечная"')
AdminSite.index_title = _("Управление контентом")

admin.site.site_header = 'Панель управления Эко Фермы "Солнечная"'
admin.site.site_title = 'Эко Ферма "Солнечная"'
admin.site.index_title = 'Администрирование сайта'

# Ресурсы для импорта/экспорта
class ProductResource(resources.ModelResource):
    class Meta:
        model = Product
        fields = ("id", "name", "slug", "description", "category__name", "featured")


class GalleryResource(resources.ModelResource):
    class Meta:
        model = Gallery
        fields = ("id", "name")


# Кастомизированные классы админки
class ProductAdmin(ImportExportModelAdmin, SummernoteModelAdmin):
    resource_class = ProductResource
    list_display = ("name", "category", "featured", "image_preview")
    list_filter = ("category", "featured")
    search_fields = ("name", "description")
    list_editable = ("featured",)
    prepopulated_fields = {"slug": ("name",)}
    readonly_fields = ("image_preview",)

    summernote_fields = ('description',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px;" />')
        return "-"

    image_preview.short_description = "Превью"


class GalleryAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = GalleryResource
    list_display = ("name", "image_preview")
    search_fields = ("name",)
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px;" />')
        return "-"

    image_preview.short_description = "Превью"


class ReviewAdmin(SummernoteModelAdmin):
    list_display = ("name", "rating", "image_preview")
    list_filter = ("rating",)
    search_fields = ("name", "description")
    readonly_fields = ("image_preview",)
    summernote_fields = ('description',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px;" />')
        return "-"

    image_preview.short_description = "Превью"


class AboutAdmin(SummernoteModelAdmin):
    list_display = ("title", "image_preview")
    readonly_fields = ("image_preview",)
    summernote_fields = ('description',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px;" />')
        return "-"

    image_preview.short_description = "Превью"


class HeroAdmin(SummernoteModelAdmin):
    list_display = ("title", "image_preview")
    readonly_fields = ("image_preview",)
    summernote_fields = ('description',)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}" style="max-height: 50px;" />')
        return "-"

    image_preview.short_description = "Превью"


class ContactsAdmin(admin.ModelAdmin):
    list_display = ("address", "phone", "email")
    search_fields = ("address", "phone", "email")


class SocialNetworkAdmin(admin.ModelAdmin):
    list_display = ("name", "base_url", "icon_class")
    search_fields = ("name", "base_url")


class AboutFarmAdmin(SummernoteModelAdmin):
    list_display = ("title", "icon_class")
    search_fields = ("title", "description")
    summernote_fields = ('description',)

# Регистрация моделей
admin.site.register(Category, admin.ModelAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Gallery, GalleryAdmin)
admin.site.register(About, AboutAdmin)
admin.site.register(Review, ReviewAdmin)
admin.site.register(Hero, HeroAdmin)
admin.site.register(AboutFarm, AboutFarmAdmin)
admin.site.register(Contacts, ContactsAdmin)
admin.site.register(SocialNetwork, SocialNetworkAdmin)
