import requests
from time import sleep
import datetime
from datetime import datetime, timedelta, date
import pandas as pd 
import os

api_key = os.environ['API_KEY']
base_url = "https://api.nytimes.com/svc/search/v2/articlesearch.json"

first_begin_date = datetime(2022, 1, 1)
begin_date = first_begin_date

all_articles = []

for two_week_interval in range(25):
    end_date = begin_date + timedelta(days=14)
    begin_date_formated = begin_date.strftime("%Y%m%d")
    end_date_formated = end_date.strftime("%Y%m%d")

    print(f"Retrieving articles between {begin_date_formated} and {end_date_formated}")

    
    page = 0
    more_items_in_collection = True 
    all_articles_query = []

    while more_items_in_collection:
        params = {
            "api-key": api_key,
            "q": "covid",
            "fq": 'headline:("Trump")',
            "begin_date": begin_date_formated,
            "end_date": end_date_formated,
            "sort": "oldest",
            "page": page
        }

        response = requests.get(base_url, params=params)
        articles = response.json()["response"]["docs"]
        hits = response.json()["response"]["meta"]["hits"]

        all_articles_query.extend(articles)
        all_articles.extend(articles)
        print(f"Page {page}: {len(all_articles_query)} out of {hits} articles retrieved. Total: {len(all_articles)}")

        if len(all_articles_query) < hits:
            page += 1
            sleep(2.0)

        else:
            more_items_in_collection = False

    begin_date += timedelta(days=15)
    sleep(2.0)

data = pd.json_normalize(all_articles)
data.to_csv('data.csv')