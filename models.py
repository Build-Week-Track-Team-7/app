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

