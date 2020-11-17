# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
layout = html.Div(
    [
        dcc.Markdown(
            """
        
            ## Honey! I'm HOOOMMMMEE!

            """
        ),
        dcc.Link(dbc.Button('Find New Songs', color='primary'), href='/predictions')
    ]
)
# gapminder = px.data.gapminder()
# fig = px.scatter(gapminder.query("year==2007"), x="gdpPercap", y="lifeExp", size="pop", color="continent",
#            hover_name="country", log_x=True, size_max=60)

# column2 = dbc.Col(
#     [
#         dcc.Graph(figure=fig),
#     ]
# )

# layout = dbc.Row([column1, column2])
