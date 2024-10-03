import plotly.express as px
import geopandas as gpd

# geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_cities'))

px.set_mapbox_access_token(open("pk.eyJ1Ijoic3NrdXNzZXYiLCJhIjoiY2xmaDA4b3VkMDRodzNxcXB0aDZ0Yjh2NiJ9.sgsihyX2LXp_oqxLxPcugQ").read())
df = px.data.carshare()
fig = px.scatter_mapbox(df, lat="55.709226", lon="37.580005",     color="peak_hour", size="car_hours",
                  color_continuous_scale=px.colors.cyclical.IceFire, size_max=15, zoom=10)
fig.show()

# 55.709226, 37.580005