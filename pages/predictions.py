from logging import PlaceHolder
import dash
import dash_bootstrap_components as dbc
from dash_bootstrap_components._components.FormGroup import FormGroup
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from models import *
from app import app

left = 'Lower'
middle = 'Same'
right = 'Higher'

options = [left, middle, right]

feature_list = ['Danceability', 'test2', 'test3', 'test4', 'test5']

_id = '-id'
default_value = 'Same'

radio_color = 'info'

radio_group_id_list = []

margin_left = str(len(left) * -2) + 'px'
margin_top = '15px'
margin_bottom = '1px'

style = {
    'margin-top': margin_top,
    'margin-bottom': margin_bottom,
    'margin-left': margin_left,
    'font-weight': 'bold'
}

current_title = "Song Title..."
current_artist = "Song Artist..."

current_selections = {
    feature: default_value for feature in feature_list
}


# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
header = dbc.Row(
    [
        dcc.Markdown(
            """
            ## Predictions  

            ###### Input a song you like and it's artist, then say if you want more, less or the same of each of the features."""
        ),
    ]
)


features = []

for feature in feature_list:
    _id = feature+'-radio-button-group'
    radio_group_id_list.append(_id)
    features.extend([
        html.P(feature.capitalize(), style=style),
        dbc.RadioItems(options=[
                {"label": option.capitalize(), "value": option} for option in options
            ], 
            id=_id,
            value="Same",
            inline=True,
        )]
    )

features = dbc.Col(features, md=4)



predictions = dbc.Col([
    dbc.Row([
        dbc.Col([
            dbc.Label("Song Title", style={'margin-top': margin_top}),
            dbc.Input(id="title", placeholder=current_title, type="text", bs_size='sm'),
        ], width=5),
        dbc.Col([
            dbc.Label("Song Artist", style={'margin-top': margin_top}),
            dbc.Input(id="artist", placeholder=current_artist, type="text", bs_size='sm'),
        ], width=5),
        dbc.Col([
            dbc.Button("Predict", id='predict-button', color='success', size="lg", style={'margin-top': '30px'})
        ])
    ]),
    dcc.Markdown(
        children=['&nbsp  \n'.join([': '.join([str(l), str(r)]) for l, r in current_selections.items()])],
        style={'margin-top': margin_top},
        id='selected-features'
    ),
])

body = dbc.Row([features, predictions])

layout = dbc.Col([header, body])



@app.callback(
    [Output('selected-features', 'children')],
    [Input('predict-button', 'n_clicks')],
    [State(radio_group_id, 'value') for radio_group_id in radio_group_id_list],)
def render_prediction(n_clicks, *values):
    for feature, value in zip(feature_list, values):
            current_selections[feature] = value

    data = Antony.get_prediction(current_selections)
    print(data)

    return ['&nbsp  \n'.join([': '.join([str(l), str(r)]) for l, r in current_selections.items()])]


