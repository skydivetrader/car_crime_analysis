import matplotlib.pyplot as plt

def plot_trends(trend_df):
    plt.figure(figsize=(12,6))
    plt.plot(trend_df['Month'].astype(str), trend_df['Count'], marker='o')
    plt.title('Car Crime & Organized Crime Reports Over Time')
    plt.xlabel('Month')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def plot_hotspots(hotspot_df):
    plt.figure(figsize=(10,6))
    plt.bar(hotspot_df['Source'], hotspot_df['Articles'], color='skyblue')
    plt.title('Articles per News Source')
    plt.xlabel('Source')
    plt.ylabel('Number of Articles')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()