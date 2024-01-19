from django.contrib import admin, messages
from django.urls import reverse
from django.utils.html import format_html
from django.utils.translation import ngettext

from shop.models import Contact, Product, Organization

admin.site.register(Contact)
admin.site.register(Product)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
	exclude = ('hierarchy_level',)
	list_display = (
		'name', 'contacts', 'supplier_link', 'organization_type', 'hierarchy_level', 'debt', 'created_time',
	)
	list_filter = ('contacts__city',)
	actions = ('clear_debt',)

	def supplier_link(self, obj):
		"""
		Возвращает ссылку на объект поставщика.
		"""
		if not obj.supplier:
			return None
		else:
			url = reverse('admin:shop_organization_change', args=[obj.supplier.id])
			return format_html("<a href='{}'>{}</a>", url, obj.supplier)

	supplier_link.short_description = "Поставщик"

	def clear_debt(self, request, queryset):
		"""
		Admin-action для очистки задолженности перед поставщиком у выбранных объектов
		"""
		updated = queryset.update(debt=0)
		self.message_user(
			request,
			ngettext(
				"%d debt was successfully cleared.",
				"%d debts were successfully cleared.",
				updated,
			)
			% updated,
			messages.SUCCESS,
		)

	clear_debt.short_description = "Clear debt for selected organizations"
