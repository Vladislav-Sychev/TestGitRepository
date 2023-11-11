from django.contrib import admin
from .models import Hall, Exhibit, Collection


class ExhibitAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'value', 'century', 'collection', 'height', 'width', 'length', 'temperature_control', 'humidity_control', 'protection')
    list_filter = ('collection', 'century', 'temperature_control', 'humidity_control', 'protection')
    search_fields = ('name', 'description')




class ExhibitInline(admin.TabularInline):
    model = Exhibit
    fields = ('name', 'description', 'value', 'century', 'height', 'width', 'length', 'temperature_control', 'humidity_control', 'protection')
    extra = 0

# Создаем класс для настройки отображения модели Collection
class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'hall', 'start_date', 'end_date')
    list_filter = ('hall', 'start_date', 'end_date')
    search_fields = ('name', 'description')
    inlines = [ExhibitInline]


admin.site.register(Hall)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Exhibit, ExhibitAdmin)









