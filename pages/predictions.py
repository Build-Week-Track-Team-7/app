import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from models import *
from app import app

kmeans = Antony.load_kmeans('pipeline.joblib')

left = 'Lower'
middle = 'Same'
right = 'Higher'
options = [left, middle, right]
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
    feature: default_value for feature in feature_order
}


# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
header =dcc.Markdown(
            """
            ## Predictions  

            ###### Input a song you like and it's artist, then say if you want more, less or the same of each of the features."""
)

features = []

for feature in feature_importance:
    _id = feature+'-radio-button-group'
    radio_group_id_list.append(_id)
    features.extend([
        html.P(
            [
                html.Span(
                    feature.capitalize(), 
                    id=f'{feature}-tooltip-target',
                )
            ], style=style
        ),
        dbc.Tooltip(
            feature_descriptions[feature],
            target=f'{feature}-tooltip-target'
        ),
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
            dbc.Button("Get Song Info", id='get-song-info', color='warning', size="md", style={'margin-top': '15px'},),
        ], width=5),
        dbc.Col([
            dbc.Label("Song Artist", style={'margin-top': margin_top}),
            dbc.Input(id="artist", placeholder=current_artist, type="text", bs_size='sm'),
            dbc.Button("Get New Songs", id='song-search', color='success', size="md", style={'margin-top': '15px'},),
        ], width=5),
    ]),
    dcc.Markdown(
        children=[],
        style={'margin-top': margin_top},
        id='selected-features'
    ),])

body = dbc.Row([features, predictions])

layout = dbc.Col([header, body])


@app.callback([Output('selected-features', 'children')],
    [Input('get-song-info', 'n_clicks')],
    [State(_id, 'value') for _id in radio_group_id_list]+
    [State("title", "value"),
    State("artist", "value")])
def render_prediction(n_clicks, *values):

    return []
    
    # for feature, value in zip(feature_importance, values):
    #     current_selections[feature] = value

    # data = Jeannine.order_features(current_selections)
    # print(data)

    # return ['&nbsp  \n'.join([': '.join([str(l), str(r)]) for l, r in current_selections.items()])]


def get_song_info(title, artist, year):
    pass
