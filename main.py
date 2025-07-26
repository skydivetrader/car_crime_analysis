from car_crime_analysis import fetch_crime_reports, analyze_trends, identify_hotspots, plot_trends, plot_hotspots

API_KEY = 'YOUR_NEWSAPI_KEY'  # <-- Replace with your API key

# Fetch reports
df = fetch_crime_reports(api_key=API_KEY)

# Save raw data
df.to_csv('car_crime_reports.csv', index=False)

# Analyze
trend_df = analyze_trends(df)
hotspot_df = identify_hotspots(df)

# Visualize
plot_trends(trend_df)
plot_hotspots(hotspot_df)