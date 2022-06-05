"""
This creates a test database for the api to serve.  It uses the scrape_weather.py file within the same directory.
"""
import scrape_weather as sw

df = sw.get_weather_data()
df = sw.clean_df(df)
sw.store_data(df)
