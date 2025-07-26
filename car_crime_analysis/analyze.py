import pandas as pd

def analyze_trends(df):
    df['published_at'] = pd.to_datetime(df['published_at'])
    df['month'] = df['published_at'].dt.to_period('M')
    trend = df['month'].value_counts().sort_index()
    trend_df = trend.reset_index()
    trend_df.columns = ['Month', 'Count']
    return trend_df

def identify_hotspots(df, location_column='source'):
    counts = df[location_column].value_counts()
    return counts.reset_index().rename(columns={'index': 'Source', 'source': 'Articles'})