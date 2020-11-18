import pandas as pd
import numpy as np

feature_order = ['acousticness','artists','danceability','duration_ms','energy','explicit','id','instrumentalness','key','liveness','loudness','mode','name','popularity','release_date','speechiness','tempo','valence','year']

feature_importance = ['energy',
 'danceability',
 'liveness',
 'key',
 'tempo',
 'duration_ms',
 'instrumentalness',
 'loudness',
 'valence',
 'acousticness',
 'popularity',
 'speechiness']

non_selectable_features = ['artists', 'explicit', 'id', 'name', 'release_date', 'year', 'mode']

class Antony:
    def get_prediction(values):
        return values

class Jeannine:
    def order_features(data):
        in_order = [np.NaN for _ in feature_order]
        for feature, value in data.items():
            in_order[feature_order.index(feature.lower())] = value
        return in_order

class Shannon:
    pass
