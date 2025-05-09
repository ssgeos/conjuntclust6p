import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime, timedelta

# Define the clusters and their time windows (-3 to +5 days)
clusters = [
    # Cluster 1: 2000-05-08 to 2000-05-09
    (datetime(2000, 5, 8), datetime(2000, 5, 9)),
    # Cluster 2: 2003-08-20 to 2003-08-22
    (datetime(2003, 8, 20), datetime(2003, 8, 22)),
    # Cluster 3: 2007-08-13 to 2007-08-15
    (datetime(2007, 8, 13), datetime(2007, 8, 15)),
    # Cluster 4: 2010-03-07 to 2010-03-09
    (datetime(2010, 3, 7), datetime(2010, 3, 9)),
    # Cluster 5: 2010-06-08 to 2010-06-09
    (datetime(2010, 6, 8), datetime(2010, 6, 9)),
    # Cluster 6: 2019-07-08 to 2019-07-09
    (datetime(2019, 7, 8), datetime(2019, 7, 9)),
]

# Define the earthquakes: (date, magnitude)
earthquakes = [
    # Cluster 1
    (datetime(2000, 5, 12), 7.2),
    # Cluster 2
    (datetime(2003, 8, 21), 7.2),
    # Cluster 3
    (datetime(2007, 8, 15), 8.0),
    # Cluster 4
    (datetime(2010, 3, 11), 7.0),
    # Cluster 5
    (datetime(2010, 6, 12), 7.5),
    # Cluster 6
    (datetime(2019, 7, 6), 7.1),
    (datetime(2019, 7, 7), 6.9),
    (datetime(2019, 7, 14), 7.2),
]

# Create the plot
plt.figure(figsize=(12, 6))

# Plot the time windows as red bars (using axvspan for the -3 to +5 day windows)
for start, end in clusters:
    window_start = start - timedelta(days=3)
    window_end = end + timedelta(days=5)
    plt.axvspan(window_start, window_end, color='red', alpha=0.3, linestyle='--', edgecolor='gray')

# Plot the earthquakes as blue dots
earthquake_dates = [eq[0] for eq in earthquakes]
earthquake_magnitudes = [eq[1] for eq in earthquakes]
plt.scatter(earthquake_dates, earthquake_magnitudes, color='blue', label='Earthquakes')

# Add magnitude labels to the points
for i, (date, mag) in enumerate(earthquakes):
    plt.text(date, mag + 0.05, f'M{mag}', fontsize=8, ha='center')

# Customize the plot
plt.title('Major Earthquakes (M≥6.9) Around Planetary Conjunction Clusters\n(Gray bars: conjunction clusters, Blue dots: earthquakes)')
plt.xlabel('Date')
plt.ylabel('Earthquake Magnitude')
plt.ylim(6.5, 8.5)  # Set y-axis range to match the provided plot
plt.grid(True, which='both', linestyle='--', alpha=0.7)

# Format the x-axis with dates
plt.gca().xaxis.set_major_locator(mdates.YearLocator())
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.xticks(rotation=45)

# Add legend
plt.legend()

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Show the plot
plt.show()
