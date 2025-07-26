import os
import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_crime_reports(api_key, years=5, max_pages=1, filename='cached_news.csv'):
    # If cache exists, load and return
    if os.path.exists(filename):
        print(f"Loading cached data from {filename}")
        return pd.read_csv(filename)

    # Otherwise, fetch data from API
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

    headers = {
        'User-Agent': 'Mozilla/5.0 (compatible; CarCrimeAnalysis/1.0)'
    }

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
        print(f"Fetching page {page} with params: {params}")
        response = requests.get('https://newsapi.org/v2/everything', headers=headers, params=params)
        print(f"Response status: {response.status_code}")

        if response.status_code != 200:
            print(f"Error fetching page {page}: {response.status_code}")
            break

        data = response.json()

        articles = data.get('articles', [])
        if not articles:
            print(f"No articles found on page {page}.")
            break

        for art in articles:
            all_articles.append({
                'title': art['title'],
                'published_at': art['publishedAt'],
                'source': art['source']['name'],
                'url': art['url'],
                'description': art['description']
            })

    # Convert to DataFrame
    df = pd.DataFrame(all_articles)

    # Save to CSV for caching
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

    return df