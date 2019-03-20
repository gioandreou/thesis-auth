import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime
import pycountry
import pandas as pd


app = dash.Dash()
# excel imports to pandas dataframes
df_age_gender = pd.read_excel('excels/lite/lite-Ages-Gender.xlsx')

df_regions = pd.read_excel('excels/lite/RegionDF.xlsx')

df_page_info = pd.read_excel('excels/lite/lite-Page-Info.xlsx')

df_page_post = pd.read_excel('excels/lite/lite-Page-Post.xlsx')

df_cities = pd.read_excel('excels/lite/lite-City.xlsx')

df_countries = pd.read_excel('excels/lite/lite-Country.xlsx')

df_posts = pd.read_excel('excels/lite/lite-Post-Info.xlsx')

df_posts_cont = pd.read_excel('excels/lite/lite-Post-Info-Countinuously.xlsx')

df_ag = pd.read_excel('excels/lite/lite-Ages-Gender.xlsx')

df_page_fans = pd.read_excel('excels/lite/lite-Page-Info.xlsx')

df_regions_fans = pd.read_excel('excels/lite/RegionDF_countinuously.xlsx')


#set starting and ending date for the first appearance in the plot
date1 = (df_posts_cont[(df_posts_cont['ID']=='974146599436745_974147879436617') & (df_posts_cont['STATUS']=='START')]['Date Fetched'].values[0])
#check if the post has a dead date or is still alive
if(len(df_posts_cont[(df_posts_cont['ID']=='974146599436745_974147879436617') & (df_posts_cont['STATUS']=='DEAD')]['Date Fetched'].values)==0):
    date2 = (df_posts_cont[(df_posts_cont['ID']=='974146599436745_974147879436617') & (df_posts_cont['STATUS']=='ALIVE')]['Date Fetched'].values[-1])
else:
    date2 = (df_posts_cont[(df_posts_cont['ID']=='974146599436745_974147879436617') & (df_posts_cont['STATUS']=='DEAD')]['Date Fetched'].values[0])

#REFORM dataframes and keep only the dates and data we need for the first appearance also
df_page_fans = df_page_fans[['Date','Page Fans']]
df_page_fans_short = df_page_fans.loc[(df_page_fans['Date']>=date1),:]

#df_test are those who are appeared first as deafult in the plot 
df_test_age_gender = df_ag.loc[(pd.to_datetime(df_ag['Date'])>=date1) & (pd.to_datetime(df_ag['Date'])<=date2),:]
df_test_diff = df_test_age_gender.diff()
df_test_regions = df_regions_fans.loc[(pd.to_datetime(df_regions_fans['Date Fetched'])>=date1) & (pd.to_datetime(df_regions_fans['Date Fetched'])<=date2),:]

list_post_cont_ids = list(df_posts_cont['ID'])
list_post_cont_ids = list(set(list_post_cont_ids))
options_posts_cont=[]
for post_id in list_post_cont_ids:
    templist = list(set(df_posts_cont[df_posts_cont['ID']==post_id]['Message']))
    options_posts_cont.append({'label':'{} '.format( templist[0] ), 'value':post_id})

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


