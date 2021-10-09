import json,csv

with open('covid_cases.json','r') as file_json:
    covid_data=json.load(file_json)

with open('covid_cases.csv','w') as covid_csv:
    data=csv.writer(covid_csv)
    data.writerow(['dateRep','countriesAndTerritories','cases','deaths'])#column names

    for data_parsing in covid_data['records']:
        data.writerow([data_parsing['dateRep'],data_parsing['countriesAndTerritories'],data_parsing['cases'],data_parsing['deaths']])#data