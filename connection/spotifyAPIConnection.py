"""
Establish a connection to the Spotify API

"""

import spotipy
from spotipy.oauth2 import SpotifyOAuth
from cfg import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET, SPOTIFY_REDIRECT_URI, SCOPE

def spotify_connection():
    try:
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        redirect_uri=SPOTIFY_REDIRECT_URI,
        scope=SCOPE
        ))
        return sp
    except Exception as e:
        print(f"❌ Spotify connection error: {e}")
        return None
