# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
            ## Song Suggestion Process
            
            ---
            
            The information/attributes can be seen in the csv file found at Kaggle, but to make it easier on ourselves, we got our information by connecting to the Spotify API and making a query/search for the song in question from the user.  

            The user then selects whether they want that attribute to be higher, lower, or the same value compared to the song.   

            The songs values are then adjusted in the direction of the user's selections.  

            The new information is then sent through an algorithm to assign a song group.  

            We then recommend 10 songs that are in that song group.  
            \(FYI Recommended songs are not guaranteed to have the selected values from the user.\) 

            """
        )
    ],
)

layout = dbc.Row([column1])
