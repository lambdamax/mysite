from django.contrib import admin

from . import models


# Register your models here.


class Tagsinline(admin.TabularInline):
    model = models.Articleship
    extra = 1


@admin.register(models.Articles)
class ArticlesAdmin(admin.ModelAdmin):
    empty_value_display = '-empty-'
    list_display = ('name', 'create_date', 'create_user',)
    search_fields = ('name',)
    inlines = [Tagsinline]
    fieldsets = (
        (None, {
            'fields': ('name', 'body', 'photo', 'catalog', 'recommand', 'active', 'order_id',)
        }),
        ('Advanced options', {
            'classes': ('collapse',),
            'fields': ('create_user', 'write_user'),
        }),
    )


# admin.site.register(models.Articles)

admin.site.register(models.Catalog)
admin.site.register(models.User)
# admin.site.register(models.Role)
admin.site.register(models.Comment)
admin.site.register(models.Link)
admin.site.register(models.SinaFutures)
admin.site.register(models.SinaStock)
