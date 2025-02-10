from django.db import models
from datetime import date

class Property(models.Model):
    RENT_MONTH_CHOICES = [
        ('farvardin', 'اجاره فروردین'),
        ('ordibehesht', 'اجاره اردیبهشت'),
        ('khordad', 'اجاره خرداد'),
        ('tir', 'اجاره تیر'),
        ('mordad', 'اجاره مرداد'),
        ('shahrivar', 'اجاره شهریور'),
        ('mehr', 'اجاره مهر'),
        ('aban', 'اجاره آبان'),
        ('azar', 'اجاره آذر'),
        ('dey', 'اجاره دی'),
        ('bahman', 'اجاره بهمن'),
        ('esfand', 'اجاره اسفند'),
    ]
    rent_month = models.CharField(max_length=15, choices=RENT_MONTH_CHOICES, blank=True, null=True)  # ماه اجاره
    # گزینه‌های کشویی
    SALE = 'sale'
    RENT = 'rent'
    PROPERTY_TYPES = [
        ('warehouse', 'سوله / سالن / خرپا'),
        ('office', 'اداری'),
        ('land', 'زمین / پارکینگ'),
        ('other', 'سایر'),
    ]

    AD_TYPES = [
        (SALE, 'فروش'),
        (RENT, 'اجاره'),
    ]

    # فیلدهای اصلی
    title = models.CharField(max_length=255, verbose_name="عنوان آگهی")  
    ad_type = models.CharField(max_length=10, choices=AD_TYPES, verbose_name="نوع آگهی")  
    property_type = models.CharField(max_length=20, choices=PROPERTY_TYPES, verbose_name="نوع ملک")  
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")  
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین ویرایش")
    description = models.TextField(blank=True)  # توضیحات ملک  
    available = models.BooleanField(default=True)  # تعیین فعال بودن ملک
    STATUS_CHOICES = [
        ('available', 'موجود'),
        ('rented', 'اجاره رفته'),
        ('sold', 'فروش رفته'),
        ('rent_cancelled', 'اجاره کنسل شده'),
        ('sale_cancelled', 'فروش کنسل شده'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')  # وضعیت ملک

    # متراژها (مقادیر عددی)
    land_size = models.PositiveIntegerField(null=True, blank=True, verbose_name="متراژ زمین")  
    warehouse_size = models.PositiveIntegerField(null=True, blank=True, verbose_name="متراژ سوله")  
    office_size = models.PositiveIntegerField(null=True, blank=True, verbose_name="متراژ اداری")  
    building_size = models.PositiveIntegerField(null=True, blank=True, verbose_name="متراژ بنا")  

    # قیمت‌ها
    total_price = models.CharField(max_length=50, null=True, blank=True, verbose_name="مبلغ کل")  
    price_per_meter = models.CharField(max_length=50, null=True, blank=True, verbose_name="مبلغ متری")  
    deposit = models.CharField(max_length=50, null=True, blank=True, verbose_name="ودیعه")  
    rent_price = models.CharField(max_length=50, null=True, blank=True, verbose_name="اجاره")  

    # امکانات و ویژگی‌ها (چک‌باکس)
    has_crane = models.BooleanField(default=False, verbose_name="جرثقیل")  
    has_stage = models.BooleanField(default=False, verbose_name="سکو")  
    has_100amp = models.BooleanField(default=False, verbose_name="برق تا ۱۰۰ آمپر")  
    has_200amp = models.BooleanField(default=False, verbose_name="برق تا ۲۰۰ آمپر")  
    has_400amp = models.BooleanField(default=False, verbose_name="برق بالای ۴۰۰ آمپر")  
    in_complex = models.BooleanField(default=False, verbose_name="در مجموعه/شهرکی")  
    independent = models.BooleanField(default=False, verbose_name="مستقل")  

    # ویژگی‌های برجسته (چک‌باکس)
    on_road = models.BooleanField(default=False, verbose_name="بر جاده")  
    showroom = models.BooleanField(default=False, verbose_name="شوروم")  
    pharmaceutical = models.BooleanField(default=False, verbose_name="دارویی")  
    special_property = models.BooleanField(default=False, verbose_name="ملک ویژه")  
    automotive = models.BooleanField(default=False, verbose_name="خودرویی / نمایندگی")  

    # محل (چک‌باکس‌ها)
    LOCATION_CHOICES = [
        ('ghods', 'قدس(قلعه حسن خان)/ زاگرس'),
        ('garmdareh', 'گرمدره'),
        ('mosallas', 'ابتدای مخصوص تا ایرانخودرو'),
        ('magspecial', 'مخصوص / ایرانخودرو تا وردآورد'),
        ('magwardavard', 'مخصوص/ وردآورد تا کرج'),
        ('fathstart', 'ابتدای فتح تا آزادگان'),
        ('azadwardavard', 'آزادگان تا وردآورد'),
        ('ahmadabad', 'احمدآباد مستوفی'),
        ('danesh', 'شهرک دانش'),
    ]
    location = models.CharField(max_length=50, choices=LOCATION_CHOICES, verbose_name="محل")  

    def str(self):
        return self.title
    
class PropertyImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='property_images/', blank=True, null=True, verbose_name="تصویر آگهی")

    def str(self):
        return f"تصویر مربوط به {self.property.title}"