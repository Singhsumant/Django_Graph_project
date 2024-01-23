
from django.http import HttpResponse
from django.shortcuts import render
from django.db.models import Count
from .models import matchModel
from collections import defaultdict

def homepage(request):
    return render(request,'matchapp/homepage.html')

def match1(request):
    season_counts = matchModel.objects.values('season').annotate(count=Count('season'))
    season_count_dict = {entry['season']: entry['count'] for entry in season_counts}
    return render(request,'matchapp/match1.html',{'season_count_dict':season_count_dict})

from django.db.models import Count
from collections import defaultdict

def match2(request):
    # Query to get the count of matches won by each winner for each season
    season_winner_counts = matchModel.objects.values('season', 'winner').annotate(count=Count('winner'))

    # Create a nested dictionary to store the count of matches won by each winner for each season
    season_winner_dict = defaultdict(dict)

    # Populate the nested dictionary
    for entry in season_winner_counts:
        season = entry['season']
        winner = entry['winner']
        count = entry['count']

        season_winner_dict[season][winner] = count
        
   

    return render(request, 'matchapp/match2.html', {'season_winner_dict': dict(season_winner_dict)})
 