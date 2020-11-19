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

music_df = pd.read_csv('music.csv', index_col=['name', 'artists'])

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


# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
header =dcc.Markdown(
            """
            ## Predictions  

            ###### Input a song you like and it's artist, then say if you want more, less or the same of each of the features."""
)

features = []

for feature in gathered_feature_order:
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
], md=8)

body = dbc.Container(dbc.Row([predictions, features]))

layout = dbc.Col([header, body])



@app.callback(Output('selected-features', 'children'),
    [Input('get-song-info', 'n_clicks')],
    [State("name", "value"), State("artist", "value")])
def get_song_info(n_clicks, name, artist):
    if not n_clicks:
        return ''
    song_info = get_spotify_song_info(name, artist)[0]

    if song_info == 'NO INPUT PROVIDED':
        return song_info
    elif not song_info:
        return ["No results: &nbsp  \nMakes sures you're spelling and gramer is corect."]

    displayed_song_features = {
        feature_names: None for feature_names in displayed_feature_order
    }

    for key, value in song_info.items():
        if key in displayed_song_features:
            if isinstance(value, list):
                value = ', '.join(value)
            displayed_song_features[key] = value

    global song
    song = Song(data=[song_info], columns=full_feature_order)
    print(song)

    return 'If the track below is not what you want, try being more specific. &nbsp  \n\n' + '&nbsp  \n'.join([f"{l.capitalize()}: {r}" for l, r in displayed_song_features.items()])


@app.callback(Output('song-suggestions', 'children'),
    [Input('get-new-songs', 'n_clicks')],
    [State("name", "value"),
    State("artist", "value")]+
    [State(_id, 'value') for _id in radio_group_id_list])
def get_new_songs(n_clicks, name, artist, *values):
    if not n_clicks:
        return ''
    global song

    if not len(song):
        return 'No song being checked.'

    selected_features = {
        feature: value for feature, value in zip(gathered_feature_order, values)
    }

    song = shift_features(song, selected_features)

    song = process(song, Antony)

    song_group = int(scale_and_kmeans(song)[0])

    same_group = music_df[music_df['group'] == song_group]

    print(same_group.head(20))
    print(len(same_group))

    new_songs = same_group.sample(10)

    return '&nbsp  \n\n'.join('&nbsp  \nArtists: '.join(x).replace('[', '').replace(']', '').replace("'", '') for x in new_songs.index)


