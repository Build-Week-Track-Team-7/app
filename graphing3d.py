# import pandas as pd
# import plotly.express as px
# from sklearn.cluster import KMeans
# from sklearn.preprocessing import StandardScaler

import json
# from plotly.utils import PlotlyJSONEncoder
# from plotly.offline import download_plotlyjs, init_notebook_mode, iplot
import plotly.graph_objs as go


# def plotlyfig2json(fig, fpath=None):
#     """
#     Serialize a plotly figure object to JSON so it can be persisted to disk.
#     Figure's persisted as JSON can be rebuilt using the plotly JSON chart API:

#     http://help.plot.ly/json-chart-schema/

#     If `fpath` is provided, JSON is written to file.

#     Modified from https://github.com/nteract/nteract/issues/1229
#     """

#     redata = json.loads(json.dumps(fig.data, cls=PlotlyJSONEncoder))
#     relayout = json.loads(json.dumps(fig.layout, cls=PlotlyJSONEncoder))

#     fig_json=json.dumps({'data': redata,'layout': relayout})

#     if fpath:
#         with open(fpath, 'w') as f:
#             f.write(fig_json)
#     else:
#         return fig_json

def plotlyfromjson(fpath):
    """Render a plotly figure from a json file"""
    with open(fpath, 'r') as f:
        v = json.loads(f.read())

    fig = go.Figure(data=v['data'], layout=v['layout'])
    return fig
    # iplot(fig, show_link=False)

# # importing the csv file to create models.
# music_df = pd.read_csv('data.csv', index_col=['name'])
# # droping columns that will just muddy up the data
# music_df = music_df.drop(columns=['artists', 'release_date', 'id'])
# # scaling the information to find the best fit
# music_scale = pd.DataFrame(data=StandardScaler().fit_transform(music_df),
#                            columns=music_df.columns,
#                            index=music_df.index)
# # creating cluster definition to call back when running kmeans
# kmeans = KMeans(n_clusters=10, random_state=42)
# kmeans.fit(music_scale.values)
# # find the centers of the Kmeans data
# centers = kmeans.cluster_centers_
# # prepare the lables of Kmeans for graphing
# labels = kmeans.labels_
# # adding lables to color code each group type
# music_df['group'] = labels.astype(str)
# # sampling the dataset to make a more managable graph
# music_sample = music_df.sample(5000, random_state=42)
# # color dictionary
# colors = {'0': 'crimson',
#           '1': '#4da6ff',
#           '2': '#ff66cc',
#           '3': '#993366',
#           '4': '#ffff66',
#           '5': '#99ff33',
#           '6': '#009933',
#           '7': '#00ffff',
#           '8': '#cc3300',
#           '9': '#cc33ff'}
# # graphing the Kmeans test
# fig = px.scatter_3d(music_sample,
#                     x='energy',  # the first important feature
#                     y='danceability',  # the second important feature
#                     z='liveness',  # the third important feature
#                     color='group',  # calling the K-means group labels
#                     color_discrete_map=colors,  # using the color dictionary
#                     width=700,
#                     height=700,
#                     hover_name=music_sample.index)  # show the name of the song
# fig.update_traces(marker=dict(size=2),  # changing the dot size
#                   showlegend=False)  # removing the legend
# # fig.show()

# plotlyfig2json(fig, 'frontpagefig.json')
