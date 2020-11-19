from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

CLIENT_ID = getenv('CLIENT_ID')
CLIENT_SECRET = getenv('CLIENT_SECRET')
# REDIRECT_URI = os.getenv('REDIRECT_URI')


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET
))


def get_song_audio_features(id):
    info = sp.audio_features([id])

def get_spotify_song_info(title, artist):
    return [title, artist]

