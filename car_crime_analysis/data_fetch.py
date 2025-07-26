import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_crime_reports(api_key, years=5, max_pages=5):
    today = datetime.now()
    start_date = today - timedelta(days=years*365)
    from_date = start_date.strftime('%Y-%m-%d')
    to_date = today.strftime('%Y-%m-%d')

    keywords = [
        "car theft",
        "vehicle theft",
        "auto theft",
        "carjacking",
        "shipping cars overseas",
        "exporting vehicles",
        "vehicle smuggling",
        "organized crime",
        "trafficking cars",
        "car trafficking"
    ]

    query = ' OR '.join(keywords) + ' AND Canada -juvenile -youth -teen -minor'

    all_articles = []

    for page in range(1, max_pages + 1):
        params = {
            'q': f'({query})',
            'from': from_date,
            'to': to_date,
            'sortBy': 'relevance',
            'language': 'en',
            'pageSize': 100,
            'page': page,
            'apiKey': api_key
        }
        response = requests.get('https://newsapi.org/v2/everything', params=params)
        if response.status_code != 200:
            print(f"Error fetching page {page}: {response.status_code}")
            continue
        data = response.json()
        articles = data.get('articles', [])
        if not articles:
            break
        for art in articles:
            all_articles.append({
                'title': art['title'],
                'published_at': art['publishedAt'],
                'source': art['source']['name'],
                'url': art['url'],
                'description': art['description']
            })

    df = pd.DataFrame(all_articles)
    return df