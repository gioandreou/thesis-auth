import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime
import pycountry
import pandas as pd


app = dash.Dash()


df_cont = pd.read_excel('excels/lite/lite-Post-Info-Countinuously.xlsx')

df_ag = pd.read_excel('excels/lite/lite-Ages-Gender.xlsx')

date1 = (df_cont[(df_cont['ID']=='974146599436745_974147879436617') & (df_cont['STATUS']=='START')]['Date Fetched'].values[0])
date2 = (df_cont[(df_cont['ID']=='974146599436745_974147879436617') & (df_cont['STATUS']=='DEAD')]['Date Fetched'].values[0])


df_test_age_gender = df_ag.loc[(df_ag['Date']>=date1) & (df_ag['Date']<=date2),:]
df_test_diff = df_test_age_gender.diff()

'''
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(date1)
    print(date2)
    print(df_test)
'''
list_post_ids = list(df_cont['ID'])
list_post_ids = list(set(list_post_ids))
options_posts_cont=[]

for post_id in list_post_ids:
    templist = list(set(df_cont[df_cont['ID']==post_id]['Message']))
    options_posts_cont.append({'label':'{} '.format( templist[0] ), 'value':post_id})

'''
print(list_post_ids)
print("---")
print(options_posts_cont)

print(df_cont[df_cont['ID']=='974146599436745_974147879436617']['Message'].values[0])

print(str(df_cont[(df_cont['ID']=='974146599436745_974147879436617') & (df_cont['STATUS']=='START')]['Date Fetched'].values[0]))
print(str(df_cont[(df_cont['ID']=='974146599436745_974147879436617') & (df_cont['STATUS']=='DEAD')]['Date Fetched'].values[0]))

'''

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
                {'x': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Impressions'],'text':df_cont[df_cont['ID']=='974146599436745_974147879436617']['STATUS'], 'type': 'lines', 'name': 'Impressions'},
                {'x': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Impressions Paid'], 'type': 'lines', 'name': 'Impressions Paid'},
                {'x': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Impressions Organic'], 'type': 'lines', 'name': 'Impressions Organic'},
                {'x': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Impressions Fans'], 'type': 'lines', 'name': 'Impressions Fans'},
                {'x': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Impressions Fans Paid'], 'type': 'lines', 'name': 'Impressions Fans Paid'},
                {'x': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Enganged Users'], 'type': 'lines', 'name': 'Enganged Users'},
                {'x': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Impressions Viral'], 'type': 'lines', 'name': 'Impressions Viral'},
                {'x': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Date Fetched'], 'y': df_cont[df_cont['ID']=='974146599436745_974147879436617']['Total Reactions'],   'type': 'lines', 'name': 'Total Reactions'}
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': graph_fonts,
                'title': 'Lines of each post'}}),

    html.P(
        id='text-bottom',
        children=['Post is alive from: '
            +str(df_cont[(df_cont['ID']=='974146599436745_974147879436617') & (df_cont['STATUS']=='START')]['Date Fetched'].values[0])
            +' until: '
            +str(df_cont[(df_cont['ID']=='974146599436745_974147879436617') & (df_cont['STATUS']=='DEAD')]['Date Fetched'].values[0])
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


    

],style={'border':'1px solid', 'border-radius': 10})
@app.callback(
    Output('linegraph_posts_cont_age_gender', 'figure'),
    [Input('submit-button-posts-cont', 'n_clicks')],
    [State('my_ticker_symbol_post_cont', 'value')])
def update_age_gender_period(n_clicks, posts_ticker_cont):
    date1 = (df_cont[(df_cont['ID']==posts_ticker_cont) & (df_cont['STATUS']=='START')]['Date Fetched'].values[0])
    date2 = (df_cont[(df_cont['ID']==posts_ticker_cont) & (df_cont['STATUS']=='DEAD')]['Date Fetched'].values[0])

    df_age_gender_func = df_ag.loc[(df_ag['Date']>=date1) & (df_ag['Date']<=date2),:]

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
                
                {'x': df_age_gender_func['Date'], 'y': df_age_gender_func['M.65+'],   'type': 'lines', 'name': 'M.65+'}

    ])
    figure_age_gender = {
        
    'data': traces_age_gender,
    #'layout': {'title':'Message: '+df_cont[df_cont['ID']==posts_ticker_cont]['Message'].values[0]}
    }
    return figure_age_gender




@app.callback(
    Output('my_graph_posts_cont', 'figure'),
    [Input('submit-button-posts-cont', 'n_clicks')],
    [State('my_ticker_symbol_post_cont', 'value')])
def update_graph_posts_cont(n_clicks, posts_ticker_cont):
    traces_posts_cont = []
    #for tic in posts_ticker_cont:
    
    traces_posts_cont=([
                    {'x': df_cont[df_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_cont[df_cont['ID']==posts_ticker_cont]['Impressions'], 'text':df_cont[df_cont['ID']==posts_ticker_cont]['STATUS'], 'type': 'lines', 'name': 'Impressions'},
                    
                    {'x': df_cont[df_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_cont[df_cont['ID']==posts_ticker_cont]['Impressions Paid'], 'type': 'lines', 'name': 'Impressions Paid'},
                
                    {'x': df_cont[df_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_cont[df_cont['ID']==posts_ticker_cont]['Impressions Organic'], 'type': 'lines', 'name': 'Impressions Organic'},
                
                    {'x': df_cont[df_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_cont[df_cont['ID']==posts_ticker_cont]['Impressions Fans'], 'type': 'lines', 'name': 'Impressions Fans'},
                    
                    {'x': df_cont[df_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_cont[df_cont['ID']==posts_ticker_cont]['Impressions Fans Paid'], 'type': 'lines', 'name': 'Impressions Fans Paid'},
                    
                    {'x': df_cont[df_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_cont[df_cont['ID']==posts_ticker_cont]['Enganged Users'], 'type': 'lines', 'name': 'Enganged Users'},
                    
                    {'x': df_cont[df_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_cont[df_cont['ID']==posts_ticker_cont]['Impressions Viral'], 'type': 'lines', 'name': 'Impressions Viral'},
                    
                    {'x': df_cont[df_cont['ID']==posts_ticker_cont]['Date Fetched'], 'y': df_cont[df_cont['ID']==posts_ticker_cont]['Total Reactions'],   'type': 'lines', 'name': 'Total Reactions'}

            ])
    
    figure_posts = {
        
    'data': traces_posts_cont,
    'layout': {'title':'Message: '+df_cont[df_cont['ID']==posts_ticker_cont]['Message'].values[0]}
    }
    return figure_posts

@app.callback(
    Output('text-bottom', 'children'),
    [Input('submit-button-posts-cont', 'n_clicks')],
    [State('my_ticker_symbol_post_cont', 'value')])
def update_date_alive(n_clicks, posts_ticker_cont):
    
    dateFrom = str(df_cont[(df_cont['ID']==posts_ticker_cont) & (df_cont['STATUS']=='START')]['Date Fetched'].values[0])
    dateUntil = str(df_cont[(df_cont['ID']==posts_ticker_cont) & (df_cont['STATUS']=='DEAD')]['Date Fetched'].values[0])
    
    child = ['Post is alive from: '+dateFrom+' until: '+dateUntil]
    return child


if __name__ == '__main__':
    app.run_server(debug=True)