#STYLES
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
    
    html.Div(children=[    
        html.P("  "),
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
    ],style={'border':'1px solid', 'border-radius': 10}),   
    
    html.Div(children=[
        html.P("  "),
        html.Div(
            children='Geographic Informations and Stats about the Fans of our Page',
            style=style_fonts),
        html.P("  "),
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
        
        #Country  
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
    ],style={'border':'1px solid', 'border-radius': 10}),    
    
    html.Div(children=[
        html.P("  "),
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
            ]}),
    ],style={'border':'1px solid', 'border-radius': 10}),        
    
    html.Div(children=[
        html.H1(
            children='Demographic Analysis of Posts For Spending Strategy ',
            style=style_fonts),
        html.Div([
            html.H3('Select Post:', style=style_fonts),
            dcc.Dropdown(
            id='my_ticker_symbol_post_cont',
            options=options_posts_cont,
            value=['Posts'],
            multi=False,
            style={'fontSize':16})],          
                style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),         
        html.Div([
            html.Button(
                id='submit-button-posts-cont',
                n_clicks=0,
                children='Submit',
                style={'fontSize':24, 'marginLeft':'30px'}),
                ], 
                style={'display':'inline-block'}),
        dcc.Graph(
            id='my_graph_posts_cont',
            figure={'data': [
                    {'x': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Impressions'],'text':df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['STATUS'], 'type': 'lines', 'name': 'Impressions'},
                    {'x': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Impressions Paid'], 'type': 'lines', 'name': 'Impressions Paid'},
                    {'x': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Impressions Organic'], 'type': 'lines', 'name': 'Impressions Organic'},
                    {'x': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Impressions Fans'], 'type': 'lines', 'name': 'Impressions Fans'},
                    {'x': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Impressions Fans Paid'], 'type': 'lines', 'name': 'Impressions Fans Paid'},
                    {'x': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Enganged Users'], 'type': 'lines', 'name': 'Enganged Users'},
                    {'x': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Impressions Viral'], 'type': 'lines', 'name': 'Impressions Viral'},
                    {'x': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']=='974146599436745_974147879436617']['Total Reactions'],   'type': 'lines', 'name': 'Total Reactions'},
                    {'x': df_page_fans_short['Date'], 'y': df_page_fans_short['Page Fans'],   'type': 'lines', 'name': 'Page Fans'}
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': graph_fonts,
                    'title': 'Lines of Each Post'}}),

        html.P(
            id='text-bottom',
            children=['Post is alive from: '
                +str(df_posts_cont[(df_posts_cont['ID']=='974146599436745_974147879436617') & (df_posts_cont['STATUS']=='START')]['Date Fetched'].values[0])
                +' until: '
                +str(df_posts_cont[(df_posts_cont['ID']=='974146599436745_974147879436617') & (df_posts_cont['STATUS']=='DEAD')]['Date Fetched'].values[0])
            ],
            style=style_fonts),
        
        dcc.Graph(
            id='linegraph_posts_cont_age_gender',
            figure={'data': [
                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['F.13-17'], 'type': 'lines', 'name': 'F.13-17'},
                    
                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['F.18-24'], 'type': 'lines', 'name': 'F.18-24'},
                    
                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['F.25-34'], 'type': 'lines', 'name': 'F.25-34'},
                    
                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['F.35-44'], 'type': 'lines', 'name': 'F.35-44'},
                    
                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['F.45-54'], 'type': 'lines', 'name': 'F.45-54'},
                    
                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['F.55-64'], 'type': 'lines', 'name': 'F.55-64'},
                    
                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['F.65+'],   'type': 'lines', 'name': 'F.65+'},

                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['M.13-17'], 'type': 'lines', 'name': 'M.13-17'},
                    
                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['M.18-24'], 'type': 'lines', 'name': 'M.18-24'},
                    
                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['M.25-34'], 'type': 'lines', 'name': 'M.25-24'},
                    
                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['M.35-44'], 'type': 'lines', 'name': 'M.35-44'},
                    
                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['M.45-54'], 'type': 'lines', 'name': 'M.45-54'},
                    
                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['M.55-64'], 'type': 'lines', 'name': 'M.55-64'},
                    
                    {'x': df_test_age_gender['Date'], 'y': df_test_age_gender['M.65+'],   'type': 'lines', 'name': 'M.65+'}
                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': graph_fonts,
                    'title': 'Lines of  Each Age-Gender Group at Specific Post Dates'}}),

        dcc.Graph(
            id='linegraph_posts_cont_regions',
            figure={'data': [
                    {'x': df_test_regions[df_test_regions['Region']=='Central Macedonia, Greece']['Date Fetched'], 'y': df_test_regions[df_test_regions['Region']=='Central Macedonia, Greece']['Fans'], 'type': 'lines', 'name': 'Central Macedonia, Greece'},
                    
                    {'x': df_test_regions[df_test_regions['Region']=='Attica (region), Greece']['Date Fetched'], 'y': df_test_regions[df_test_regions['Region']=='Attica (region), Greece']['Fans'], 'type': 'lines', 'name': 'Attica (region), Greece'},
                    
                    {'x': df_test_regions[df_test_regions['Region']=='Western Greece, Greece']['Date Fetched'], 'y': df_test_regions[df_test_regions['Region']=='Western Greece, Greece']['Fans'], 'type': 'lines', 'name': 'Western Greece, Greece'},
                    
                    {'x': df_test_regions[df_test_regions['Region']=='Thessaly, Greece']['Date Fetched'], 'y': df_test_regions[df_test_regions['Region']=='Thessaly, Greece']['Fans'], 'type': 'lines', 'name': 'Thessaly, Greece'},
                    
                    {'x': df_test_regions[df_test_regions['Region']=='Epirus (region), Greece']['Date Fetched'], 'y': df_test_regions[df_test_regions['Region']=='Epirus (region), Greece']['Fans'], 'type': 'lines', 'name': 'Epirus (region), Greece'},
                    
                    {'x': df_test_regions[df_test_regions['Region']=='Eastern Macedonia and Thrace, Greece']['Date Fetched'], 'y': df_test_regions[df_test_regions['Region']=='Eastern Macedonia and Thrace, Greece']['Fans'], 'type': 'lines', 'name': 'Eastern Macedonia and Thrace, Greece'},
                    
                    {'x': df_test_regions[df_test_regions['Region']=='Crete, Greece']['Date Fetched'], 'y': df_test_regions[df_test_regions['Region']=='Crete, Greece']['Fans'],   'type': 'lines', 'name': 'Crete, Greece'},


                ],
                'layout': {
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': graph_fonts,
                    'title': 'Lines of Each Region at Specific Post Dates'}}),

    ],style={'border':'1px solid', 'border-radius': 10})

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


