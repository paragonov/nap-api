from django.contrib import admin
from .models import News, Positions, Insites, Trends


class NewsAdmin(admin.ModelAdmin):
    fields = ('title', 'date', 'positions')


class PositionsAdmin(admin.ModelAdmin):
    fields = ('name', 'slug',)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(NewsAdmin)
admin.site.register(PositionsAdmin)
admin.site.register(Insites)
admin.site.register(Trends)
