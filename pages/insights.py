import os
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

image_descriptions = {
    'kmeans_pairplots.png': """The pair plots shown here show how the various features are related to one another as a part of the whole relationship that allows us to group various songs together.  You can see in many of the graphs some of the features have more strongly similar clusters then others in relation to one another.  These clustering patterns indicate the different groups and their correlated values.  These correlated values then determine the grouping that the various songs would belong to indicating what would be a similar experience for the user.""",

    # 'spotify_releasedate_popularity_explicit.png': """Songs with explicit language are becoming increasingly popular (shown in yellow)""",

    # 'spotify_pairplot_pop_year.png': """The popularity of each of the keys over the years.""",

    'song%20popularity%20by%20explicitness%20and%20year.png': """""",

    'song%20popularity%20by%20major_minor%2C%20key%20and%20year.png': """""",

    'song%20popularity%20by%20year%2C%20key%20and%20major_minor%20pastel.png': """""",

    'song%20popularity%20by%20year%2C%20key%20and%20major_minor.png': """""",
}

insight_header = dbc.Col([
        dcc.Markdown(
            """
            ## Insights
            """),
        html.Hr(),
    ])

insights = []

for image, description in image_descriptions.items():
    insights.extend([
        dcc.Markdown(f'  \n\n{description}', style={'margin-left': '10px'}),
        html.A(html.Img(src=f'assets/img/{image}', style={'width': '100%'}), href=f'https://raw.githubusercontent.com/Build-Week-Track-Team-7/app/main/assets/img/{image}', target='_blank'),
    ])

insights = dbc.Col(insights)

layout = [insight_header, insights]
