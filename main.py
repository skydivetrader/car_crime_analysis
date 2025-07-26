from car_crime_analysis import fetch_crime_reports, analyze_trends, identify_hotspots, plot_trends, plot_hotspots

# Retrieve API key from environment variable
import os
API_KEY = os.getenv('NEWS_API_KEY')
if not API_KEY:
    raise ValueError("Missing NEWS_API_KEY environment variable")

# Fetch reports with caching
# You can specify a filename for cache, e.g., 'cached_news.csv'
df = fetch_crime_reports(api_key=API_KEY, filename='cached_news.csv')

# Check if data is fetched
if df.empty:
    print("No data available. Please check your API quota or data source.")
    exit(1)

# Proceed with analysis
trend_df = analyze_trends(df)
hotspot_df = identify_hotspots(df)

# Visualize results
plot_trends(trend_df)
plot_hotspots(hotspot_df)