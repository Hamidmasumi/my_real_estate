from django.shortcuts import render
from .models import Property
from django.db import models
from django.db.models import Q

def index(request):
    
    # دیکشنری تبدیل نام‌های انگلیسی به فارسی از مدل
    location_dict = dict(Property.LOCATION_CHOICES)
    
    # دریافت لیست املاک فعال
    properties = Property.objects.filter(available=True)

    # دریافت فقط املاک ویژه برای اسلایدر
    special_properties = Property.objects.filter(special_property=True)

    # دریافت مناطق (بدون تکرار) و تبدیل به فارسی
    locations = list(Property.objects.values_list('location', flat=True).distinct())
    locations = [(loc, location_dict.get(loc, loc)) for loc in locations]  # تبدیل کلید به مقدار فارسی

    # دریافت فیلدهای BooleanField از مدل Property
    facility_fields = [
        field for field in Property._meta.fields
        if isinstance(field, models.BooleanField)
    ]

    # تبدیل به دیکشنری {نام فیلد: عنوان فارسی}
    facilities = {field.name: field.verbose_name for field in facility_fields}

    # دریافت مقدار فیلترها از request.GET
    ad_type = request.GET.get('ad_type')
    property_type = request.GET.get('property_type')
    land_size_min = request.GET.get('land_size_min')
    land_size_max = request.GET.get('land_size_max')
    warehouse_size_min = request.GET.get('warehouse_size_min')
    warehouse_size_max = request.GET.get('warehouse_size_max')
    office_size_min = request.GET.get('office_size_min')
    office_size_max = request.GET.get('office_size_max')
    building_size_min = request.GET.get('building_size_min')
    building_size_max = request.GET.get('building_size_max')
    total_price_min = request.GET.get('total_price_min')
    total_price_max = request.GET.get('total_price_max')
    deposit_min = request.GET.get('deposit_min')
    deposit_max = request.GET.get('deposit_max')
    rent_min = request.GET.get('rent_min')
    rent_max = request.GET.get('rent_max')
    selected_facilities = request.GET.getlist('facilities')  # لیست امکانات انتخاب‌شده
    selected_locations = request.GET.getlist('location')  # لیست مناطق انتخاب‌شده

    # اعمال فیلترها
    if ad_type:
        properties = properties.filter(ad_type=ad_type)
    if property_type:
        properties = properties.filter(property_type=property_type)
    if land_size_min:
        properties = properties.filter(land_size__gte=land_size_min)
    if land_size_max:
        properties = properties.filter(land_size__lte=land_size_max)
    if warehouse_size_min:
        properties = properties.filter(warehouse_size__gte=warehouse_size_min)
    if warehouse_size_max:
        properties = properties.filter(warehouse_size__lte=warehouse_size_max)
    if office_size_min:
        properties = properties.filter(office_size__gte=office_size_min)
    if office_size_max:
        properties = properties.filter(office_size__lte=office_size_max)
    if building_size_min:
        properties = properties.filter(building_size__gte=building_size_min)
    if building_size_max:
        properties = properties.filter(building_size__lte=building_size_max)
    if total_price_min:
        properties = properties.filter(total_price__gte=total_price_min)
    if total_price_max:
        properties = properties.filter(total_price__lte=total_price_max)
    if deposit_min:
        properties = properties.filter(deposit__gte=deposit_min)
    if deposit_max:
        properties = properties.filter(deposit__lte=deposit_max)
    if rent_min:
        properties = properties.filter(rent__gte=rent_min)
    if rent_max:
        properties = properties.filter(rent__lte=rent_max)

    # فیلتر کردن املاک بر اساس امکانات انتخاب‌شده
    if selected_facilities:
        facility_filter = Q()
        for facility in selected_facilities:
            if facility in facilities:  # بررسی وجود این فیلد در مدل
                facility_filter |= Q(**{facility: True})  # شرط OR برای هر گزینه

    # فیلتر محل (چک‌باکس OR)
    if selected_locations:
        properties = properties.filter(location__in=selected_locations)
    # اضافه کردن امکانات به هر ملک
    for property in properties:
        property.facilities = []
        if property.has_crane:
            property.facilities.append('جرثقیل')
        if property.has_stage:
            property.facilities.append('سکو')
        if property.has_100amp:
            property.facilities.append('برق تا ۱۰۰ آمپر')
        if property.has_200amp:
            property.facilities.append('برق تا ۲۰۰ آمپر')
        if property.has_400amp:
            property.facilities.append('برق بالای ۴۰۰ آمپر')
        if property.in_complex:
            property.facilities.append('در مجموعه/شهرکی')
        if property.independent:
            property.facilities.append('مستقل')
        if property.on_road:
            property.facilities.append('بر جاده')
        if property.showroom:
            property.facilities.append('شوروم')
        if property.pharmaceutical:
            property.facilities.append('دارویی')
        if property.special_property:
            property.facilities.append('ملک ویژه')
        if property.automotive:
            property.facilities.append('خودرویی / نمایندگی')

    # ارسال داده به قالب
    context = {
        'properties': properties,
        'special_properties': special_properties,  # املاک ویژه برای اسلایدر
        'locations': locations,  # حالا شامل کلید و مقدار فارسی است
        'facilities': facilities,
        'AD_TYPES': Property.AD_TYPES,
        'PROPERTY_TYPES': Property.PROPERTY_TYPES,
    }
    return render(request, 'real_estate_website/index.html', context)