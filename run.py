import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app, server
from pages import index, predictions, insights, process

navbar = dbc.NavbarSimple(
    brand='Spot The Music',
    brand_href='/', 
    children=[
        dbc.NavItem(dcc.Link('Predictions', 
                             href='/predictions', 
                             className='nav-link')), 

        dbc.NavItem(dcc.Link('Insights', 
                             href='/insights', 
                             className='nav-link')), 

        dbc.NavItem(dcc.Link('Process', 
                             href='/process', 
                             className='nav-link')), 
    ],
    sticky='top',
    color='light', 
    light=True, 
    dark=False
)

footer = dbc.Container(
    dbc.Row(
        dbc.Col([
            html.P(
                [
                    html.Span('Lambda School - Build Week', className='mr-1'),
                ], 
                className='lead'
            ),
            html.Span('Track Team 7 - November 2020', className='mr-2'), 
            html.A(html.I(className='fab fa-github-square mr-1'), 
                href='https://github.com/Build-Week-Track-Team-7'),
        ])
    ), id="footer"
)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False), 
    navbar, 
    dbc.Container(id='page-content', className='mt-4'),
    html.Hr(), 
    footer
], id='page-container')

@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/':
        return index.layout
    elif pathname == '/predictions':
        return predictions.layout
    elif pathname == '/insights':
        return insights.layout
    elif pathname == '/process':
        return process.layout
    else:
        return dcc.Markdown('## Page not found')


if __name__ == '__main__':
    app.run_server(debug=True)
