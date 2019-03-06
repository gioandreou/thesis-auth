import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader.data as web # requires v0.6.0 or later
from datetime import datetime
import pandas as pd
import plotly.graph_objs as go


app = dash.Dash()

df_posts = pd.read_excel('excels/lite/lite-Post-Info.xlsx')

list_post_ids = list(df_posts['ID'])

options_posts=[]

for post_id in list_post_ids:
    options_posts.append({'label':'{} '.format(df_posts.loc[df_posts['ID']==post_id]['Message'].item()), 'value':post_id})

app.layout =html.Div([
            html.H1('test',style={
                'textAlign': 'center',
                'color': '#191919',
                'fontFamily':'Helvetica',
                'fontSize':'30px'}),
            html.Div([
                html.H3('Select posts:', style={'paddingRight':'30px'}),
                dcc.Dropdown(
                id='my_ticker_symbol_posts',
                options=options_posts,
                value=['Post'],
                multi=False
            )
                ],          
                style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),
                html.Div([
                html.Button(
                id='submit-button-posts',
                n_clicks=0,
                children='Submit',
                style={'fontSize':24, 'marginLeft':'30px'}
            ),
            ], style={'display':'inline-block'}),
            dcc.Graph(
            id='my_graph_posts',
            figure={
                'data': [
                    {'x':['Impressions'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Impressions'],'type':'bar'},
                    {'x':['Impressions Paid'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Impressions Paid'],'type':'bar'},
                    {'x':['Impressions Organic'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Impressions Organic'],'type':'bar'},
                    {'x':['Impressions Fans'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Impressions Fans'],'type': 'bar'},
                    {'x':['Impressions Fans Paid'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Impressions Fans Paid'],'type': 'bar'},
                    {'x':['Enganged Users'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Enganged Users'],'type': 'bar'},
                    {'x':['Impressions Viral'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Impressions Viral'],'type': 'bar'},
                    {'x':['Total Reactions'], 'y': df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Total Reactions'],'type': 'bar'}
            ]
        })
                ])


@app.callback(
    Output('my_graph_posts', 'figure'),
    [Input('submit-button-posts', 'n_clicks')],
    [State('my_ticker_symbol_posts', 'value')])
def update_graph_posts(n_clicks, posts_ticker):
    traces_posts = []
    #for tic in posts_ticker:
    traces_posts=([
                    {'x':['Impressions'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Impressions'].item()],'type':'bar'},
                    {'x':['Impressions Paid'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Paid'].item()],'type':'bar'},
                    {'x':['Impressions Organic'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Organic'].item()],'type':'bar'},
                    {'x':['Impressions Fans'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Fans'].item()],'type':'bar'},
                    {'x':['Impressions Fans Paid'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Fans Paid'].item()],'type':'bar'},
                    {'x':['Enganged Users'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Enganged Users'].item()],'type':'bar'},
                    {'x':['Impressions Viral'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Impressions Viral'].item()],'type':'bar'},
                    {'x':['Total Reactions'], 'y': [df_posts.loc[df_posts['ID']==posts_ticker]['Total Reactions'].item()],'type':'bar'}
            ])
        
    figure_posts = {
    'data': traces_posts,
    'layout': {'title':'Message: '+df_posts.loc[df_posts['ID']==posts_ticker]['Message'].item()}}
    return figure_posts


if __name__ == "__main__":
    app.run_server()