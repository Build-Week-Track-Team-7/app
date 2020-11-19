from re import S
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

from spotify import get_spotify_song_info
from models import *
from app import app

# kmeans = Antony.load_kmeans('pipeline.joblib')
song = Song()

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

song_info = {
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
            dbc.Input(id="name", placeholder=current_title, type="text", bs_size='sm'),
            dbc.Button("Get Song Info", id='get-song-info', color='warning', size="md", style={'margin-top': '15px'},),
            dcc.Markdown(
                children=['features'],
                style={'margin-top': margin_top},
                id='selected-features'
            ),
        ], width=6),
        dbc.Col([
            dbc.Label("Song Artist", style={'margin-top': margin_top}),
            dbc.Input(id="artist", placeholder=current_artist, type="text", bs_size='sm'),
            dbc.Button("Get New Songs", id='get-new-songs', color='success', size="md", style={'margin-top': '15px'},),
            dcc.Markdown(
                children=['song suggestions'],
                style={'margin-top': margin_top},
                id='song-suggestions'
            ),
        ], width=6),
    ]),
])

body = dbc.Row([features, predictions])

layout = dbc.Col([header, body])

@app.callback(Output('song-suggestions', 'children'),
    [Input('get-new-songs', 'n_clicks')],
    [State("name", "value"),
    State("artist", "value")]+
    [State(_id, 'value') for _id in radio_group_id_list])
def get_new_songs(n_clicks, name, artist, *values):
    if not n_clicks:
        return ''
    global song
    print(song)

    return 'NOT IMPLEMENTED'

@app.callback(Output('selected-features', 'children'),
    [Input('get-song-info', 'n_clicks')],
    [State("name", "value"), State("artist", "value")])
def get_song_info(n_clicks, name, artist):
    if not n_clicks:
        return ''
    global song
    raw_info = get_spotify_song_info(name, artist)

    if raw_info[0] == 'NO INPUT PROVIDED':
        return raw_info
    elif not raw_info[0]:
        return ["No results &nbsp  \nMakes sures you're spelling and gramer is corect"]

    info = {
        feature_names: None for feature_names in feature_importance
    }

    print(raw_info)


    for key, value in raw_info[0].items():
        if key in info:
            info[key] = value

    return 'If the track below is not what you want, try being more specific &nbsp  \n\n' + '&nbsp  \n'.join([f'{l}: {r}' for l, r in info.items()])

