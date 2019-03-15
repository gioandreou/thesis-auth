import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime
import pycountry
import pandas as pd


app = dash.Dash()

df_age_gender = pd.read_excel('excels/lite/lite-Ages-Gender.xlsx')

df_regions = pd.read_excel('excels/lite/RegionDF.xlsx')

df_page_info = pd.read_excel('excels/lite/lite-Page-Info.xlsx')

df_page_post = pd.read_excel('excels/lite/lite-Page-Post.xlsx')

df_cities = pd.read_excel('excels/lite/lite-City.xlsx')

df_countries = pd.read_excel('excels/lite/lite-Country.xlsx')

df_posts = pd.read_excel('excels/lite/lite-Post-Info.xlsx')

list_cities=list(df_cities.columns)
list_cities=list_cities[1:]
options_cities=[]

list_countries=list(df_countries.columns)
list_countries=list_countries[1:]
options_countries=[]

list_post_ids = list(df_posts['ID'])
options_posts=[]
for post_id in list_post_ids:
    options_posts.append({'label':'{} '.format(df_posts.loc[df_posts['ID']==post_id]['Message'].item()), 'value':post_id})

#world map 
df_countries_map = df_countries.drop('Date',1)
df_country_last = pd.DataFrame()
df_country_last['locations'] = df_countries_map.columns.values
df_country_last['values'] = df_countries_map.iloc[-1].values

for item in df_country_last['locations']:
    country = pycountry.countries.get(alpha_2=item)
    #df_country_last.loc[df_country_last['locations']==item]
    df_country_last['locations'].loc[df_country_last['locations']==item] = country.alpha_3

for city in list_cities:
    options_cities.append({'label':'{} '.format(city), 'value':city})

for country in list_countries:
    options_countries.append({'label':'{} '.format(country), 'value':country})


colors = {
    'background': '#ffffff',
    'text': '#191919'}

graph_fonts={
    'family':'sans-serif',
    'size':'18',
    'color':colors['text']}

style_fonts ={
    'textAlign': 'center',
    'color': colors['text'],
    'fontFamily':'Helvetica',
    'fontSize':'30px'}
style_whole_div ={
    'textAlign': 'left',
    'color': colors['text'],
    'fontFamily':'Helvetica',
    'fontSize':'25px',
    'background-image': 'url(Images/what-the-hex.png)'}

