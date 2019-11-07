import pandas as pd

data = pd.read_csv("20171013111831-SurveyExport.csv", delimiter = ',', encoding = "iso-8859-1")

countries = set(data["Country"])
responses = data["Response ID"]

for country in countries:
    if country != 'nan':
        print(data[country].count())
