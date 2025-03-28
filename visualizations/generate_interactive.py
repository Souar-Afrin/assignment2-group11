import pandas as pd
from bokeh.plotting import figure, output_file, save
from bokeh.layouts import column
from bokeh.models import ColumnDataSource, Select, CustomJS
from bokeh.embed import components

# Example data (replace this with SF crime data)
data = {
    'year': [2019, 2019, 2020, 2020, 2021, 2021],
    'lat': [37.77, 37.78, 37.76, 37.75, 37.74, 37.79],
    'lon': [-122.41, -122.42, -122.43, -122.44, -122.45, -122.46],
    'desc': ['Crime A', 'Crime B', 'Crime C', 'Crime D', 'Crime E', 'Crime F']
}
df = pd.DataFrame(data)

years = sorted(df['year'].unique())
initial_year = years[0]

# Filter for initial year
df_year = df[df['year'] == initial_year]
source = ColumnDataSource(data=dict(lat=df_year['lat'], lon=df_year['lon'], desc=df_year['desc']))

# Create plot
p = figure(title="Crime Locations by Year", x_axis_label="Longitude", y_axis_label="Latitude", width=800, height=400)
p.circle(x='lon', y='lat', size=10, fill_color="orange", source=source)

# Year dropdown
dropdown = Select(title="Select Year:", value=str(initial_year), options=[str(y) for y in years])

# Add interactivity via JavaScript callback
callback = CustomJS(args=dict(source=source, full_data=df.to_dict(orient='list'), dropdown=dropdown), code="""
    const data = source.data;
    const year = parseInt(dropdown.value);
    const full = full_data;

    data['lat'] = [];
    data['lon'] = [];
    data['desc'] = [];

    for (let i = 0; i < full['year'].length; i++) {
        if (full['year'][i] === year) {
            data['lat'].push(full['lat'][i]);
            data['lon'].push(full['lon'][i]);
            data['desc'].push(full['desc'][i]);
        }
    }
    source.change.emit();
""")

dropdown.js_on_change('value', callback)

# Save output
layout = column(dropdown, p)
output_file("visualizations/output/interactive_plot.html")
save(layout)
