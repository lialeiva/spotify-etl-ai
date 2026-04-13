"""
Extract recently played tracks from Spotify.

Args:
    date: The date from which to retrieve plays (None = most recent).
    limit: Number of tracks to retrieve (1-50).

Returns:
    List of tracks or None if an error occurs.
"""
from datetime import datetime

from connection.spotifyAPIConnection import spotify_connection


sp = spotify_connection()

def extract_recent_playlist(date: datetime, limit: int = 50):
    if sp is None:
        print("❌ Error: Could not establish a connection to Spotify")
        return None

    try:
        ds = int(date.timestamp()) * 1000
        return sp.current_user_recently_played(limit=limit, after=ds)
    except Exception as e:
        print(f"❌ Error: {e}")
        return None