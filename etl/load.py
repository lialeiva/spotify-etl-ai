"""
Load the transformed data into the spotify_recently_playlist table.

Args:
    df: DataFrame containing the data to be loaded (must include columns: played_at, artist, track, url).

Returns:
    bool: True if the load was successful, False if an error occurred (the DataFrame is empty or does not have the required columns).

"""

from sqlalchemy import create_engine, MetaData, Table
from db.createTable import create_table_spotify_recently_playlist
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.exc import SQLAlchemyError
from cfg import DB_CONNSTR

def load(df):
    engine = None
    try:
        create_table_spotify_recently_playlist()

        engine = create_engine(DB_CONNSTR)
        metadata = MetaData()
        table = Table("spotify_recently_playlist", metadata, autoload_with=engine)

        data = df.to_dict(orient="records")
        stmt = insert(table).values(data)
        stmt = stmt.on_conflict_do_nothing(index_elements=["played_at"])

        with engine.begin() as conn:
            conn.execute(stmt)

        print(f"   ✅ Loaded {len(data)} registers")
        return True

    except SQLAlchemyError as e:
        print(f"   ❌ Error: {e}")
        return False
    finally:
        if engine:
            engine.dispose()