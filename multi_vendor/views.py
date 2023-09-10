from django.http import HttpResponse
from django.shortcuts import render

from vendor.models import Vendor


def home(request):
    vendor = Vendor.objects.filter(is_approved=True, user__is_active=True)[:8]
    context = {
        "vendor": vendor,
    }
    return render(request, "index.html", context)
