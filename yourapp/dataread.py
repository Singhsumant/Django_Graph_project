import csv
from matchapp.models import matchModel


csv_file_path = 'Data/matches.csv'

with open(csv_file_path, 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        matchModel.objects.create(
            season=row['season'],
            winner=row['winner'],
            
            # Add other fields as needed
        )