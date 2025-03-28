from bokeh.plotting import figure, output_file, save
import pandas as pd

# Dummy data — replace this with your SF drug data later
data = {
    'year': [2015, 2016, 2017, 2018, 2019, 2020],
    'incidents': [1200, 1350, 1600, 1450, 1700, 900]
}
df = pd.DataFrame(data)

# Define where the output file goes
output_file("visualizations/output/chart1.html")

# Create the plot
p = figure(
    title="Drug-Related Incidents Over Time",
    x_axis_label='Year',
    y_axis_label='Number of Incidents',
    width=800,
    height=400  # ← changed from plot_width and plot_height
)


p.line(df['year'], df['incidents'], line_width=2, color='firebrick')
p.circle(df['year'], df['incidents'], size=8, color='navy')

# Save it
save(p)