app.layout = html.Div(children=[
    html.H1(
        children='Dashboard of Andreou George Thesis',
        style=style_fonts),
    html.Div(
        children='The Informations and Stats about the Fans of our Page',
        style=style_fonts),
    #Age-Gender
    dcc.Graph(
        id='age-gender',
        figure={'data': [
                {'x': df_age_gender['Date'], 'y': df_age_gender['F.13-17'], 'type': 'lines', 'name': 'F.13-17'},
                {'x': df_age_gender['Date'], 'y': df_age_gender['F.18-24'], 'type': 'lines', 'name': 'F.18-24'},
                {'x': df_age_gender['Date'], 'y': df_age_gender['F.25-34'], 'type': 'lines', 'name': 'F.25-34'},
                {'x': df_age_gender['Date'], 'y': df_age_gender['F.35-44'], 'type': 'lines', 'name': 'F.35-44'},
                {'x': df_age_gender['Date'], 'y': df_age_gender['F.45-54'], 'type': 'lines', 'name': 'F.45-54'},
                {'x': df_age_gender['Date'], 'y': df_age_gender['F.55-64'], 'type': 'lines', 'name': 'F.55-64'},
                {'x': df_age_gender['Date'], 'y': df_age_gender['F.65+'],   'type': 'lines', 'name': 'F.65+'},

                {'x': df_age_gender['Date'], 'y': df_age_gender['M.13-17'], 'type': 'lines', 'name': 'M.13-17'},
                {'x': df_age_gender['Date'], 'y': df_age_gender['M.18-24'], 'type': 'lines', 'name': 'M.18-24'},
                {'x': df_age_gender['Date'], 'y': df_age_gender['M.25-34'], 'type': 'lines', 'name': 'M.25-24'},
                {'x': df_age_gender['Date'], 'y': df_age_gender['M.35-44'], 'type': 'lines', 'name': 'M.35-44'},
                {'x': df_age_gender['Date'], 'y': df_age_gender['M.45-54'], 'type': 'lines', 'name': 'M.45-54'},
                {'x': df_age_gender['Date'], 'y': df_age_gender['M.55-64'], 'type': 'lines', 'name': 'M.55-64'},
                {'x': df_age_gender['Date'], 'y': df_age_gender['M.65+'],   'type': 'lines', 'name': 'M.65+'}
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': graph_fonts,
                'title': 'Age and Gender of FB PAGE'}}),
    #Regions
    dcc.Graph(
        id='regions',
        figure={'data': [
                {'x': df_regions['Regions'], 'y': df_regions['Fans'], 'type': 'bar', 'name': 'Regions'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': graph_fonts,
                'title': 'Regions of Fans '}}),
    #Page Info
    dcc.Graph(
        id='page-info',
        figure={'data': [
                {'x': df_page_info['Date'], 'y': df_page_info['Page View Totals'], 'type': 'lines', 'name': 'Page View Total'},
                {'x': df_page_info['Date'], 'y': df_page_info['Page Fans'], 'type': 'lines', 'name': 'Page Fans'},
                {'x': df_page_info['Date'], 'y': df_page_info['Page Fan Adds Paid'], 'type': 'lines', 'name': 'Page Fan Adds Paid'},
                {'x': df_page_info['Date'], 'y': df_page_info['Page Fan Adds Non Paid'], 'type': 'lines', 'name': 'Page Fan Adds Non Paid'},
                {'x': df_page_info['Date'], 'y': df_page_info['Page Impressions'], 'type': 'lines', 'name': 'Page Impressions'},
                {'x': df_page_info['Date'], 'y': df_page_info['Page Impressions Paid'], 'type': 'lines', 'name': 'Page Impressions Paid'},
                {'x': df_page_info['Date'], 'y': df_page_info['Page Impressions Organic'], 'type': 'lines', 'name': 'Page Impressions Organic'}
            ],
            'layout': {
                'legend':{
                    'size':'15px','color':'#000'},
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': graph_fonts,
                'title': 'Informations about the Page'}}),
    #Post Info
    dcc.Graph(
        id='page-post',
        figure={'data': [
                {'x': df_page_post['Date'], 'y': df_page_post['Page Post Impressions'], 'type': 'lines', 'name': 'Page Post Impressions'},
                {'x': df_page_post['Date'], 'y': df_page_post['Page Post Engagements'], 'type': 'lines', 'name': 'Page Post Engagements'},
                {'x': df_page_post['Date'], 'y': df_page_post['Page Consumptios'], 'type': 'lines', 'name': 'Page Consumptios'},
                {'x': df_page_post['Date'], 'y': df_page_post['Page Post Impressions Paid'], 'type': 'lines', 'name': 'Page Post Impressions Paid'},
                {'x': df_page_post['Date'], 'y': df_page_post['Page Post Impressions Organic'], 'type': 'lines', 'name': 'Page Post Impressions Organic'},
                {'x': df_page_post['Date'], 'y': df_page_post['Page Post Impressions Viral'], 'type': 'lines', 'name': 'Page Post Impressions Viral'}    
            ],
            'layout': {
                'legend':{
                    'size':'15px','color':'#000'},
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': graph_fonts,
                'title': 'Informations about the Posts of the Page'}}),
    
    #cities
    html.Div([
        html.H3('Select Cities:', style=style_fonts),
        dcc.Dropdown(
        id='my_ticker_symbol_cities',
        options=options_cities,
        value=['City'],
        multi=True,
        style={'fontSize':16})],          
            style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),         
    html.Div([
        html.Button(
            id='submit-button-cities',
            n_clicks=0,
            children='Submit',
            style={'fontSize':24, 'marginLeft':'30px'}),
            ], 
            style={'display':'inline-block'}),
    dcc.Graph(
            id='my_graph_cities',
            figure={'data': [
                    {'x': [1,2], 'y': [3,1]}
            ],'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': graph_fonts,
                'title': 'City Plot'}}),
    
    #Countr  
    html.Div([
        html.H3('Select Countries:', style=style_fonts),
        dcc.Dropdown(
            id='my_ticker_symbol_countries',
            options=options_countries,
            value=['Country'],
            multi=True,
            style={'fontSize':16})
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
            ],'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': graph_fonts,
                    'title': 'Country Plot'}}),
    
    #world map
    dcc.Graph(
        id='world-map',
        figure={'data': [
                {"type":'choropleth',
                "locations":df_country_last['locations'], 
                "z":df_country_last['values'],
                "reversescale": False, 
                "marker": {
                    "line": {
                        "color": "rgb(180,180,180)",
                        "width": 0.5}},
                "colorbar": {
                    "title": "Fans Number"},
                "colorscale": 'Viridis'},
                ],'layout': {
                    'width':1500,
                    'height':500,
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': graph_fonts,
                    'title': 'World Map of Fans'}}),
    
    #posts infos 
    html.Div([
        html.H3('Select Posts:', style=style_fonts),
        dcc.Dropdown(
            id='my_ticker_symbol_posts',
            options=options_posts,
            value=['Post'],
            multi=False,
            style={'fontSize':16})
            ],style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
    html.Div([
        html.Button(
            id='submit-button-posts',
            n_clicks=0,
            children='Submit',
            style={'fontSize':24, 'marginLeft':'30px'}),
            ], style={'display':'inline-block'}),
    dcc.Graph(
        id='my_graph_posts',
        figure={'data': [
                {'x':['Impressions'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Impressions'],'type':'bar','name': '%'},
                {'x':['Impressions Paid'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Impressions Paid'],'type':'bar','name': '%'},
                {'x':['Impressions Organic'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Impressions Organic'],'type':'bar','name': '%'},
                {'x':['Impressions Fans'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Impressions Fans'],'type': 'bar','name': '%'},
                {'x':['Impressions Fans Paid'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Impressions Fans Paid'],'type': 'bar','name': '%'},
                {'x':['Enganged Users'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Enganged Users'],'type': 'bar','name': '%'},
                {'x':['Impressions Viral'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Impressions Viral'],'type': 'bar','name': '%'},
                {'x':['Total Reactions'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Total Reactions'],'type': 'bar','name': '%'}
        ]})

],style=style_whole_div)


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


@app.callback(
    Output('my_graph_posts', 'figure'),
    [Input('submit-button-posts', 'n_clicks')],
    [State('my_ticker_symbol_posts', 'value')])
def update_graph_posts(n_clicks, posts_ticker):
    traces_posts = []
    #for tic in posts_ticker:
    traces_posts=([
                    {'x':['Impressions'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Impressions'].item()],'type':'bar',
                    'name':'100%'},
                    
                    {'x':['Impressions Paid'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Paid'].item()],'type':'bar',
                    'name':str(round(df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Paid'].item()/df_posts.loc[df_posts['ID']==posts_ticker]['Impressions'].item()*100,2))+'%'},
                    
                    {'x':['Impressions Organic'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Organic'].item()],'type':'bar',
                    'name':str(round(df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Organic'].item()/df_posts.loc[df_posts['ID']==posts_ticker]['Impressions'].item()*100,2))+'%'},
                    
                    {'x':['Impressions Fans'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Fans'].item()],'type':'bar',
                    'name':str(round(df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Fans'].item()/df_posts.loc[df_posts['ID']==posts_ticker]['Impressions'].item()*100,2))+'%'},
                    
                    {'x':['Impressions Fans Paid'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Fans Paid'].item()],'type':'bar',
                    'name':str(round(df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Fans Paid'].item()/df_posts.loc[df_posts['ID']==posts_ticker]['Impressions'].item()*100,2))+'%'},
                    
                    {'x':['Enganged Users'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Enganged Users'].item()],'type':'bar',
                    'name':str(round(df_posts.loc[df_posts['ID']==posts_ticker]['Enganged Users'].item()/df_posts.loc[df_posts['ID']==posts_ticker]['Impressions'].item()*100,2))+'%'},
                    
                    {'x':['Impressions Viral'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Viral'].item()],'type':'bar',
                    'name':str(round(df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Viral'].item()/df_posts.loc[df_posts['ID']==posts_ticker]['Impressions'].item()*100,2))+'%'},
                    
                    {'x':['Total Reactions'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Total Reactions'].item()],'type':'bar',
                    'name':str(round(df_posts.loc[df_posts['ID']==posts_ticker]['Total Reactions'].item()/df_posts.loc[df_posts['ID']==posts_ticker]['Impressions'].item()*100,2))+'%'}
            ])
        
    figure_posts = {
    'data': traces_posts,
    'layout': {'title':'Message: '+df_posts.loc[df_posts['ID']==posts_ticker]['Message'].item()}}
    return figure_posts

if __name__ == '__main__':
    app.run_server(debug=True)