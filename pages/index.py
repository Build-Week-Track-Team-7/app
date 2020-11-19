import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px


from app import app
from models import Antony

column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Welcome to  
            # Spot The Music!


            This graph shows the relation between a subset of features from a total data set.  The features displayed are the 3 most important features to the machine learning model.  This relation shows the clustering and which pieces of music are most similar to each other based on the total available 15 features. The different colors indicate which group, after applying a K-means test to the data, the individual song belongs to.  You will notice that as you hover over a point you will see the song title it’s group number and the values of each feature.  The 3 predominant features that are graphed are ‘energy’ ‘danceability’ and ‘liveness’.  
            

            Energy - refers to the perceptual measure of intensity and activity. Typically, energetic tracks feel fast, loud, and noisy. For example, death metal has high energy, while a Bach prelude scores low on the scale. Perceptual features contributing to this attribute include dynamic range, perceived loudness, timbre, onset rate, and general entropy.  
            
            
            Danceability - this is on a scale of 0-1 of how easy a song is to dance too based on various features.  
            
            
            Liveness - is a feature that describes how detectable a live audience is in a recording. 

            We use these features along with several others to see if any songs have similarities and can provide a similar experience to the user.  

            Click the button below and hopefully you can find a new song you like.
            
            Dataset used for this project can be found at [Kaggle.com](https://www.kaggle.com/yamaerenay/spotify-dataset-19212020-160k-tracks).  

            """
        ),
        dcc.Link(dbc.Button('Discover New Songs', color='primary'), href='/predictions')
    ], width=4
)



graph = dbc.Col(
    [
        dcc.Graph(figure=Antony.plotlyfromjson('frontpagefig.json')),
    ], width=6
)

layout = dbc.Row([column1, graph])

