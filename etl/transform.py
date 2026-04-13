"""
Transforms raw Spotify data into a clean DataFrame.

Args:
    raw_data: Dictionary containing the raw data from the Spotify API.

Returns:
    DataFrame with transformed data or None if an error occurs (duplicate data or null values are found (maintaining your original logic).
"""
import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', 25)
pd.set_option('display.float_format', '{:.2f}'.format)

def transform(raw_data):
    data = []
    for r in raw_data["items"]:
        data.append({
            "played_at": r["played_at"],
            "artist": r["track"]["artists"][0]["name"],
            "track": r["track"]["name"],
            "url": r["track"]["album"]["artists"][0]["external_urls"]["spotify"],
        })
    df = pd.DataFrame(data)

    if not df["played_at"].is_unique:
        raise Exception("The list contains duplicate values")

    if df.isnull().values.any():
        raise Exception("The list contains null values")

    return df