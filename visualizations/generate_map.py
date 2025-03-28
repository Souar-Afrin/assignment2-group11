import folium
from folium.plugins import HeatMap

# Example dummy coordinates — replace with your data
data = [
    [37.7749, -122.4194],  # SF center
    [37.7750, -122.4193],
    [37.7751, -122.4192],
    [37.7752, -122.4191],
]

# Create a base map
m = folium.Map(location=[37.7749, -122.4194], zoom_start=13)

# Add heatmap layer
HeatMap(data).add_to(m)

# Save map to HTML
m.save('visualizations/output/map1.html')
