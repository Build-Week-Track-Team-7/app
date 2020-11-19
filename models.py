import json
import plotly.graph_objs as go
from plotly.utils import PlotlyJSONEncoder
import pandas as pd
import numpy as np
from features import *

from joblib import load

class Antony:
    def load_kmeans(model_path):
        kmeans = load(model_path)
        return kmeans

    def load_scalar(scalar_path):
        scalar = load(scalar_path)
        return scalar

    def plotlyfig2json(fig, fpath=None):
        """
        Serialize a plotly figure object to JSON so it can be persisted to disk.
        Figure's persisted as JSON can be rebuilt using the plotly JSON chart API:

        http://help.plot.ly/json-chart-schema/

        If `fpath` is provided, JSON is written to file.

        Modified from https://github.com/nteract/nteract/issues/1229
        """

        redata = json.loads(json.dumps(fig.data, cls=PlotlyJSONEncoder))
        relayout = json.loads(json.dumps(fig.layout, cls=PlotlyJSONEncoder))

        fig_json=json.dumps({'data': redata,'layout': relayout})

        if fpath:
            with open(fpath, 'w') as f:
                f.write(fig_json)
        else:
            return fig_json

    def plotlyfromjson(fpath):
        """Render a plotly figure from a json file"""
        with open(fpath, 'r') as f:
            v = json.loads(f.read())

        fig = go.Figure(data=v['data'], layout=v['layout'])
        return fig
        # iplot(fig, show_link=False)


class Jeannine:
    def order_features(data):
        in_order = [np.NaN for _ in feature_order]
        for feature, value in data.items():
            in_order[feature_order.index(feature.lower())] = value
        return in_order

class Shannon:
    pass


class Song(pd.DataFrame):
    pass


def scale_and_kmeans(song):
    scale = Antony.load_scalar('scale.joblib')
    kmeans = Antony.load_kmeans('pipeline.joblib')

    song = scale.transform(song)
    song = kmeans.predict(song)

    return song


one_range = [
    'energy',
    'danceability',
    'liveness',
    'instrumentalness',
    'valence',
    'acousticness',
    'speechiness'
]

set_range = {
    'key': [-1, 12],
    'loudness': [-60, 1],
    'popularity': [0, 101],
    'year': [1920, 2021],
    'explicit': [0, 2]
}

any_range = [
    'tempo',
    'duration_ms',
]

def shift_features(song, shift_values):
    song = song.copy()
    for feature in shift_values:
        if song[feature][0]:
            if feature in one_range:
                shift_value = .1
                if shift_values[feature] == 'Higher':
                    song.loc[:, feature] = min(song[feature][0] + shift_value, 1.0)
                elif shift_values[feature] == 'Lower':
                    song.loc[:, feature] = max(song[feature][0] - shift_value, 0.0)
            elif feature in set_range:
                l, r = set_range[feature]
                if shift_values[feature] == 'Higher':
                    song.loc[:, feature] = min(song[feature][0] + int(len(range(l, r))/10), r)
                elif shift_values[feature] == 'Lower':
                    song.loc[:, feature] = max(song[feature][0] - int(len(range(l, r))/10), l)
            elif feature in any_range:
                if shift_values[feature] == 'Higher':
                    song.loc[:, feature] = int(song[feature][0] * 1.1)
                elif shift_values[feature] == 'Lower':
                    song.loc[:, feature] = int(song[feature][0] * 0.9)

    return song
