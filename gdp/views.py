from django.shortcuts import render
from django.views.generic import View
from .models import CGDP


class ListCountries(View):
    def get(self, request):
        top_countries = CGDP.objects.all().order_by('value')[:20]
        bottom_countries = CGDP.objects.all().order_by('-value')[:20]
        years = CGDP.objects.all().order_by('-year').values_list('year',flat=True).distinct()
        return render(request, 'list_countries.html', context={'top_countries': top_countries, 'bottom_countries': bottom_countries,'years':years})