@app.callback(
    Output('my_graph_posts_cont', 'figure'),
    [Input('submit-button-posts-cont', 'n_clicks')],
    [State('my_ticker_symbol_post_cont', 'value')])
def update_graph_posts_cont(n_clicks, posts_ticker_cont):
    traces_posts_cont = []
    #for tic in posts_ticker_cont:
    
    date_from = (df_posts_cont[(df_posts_cont['ID']==posts_ticker_cont) & (df_posts_cont['STATUS']=='START')]['Date Fetched'].values[0])
    df_page_fans_short = df_page_fans.loc[(df_page_fans['Date']>=date_from),:]

    traces_posts_cont=([
                    {'x': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Impressions'], 'text':df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['STATUS'], 'type': 'lines', 'name': 'Impressions'},
                    
                    {'x': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Impressions Paid'], 'type': 'lines', 'name': 'Impressions Paid'},
                
                    {'x': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Impressions Organic'], 'type': 'lines', 'name': 'Impressions Organic'},
                
                    {'x': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Impressions Fans'], 'type': 'lines', 'name': 'Impressions Fans'},
                    
                    {'x': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Impressions Fans Paid'], 'type': 'lines', 'name': 'Impressions Fans Paid'},
                    
                    {'x': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Enganged Users'], 'type': 'lines', 'name': 'Enganged Users'},
                    
                    {'x': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Impressions Viral'], 'type': 'lines', 'name': 'Impressions Viral'},
                    
                    {'x': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Total Reactions'],   'type': 'lines', 'name': 'Total Reactions'},

                    {'x': df_page_fans_short['Date'], 'y': df_page_fans_short['Page Fans'],   'type': 'lines', 'name': 'Page Fans'}

            ])
    
    figure_posts = {
        
    'data': traces_posts_cont,
    'layout': {'title':'Message: '+df_posts_cont[df_posts_cont['ID']==posts_ticker_cont]['Message'].values[0]}
    }
    return figure_posts

@app.callback(
    Output('linegraph_posts_cont_age_gender', 'figure'),
    [Input('submit-button-posts-cont', 'n_clicks')],
    [State('my_ticker_symbol_post_cont', 'value')])
def update_age_gender_period(n_clicks, posts_ticker_cont):
    #dates when post is alive
    # if post is not dead, dateEnd= the latest alive date 
    
    dateStart = (df_posts_cont[(df_posts_cont['ID']==posts_ticker_cont) & (df_posts_cont['STATUS']=='START')]['Date Fetched'].values[0])

    if(len(df_posts_cont[(df_posts_cont['ID']==posts_ticker_cont) & (df_posts_cont['STATUS']=='DEAD')]['Date Fetched'].values)==0):
        dateEnd = (df_posts_cont[(df_posts_cont['ID']==posts_ticker_cont) & (df_posts_cont['STATUS']=='ALIVE')]['Date Fetched'].values[-1])
    else:
        dateEnd = (df_posts_cont[(df_posts_cont['ID']==posts_ticker_cont) & (df_posts_cont['STATUS']=='DEAD')]['Date Fetched'].values[0])
 
    df_age_gender_func = df_ag.loc[(df_ag['Date']>=dateStart) & (df_ag['Date']<=dateEnd),:]

    traces_age_gender=([
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['F.13-17'], 'type': 'lines', 'name': 'F.13-17'},
                
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['F.18-24'], 'type': 'lines', 'name': 'F.18-24'},
                
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['F.25-34'], 'type': 'lines', 'name': 'F.25-34'},
                
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['F.35-44'], 'type': 'lines', 'name': 'F.35-44'},
                
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['F.45-54'], 'type': 'lines', 'name': 'F.45-54'},
                
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['F.55-64'], 'type': 'lines', 'name': 'F.55-64'},
                
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['F.65+'],   'type': 'lines', 'name': 'F.65+'},

                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['M.13-17'], 'type': 'lines', 'name': 'M.13-17'},
                
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['M.18-24'], 'type': 'lines', 'name': 'M.18-24'},
                
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['M.25-34'], 'type': 'lines', 'name': 'M.25-24'},
                
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['M.35-44'], 'type': 'lines', 'name': 'M.35-44'},
                
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['M.45-54'], 'type': 'lines', 'name': 'M.45-54'},
                
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['M.55-64'], 'type': 'lines', 'name': 'M.55-64'},
                
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['M.65+'], 'type': 'lines', 'name': 'M.65+'}

    ])
    figure_age_gender = {
        
    'data': traces_age_gender,
    'layout': {'font': graph_fonts,
            'title':'Lines of Each Age-Gender Group at Specific Post Dates',
            'background':'#fffff2'}
    }
    return figure_age_gender


