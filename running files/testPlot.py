import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web # requires v0.6.0 or later
from datetime import datetime
import pandas as pd

app = dash.Dash()

df_cities = pd.read_excel('excels/lite/lite-City.xlsx')
#cities = cities.T
list_cities=list(df_cities.columns)
list_cities=list_cities[1:]
options_cities=[]

df_countries = pd.read_excel('excels/lite/lite-Country.xlsx')
#cities = cities.T
list_countries=list(df_countries.columns)
list_countries=list_countries[1:]
options_countries=[]


for city in list_cities:
    options_cities.append({'label':'{} '.format(city), 'value':city})

for country in list_countries:
    options_countries.append({'label':'{} '.format(country), 'value':country})

app.layout =html.Div([
            html.H1('Cities-Counties of The page',style={
                'textAlign': 'center',
                'color': '#191919',
                'fontFamily':'Helvetica',
                'fontSize':'30px'}),
            html.Div([
                html.H3('Select Cities:', style={'paddingRight':'30px'}),
                dcc.Dropdown(
                id='my_ticker_symbol_cities',
                options=options_cities,
                value=['City'],
                multi=True
            )
                ],          
                style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
            
            html.Div([
            html.Button(
                id='submit-button-cities',
                n_clicks=0,
                children='Submit',
                style={'fontSize':24, 'marginLeft':'30px'}
            ),
            ], style={'display':'inline-block'}),
            dcc.Graph(
            id='my_graph_cities',
            figure={
                'data': [
                    {'x': [1,2], 'y': [3,1]}
            ]
        }
),
                html.Div([
                html.H3('Select Countries:', style={'paddingRight':'30px'}),
                dcc.Dropdown(
                id='my_ticker_symbol_countries',
                options=options_countries,
                value=['Country'],
                multi=True
            )
                ],          
                style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
            html.Div([
            html.Button(
                id='submit-button-countries',
                n_clicks=0,
                children='Submit',
                style={'fontSize':24, 'marginLeft':'30px'}
            ),
            ], style={'display':'inline-block'}),
            dcc.Graph(
            id='my_graph_countries',
            figure={
                'data': [
                    {'x': [1,2], 'y': [3,1]}
            ]
        }
)
])

@app.callback(
    Output('my_graph_cities', 'figure'),
    [Input('submit-button-cities', 'n_clicks')],
    [State('my_ticker_symbol_cities', 'value')])
def update_graph_cities(n_clicks, cities_ticker):
    traces_city = []
    for tic in cities_ticker:
        #df = web.DataReader(tic,'iex',start,end)
        traces_city.append({'x':df_cities['Date'], 'y': df_cities[tic], 'name':tic})
        figure_city = {
        'data': traces_city,
        'layout': {'title':'  &&  '.join(cities_ticker)}
    }
    return figure_city

@app.callback(
    Output('my_graph_countries', 'figure'),
    [Input('submit-button-countries', 'n_clicks')],
    [State('my_ticker_symbol_countries', 'value'),
    ])
def update_graph_countries(n_clicks, countries_ticker):
    traces_country = []
    for tic in countries_ticker:
        #df = web.DataReader(tic,'iex',start,end)
        traces_country.append({'x':df_countries['Date'], 'y': df_countries[tic], 'name':tic})
        figure_country = {
        'data': traces_country,
        'layout': {'title':'  &&  '.join(countries_ticker)}
    }
    return figure_country


if __name__ == "__main__":
    app.run_server()