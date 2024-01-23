from django.shortcuts import render
from django.http import HttpResponse
from yourapp.models import schoolModel
from django.db.models import Count




def selectQuestion(request):
    return render(request,'yourapp/select.html')

def homepage(request):
    return render(request,'yourapp/homepage.html')

def school1(request):
    unique_districts_data = schoolModel.objects.values('district_name').annotate(count=Count('district_name'))
    district_count_dict = {entry['district_name']: entry['count'] for entry in unique_districts_data}

    
    return render(request,'yourapp/school1.html',{"district_count_dict":district_count_dict})

def school2(request):
    district_category_counts = schoolModel.objects.values('district_name', 'category') \
        .annotate(count=Count('category'))

   
    district_category_dict = {}
    for entry in district_category_counts:
        district_name = entry['district_name']
        category = entry['category']
        count = entry['count']

        if district_name not in district_category_dict:
            district_category_dict[district_name] = {}

        district_category_dict[district_name][category] = count
    
    return render(request, 'yourapp/school2.html', {'district_category_dict': district_category_dict})

from django.shortcuts import render
from .models import schoolModel

def school3(request):
    district_languages = schoolModel.objects.values('district_name', 'language').distinct()

    district_language_dict = {}
    for entry in district_languages:
        district_name = entry['district_name']
        language = entry['language']

        if district_name not in district_language_dict:
            district_language_dict[district_name] = []

        district_language_dict[district_name].append(language)

    return render(request, 'yourapp/school3.html', {'district_language_dict': district_language_dict})

