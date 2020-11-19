import os
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

insight_header = dbc.Col([
        dcc.Markdown(
            """
            ## Insights
            """),
        html.Hr(),
        html.Img(src='assets/img/kmeans_pairplots.png', style={'width': '100%'})

    ])

insights = dbc.Col([
    
])


layout = [insight_header]
