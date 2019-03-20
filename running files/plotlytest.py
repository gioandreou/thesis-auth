import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime
import pycountry
import pandas as pd


app = dash.Dash()

#excel imports
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

#reform dataframes and keep only the dates and data we need for the first appearance also
df_page_fans = df_page_fans[['Date','Page Fans']]
df_page_fans_short = df_page_fans.loc[(df_page_fans['Date']>=date1),:]
#df_test are those who are appeared first as deafult in the plot 
df_test_age_gender = df_ag.loc[(pd.to_datetime(df_ag['Date'])>=date1) & (pd.to_datetime(df_ag['Date'])<=date2),:]
df_test_diff = df_test_age_gender.diff()
df_test_regions = df_regions_fans.loc[(pd.to_datetime(df_regions_fans['Date Fetched'])>=date1) & (pd.to_datetime(df_regions_fans['Date Fetched'])<=date2),:]

#list of the posts' ids and messages
list_post_cont_ids = list(df_posts_cont['ID'])
list_post_cont_ids = list(set(list_post_cont_ids))
options_posts_cont=[]
for post_id in list_post_cont_ids:
    templist = list(set(df_posts_cont[df_posts_cont['ID']==post_id]['Message']))
    options_posts_cont.append({'label':'{} '.format( templist[0] ), 'value':post_id})


#print(df_test_regions)


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
                'title': 'Lines of each post'}}),

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
                'title': 'Lines of each age-gender group at specific post dates'}}),

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
                'title': 'Lines of each Region at specific post dates'}}),


],style={'border':'1px solid', 'border-radius': 10})


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
