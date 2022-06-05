import datetime

import requests as req
import pandas as pd
from pymongo import MongoClient


URL = 'https://www.metaweather.com/api/location/2391279/'


def get_weather_data(url=URL):
    """
    Takes URL (url) and fetches weather data from metaweather.com.
    """
    response = req.get(url)
    json_data = response.json()
    days = json_data['consolidated_weather']

    df = pd.io.json.json_normalize(days[0])
    for day in days[1:]:
        df = df.append(pd.io.json.json_normalize(day))

    return df


def clean_df(df):
    """
    Cleans dataframe up by converting datetimes datatypes and dropping
    unnecessary columns.
    """
    # clean up df datatypes
    # Z means Zulu time, or GMT or UTC
    df['created'] = pd.to_datetime(df['created'], utc=True)
    df['applicable_date'] = pd.to_datetime(df['applicable_date']).dt.tz_localize('US/Mountain')

    # drop unneccesary columns
    df.drop(['weather_state_abbr', 'id'], inplace=True, axis=1)
    return df


def store_data(df):
    """
    Takes dataframe (df) and stores it in MongoDB.
    """
    client = MongoClient()
    db = client['weather_test']
    collection = db['denver']
    collection.insert_many(df.to_dict('records'))
    client.close()


def daily_scrape():
    """
    Scrapes data once per day at specified time.

    A better way to do this might be to check once per minute (or hour),
    and only scrape if the utc_time.hour hits a specified hour and it hasn't scraped
    yet that day.  A boolean variable could be used as a flag as to whether or
    not it has scraped that day, or a variable which stores the last scraped day
    from utc_time.day.

    Another way is to use crontab.  Running 'crontab -e' from the console allows
    editing of the crontab file, and files can be set to run there periodically.
    """
    while True:
        utc_time = datetime.datetime.utcnow()
        if utc_time.hour == 0 and utc_time.minute == 0 and utc_time.second == 0:
            df = get_weather_data()
            df = clean_df(df)
            store_data(df)
            time.sleep(1)  # sleep one second to ensure we don't double-scrape

        time.sleep(1)


if __name__ == "__main__":
    df = get_weather_data()
    df = clean_df(df)
    store_data(df)
