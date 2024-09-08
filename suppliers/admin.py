from django.contrib import admin
from suppliers.models import Supplier


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """Отображение модели Supplier в админ-панели Django."""

    list_display = ('name', 'email', 'country', 'city', 'link', 'supplier', 'debit_arrears', 'created_at')
    list_filter = ('city',)
    search_fields = ('name', 'city',)
    actions = ['cleanup_debit_arrears']

    def cleanup_debit_arrears(self, request, queryset):
        """Очистка задолженности перед поставщиком у выбранных объектов."""

        queryset.update(debit_arrears=0.00)

    cleanup_debit_arrears.short_description = 'Очистить задолженность'