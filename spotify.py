from pprint import pprint
from os import getenv
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials, SpotifyOAuth

from features import *

CLIENT_ID = getenv('CLIENT_ID')
CLIENT_SECRET = getenv('CLIENT_SECRET')
# REDIRECT_URI = os.getenv('REDIRECT_URI')


sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id=CLIENT_ID, 
    client_secret=CLIENT_SECRET
))

def get_song_audio_features(ids=[]):
    info = sp.audio_features(ids)
    return info

def get_spotify_song_info(title=None, artist=None):
    if not title and not artist:
        return ['NO INPUT PROVIDED']
    query = ''
    if title:
        query += f"track:{title}"
    if title and artist:
        query += " "
    if artist:
        query += f"artist:{artist}"
    
    data = sp.search(query)['tracks']['items']

    ids = [x['id'] for x in data]
    names = [x['name'] for x in data]
    artists = []
    for x in data:
        arts = []
        for y in x['artists']:
            arts.append(y['name'])
        artists.append(arts)
    # artists = [y['name'] for x in data for y in x['artists']]
    explicits = [x['explicit'] for x in data]
    popularities = [x['popularity'] for x in data]
    try:
        release_dates = [x['album']['release_date'] for x in data]
        years = [x['album']['release_date'][:4] for x in data]
    except KeyError:
        release_dates = [None for x in data]
        years = [None for x in data]

    song_features = get_song_audio_features(ids)

    for i, song in enumerate(song_features):
        if len(names) > i:
            song['name'] = names[i]
            song['artists'] = artists[i]
            song['explicit'] = explicits[i]
            song['popularity'] = popularities[i]
            song['release_date'] = release_dates[i]
            song['year'] = years[i]
    
    if song_features[0]:
        for s in song_features:
            for feat in list(s):
                if feat not in feature_order:
                    del s[feat]

    return song_features

# pprint(get_spotify_song_info('freaky friday', 'lil dick'))