@app.callback(
    Output('linegraph_posts_cont_regions', 'figure'),
    [Input('submit-button-posts-cont', 'n_clicks')],
    [State('my_ticker_symbol_post_cont', 'value')])
def update_regions_period(n_clicks, posts_ticker_cont):
    traces_regions_cont = []

    dateStart = (df_posts_cont[(df_posts_cont['ID']==posts_ticker_cont) & (df_posts_cont['STATUS']=='START')]['Date Fetched'].values[0])

    if(len(df_posts_cont[(df_posts_cont['ID']==posts_ticker_cont) & (df_posts_cont['STATUS']=='DEAD')]['Date Fetched'].values)==0):
        dateEnd = (df_posts_cont[(df_posts_cont['ID']==posts_ticker_cont) & (df_posts_cont['STATUS']=='ALIVE')]['Date Fetched'].values[-1])
    else:
        dateEnd = (df_posts_cont[(df_posts_cont['ID']==posts_ticker_cont) & (df_posts_cont['STATUS']=='DEAD')]['Date Fetched'].values[0])

    df_function_regions = df_regions_fans.loc[(pd.to_datetime(df_regions_fans['Date Fetched'])>=dateStart) & (pd.to_datetime(df_regions_fans['Date Fetched'])<=dateEnd),:]

    traces_regions_cont=([
        {'x': df_function_regions[df_function_regions['Region']=='Central Macedonia, Greece']['Date Fetched'], 'y': df_function_regions[df_function_regions['Region']=='Central Macedonia, Greece']['Fans'], 'type': 'lines', 'name': 'Central Macedonia, Greece'},
                
                {'x': df_function_regions[df_function_regions['Region']=='Attica (region), Greece']['Date Fetched'], 'y': df_function_regions[df_function_regions['Region']=='Attica (region), Greece']['Fans'], 'type': 'lines', 'name': 'Attica (region), Greece'},
                
                {'x': df_function_regions[df_function_regions['Region']=='Western Greece, Greece']['Date Fetched'], 'y': df_function_regions[df_function_regions['Region']=='Western Greece, Greece']['Fans'], 'type': 'lines', 'name': 'Western Greece, Greece'},
                
                {'x': df_function_regions[df_function_regions['Region']=='Thessaly, Greece']['Date Fetched'], 'y': df_function_regions[df_function_regions['Region']=='Thessaly, Greece']['Fans'], 'type': 'lines', 'name': 'Thessaly, Greece'},
                
                {'x': df_function_regions[df_function_regions['Region']=='Epirus (region), Greece']['Date Fetched'], 'y': df_function_regions[df_function_regions['Region']=='Epirus (region), Greece']['Fans'], 'type': 'lines', 'name': 'Epirus (region), Greece'},
                
                {'x': df_function_regions[df_function_regions['Region']=='Eastern Macedonia and Thrace, Greece']['Date Fetched'], 'y': df_function_regions[df_function_regions['Region']=='Eastern Macedonia and Thrace, Greece']['Fans'], 'type': 'lines', 'name': 'Eastern Macedonia and Thrace, Greece'},
                
                {'x': df_function_regions[df_function_regions['Region']=='Crete, Greece']['Date Fetched'], 'y': df_function_regions[df_function_regions['Region']=='Crete, Greece']['Fans'],   'type': 'lines', 'name': 'Crete, Greece'},

    ])
    figure_regions = {

        'data': traces_regions_cont,
        'layout': {'font': graph_fonts,
                'title': 'Lines of Each Region at Specific Post Dates',
                'background':'#f9f1f1'}
    }
    return figure_regions


@app.callback(
    Output('text-bottom', 'children'),
    [Input('submit-button-posts-cont', 'n_clicks')],
    [State('my_ticker_symbol_post_cont', 'value')])
def update_date_alive(n_clicks, posts_ticker_cont):
    
    dateFrom = str(df_posts_cont[(df_posts_cont['ID']==posts_ticker_cont) & (df_posts_cont['STATUS']=='START')]['Date Fetched'].values[0])
    
    if(len(df_posts_cont[(df_posts_cont['ID']==posts_ticker_cont) & (df_posts_cont['STATUS']=='DEAD')]['Date Fetched'].values)==0):
        dateUntil = str(df_posts_cont[(df_posts_cont['ID']==posts_ticker_cont) & (df_posts_cont['STATUS']=='ALIVE')]['Date Fetched'].values[-1])
    else:
        dateUntil = str(df_posts_cont[(df_posts_cont['ID']==posts_ticker_cont) & (df_posts_cont['STATUS']=='DEAD')]['Date Fetched'].values[0])

    child = ['Post is alive from: '+dateFrom+' until: '+dateUntil]
    return child


if __name__ == '__main__':
    app.run_server(debug=True)