from django.contrib import admin

from shop.models import Contact, Product, Organization

admin.site.register(Contact)
admin.site.register(Product)


@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
	list_display = [f.name for f in Organization._meta.fields]
