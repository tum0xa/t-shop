from django.shortcuts import render
from django.views.generic import TemplateView
from contacts.models import Company
from catalog.models import Category

class Home(TemplateView):
    template_name = 'home/index.html'
    try:
        contacts = Company.objects.get(pk=0)
    except Exception:
        contacts = Company(name = "Dummy")
    shop = contacts
    catalog = Category.objects.filter(active=True)
    extra_context = {
                    'shop': shop,
                    'contacts': contacts,
                    'catalog': catalog,
    }
