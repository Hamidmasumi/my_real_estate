# Generated by Django 5.1.6 on 2025-02-09 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('real_estate_website', '0004_property_updated_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='property',
            name='available',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='property',
            name='rent_month',
            field=models.CharField(blank=True, choices=[('farvardin', 'اجاره فروردین'), ('ordibehesht', 'اجاره اردیبهشت'), ('khordad', 'اجاره خرداد'), ('tir', 'اجاره تیر'), ('mordad', 'اجاره مرداد'), ('shahrivar', 'اجاره شهریور'), ('mehr', 'اجاره مهر'), ('aban', 'اجاره آبان'), ('azar', 'اجاره آذر'), ('dey', 'اجاره دی'), ('bahman', 'اجاره بهمن'), ('esfand', 'اجاره اسفند')], max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='property',
            name='status',
            field=models.CharField(choices=[('available', 'موجود'), ('rented', 'اجاره رفته'), ('sold', 'فروش رفته'), ('rent_cancelled', 'اجاره کنسل شده'), ('sale_cancelled', 'فروش کنسل شده')], default='available', max_length=20),
        ),
    ]
