from django.contrib import admin

from .models import (
    Hero,
    AboutFarm,
    Product,
    Category,
    Gallery,
    About,
    Review,
    Contacts,
    SocialNetwork,
)


@admin.register(Product)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ["name", "image"]
    list_filter = ["name"]
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Hero)
admin.site.register(AboutFarm)
admin.site.register(Category)
admin.site.register(Gallery)
admin.site.register(About)
admin.site.register(Review)
admin.site.register(Contacts)
admin.site.register(SocialNetwork)
