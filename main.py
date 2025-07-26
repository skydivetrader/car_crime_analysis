import os
from car_crime_analysis import fetch_crime_reports, analyze_trends, identify_hotspots, plot_trends, plot_hotspots

def main():
    # Retrieve API key from environment variable
    API_KEY = os.getenv('NEWS_API_KEY')
    if not API_KEY:
        raise ValueError("Missing NEWS_API_KEY environment variable")
    
    # Fetch data with caching
    df = fetch_crime_reports(api_key=API_KEY, filename='cached_news.csv', max_pages=1)

    # Check if data is available
    if df.empty:
        print("No data available. Please check your API quota or data source.")
        return

    # Analyze trends over time
    trend_df = analyze_trends(df)

    # Identify hotspots
    hotspot_df = identify_hotspots(df)

    # Visualize trend analysis
    plot_trends(trend_df)

    # Visualize hotspots
    plot_hotspots(hotspot_df)

if __name__ == "__main__":
    main()