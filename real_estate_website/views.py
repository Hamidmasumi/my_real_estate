from django.shortcuts import render
from .models import Property

def index(request):
    properties = Property.objects.filter(available=True)  # فقط املاک فعال را نمایش بده
    return render(request, 'real_estate_website/index.html', {'properties': properties})