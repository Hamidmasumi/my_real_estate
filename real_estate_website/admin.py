from django.contrib import admin
from .models import Property, PropertyImage

class PropertyImageInline(admin.TabularInline):
    model = PropertyImage
    extra = 1

@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ('title', 'ad_type', 'property_type', 'location', 'created_at', 'description', 'status', 'available')  
    list_filter = ('ad_type', 'property_type', 'location', 'created_at', 'status', 'available', 'rent_month')  # اضافه شدن rent_month
    search_fields = ('title', 'location')  
    inlines = [PropertyImageInline]

admin.site.register(PropertyImage)