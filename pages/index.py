import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

from app import app
from graphing3d import fig

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Welcome to Spot The Music!

            Seen here is approximately a 3% sample of a database found at [Kaggle.com](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks).  

            This graph has 5000 randomly selected songs from the database of over 160 thousand songs.  

            Click the button below and hopefully you can find a new song you like.

            """
        ),
        dcc.Link(dbc.Button('Discover New Songs', color='primary'), href='/predictions')
    ], md=4
)



graph = dbc.Col(
    [
        dcc.Graph(figure=fig),
    ]
)

layout = dbc.Row([column1, graph])
