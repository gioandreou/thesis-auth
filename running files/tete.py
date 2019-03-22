import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime
import pycountry
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go


app = dash.Dash()

df_occupation = pd.read_excel('excels/elstat/formated katastasi asxolias regions_.xlsx')

shadesblue=['#838B8B','#668B8B','#2F4F4F','#528B8B','#388E8E','#8FD8D8','#70DBDB']
shadesred=['#FFA07A','#FA8072','#E9967A','#F08080','#CD5C5C','#DC143C','#B22222']

#wont copy
elstat_regions = df_occupation['Region']
elstat_regions = list(set(elstat_regions))
options_region=[]
for region in elstat_regions:
    options_region.append({'label':'{} '.format(region), 'value':region})

#print(options_region)

#STYLES
colors = {
    'background': '#ffffff',
    'text': '#191919'}

graph_fonts={
    'family':'sans-serif',
    'size':'12',
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

agelist = df_occupation['Age'][1:15] #change 1->0 for Total Age bar
age_dict = {}
percent_age_dict={}
for age in agelist:
    age_dict.update({age:[]})
    percent_age_dict.update({age:[]})
#print(percent_age_dict)

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #print(df_family)
    #print(df_occupation.columns)
    #ll = df_family[df_family['Region']=='Greece']['Total'].item()
    #print(ll)
    occupation_labels = list(df_occupation.columns)
    occupation_labels=occupation_labels[3:14]
  
    for item in occupation_labels:
        for age in agelist:
            age_dict[age].append(df_occupation[(df_occupation['Region']=='Greece') & (df_occupation['Age']==age)][item].item())
            temp = round(df_occupation[(df_occupation['Region']=='Greece') & (df_occupation['Age']==age)][item].item() / df_occupation[(df_occupation['Region']=='Greece') & (df_occupation['Age']==age)]['Total'].item()*100,2)
            percent_age_dict[age].append(str(temp)+'%')
            
    #print(age_dict)
    #print(percent_age_dict)
    barlist=[]
    red=0
    blue=0
    for age in agelist:
        if 'F' in age: #Female
            barlist.append(
                go.Bar(
                    x=occupation_labels,
                    y=age_dict[age],
                    name=age,
                    text=percent_age_dict[age],
                    marker=dict(
                        color=shadesred[red])
                        )
                )
            red=red+1
        elif 'M' in age: #Male
            barlist.append(
                go.Bar(
                    x=occupation_labels,
                    y=age_dict[age],
                    name=age,
                    text=percent_age_dict[age],
                    marker=dict(
                        color=shadesblue[blue])
                        )
                )
            blue=blue+1
        else: #Total Age
            barlist.append(
                go.Bar(
                    x=occupation_labels,
                    y=age_dict[age],
                    name=age,
                    text=percent_age_dict[age],
                    marker=dict(
                        color='#6B8E23')
                        )
                )

app.layout = html.Div(children=[
    html.Div([
            html.H3('Select Region:', style=style_fonts),
            dcc.Dropdown(
            id='my_ticker_symbol_region',
            options=options_region,
            value=['Regions'],
            multi=False,
            style={'fontSize':16})],          
                style={'display':'inline-block', 'verticalAlign':'top', 'width':'30%'}),         
        html.Div([
            html.Button(
                id='submit-button-region',
                n_clicks=0,
                children='Submit',
                style={'fontSize':24, 'marginLeft':'30px'}),
                ], 
                style={'display':'inline-block'}),

    dcc.Graph(
        id='occupation-graph',
        figure={
            'data': barlist,
            'layout': { 'xaxis':{'tickfont':{'size':14,'color':'rgb(107, 107, 107)'},
                            'automargin':True,},
                    
                    'yaxis':{'title':'Scale',
                        'autorange':True,
                        'type':'log',
                        },
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': graph_fonts,
                    'bargap': 0.1, 
                    'bargroupgap': 0.1, 
                    'barmode': 'group', 
                    'title': 'Greece Occupation Status'}
            }),

])
@app.callback(
    Output('occupation-graph', 'figure'),
    [Input('submit-button-region', 'n_clicks'),
    Input('my_ticker_symbol_region', 'value')])
def update_occupation_graph(n_clicks, posts_ticker_cont):
    
    age_dict = {}
    percent_age_dict={}
    for age in agelist:
        age_dict.update({age:[]})
        percent_age_dict.update({age:[]})
    
    for item in occupation_labels:
        for age in agelist:
            age_dict[age].append(df_occupation[(df_occupation['Region']==posts_ticker_cont) & (df_occupation['Age']==age)][item].item())
            temp = round(df_occupation[(df_occupation['Region']==posts_ticker_cont) & (df_occupation['Age']==age)][item].item() / df_occupation[(df_occupation['Region']==posts_ticker_cont) & (df_occupation['Age']==age)]['Total'].item()*100,2)
            percent_age_dict[age].append(str(temp)+'%')

    barlist=[]
    red=0
    blue=0
    for age in agelist:
        if 'F' in age: #Female
            barlist.append(
                go.Bar(
                    x=occupation_labels,
                    y=age_dict[age],
                    name=age,
                    text=percent_age_dict[age],
                    marker=dict(
                        color=shadesred[red])
                        )
                )
            red=red+1
        elif 'M' in age: #Male
            barlist.append(
                go.Bar(
                    x=occupation_labels,
                    y=age_dict[age],
                    name=age,
                    text=percent_age_dict[age],
                    marker=dict(
                        color=shadesblue[blue])
                        )
                )
            blue=blue+1
        else: #Total Age
            barlist.append(
                go.Bar(
                    x=occupation_labels,
                    y=age_dict[age],
                    name=age,
                    text=percent_age_dict[age],
                    marker=dict(
                        color='#6B8E23')
                        )
                )
        
    occupation_figure={
            'data': barlist,
            'layout': { 'xaxis':{'tickfont':{'size':14,'color':'rgb(107, 107, 107)'},
                            'automargin':True,},
                    
                    'yaxis':{'title':'Scale',
                        'autorange':True,
                        'type':'log',
                        },
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': graph_fonts,
                    'bargap': 0.1, 
                    'bargroupgap': 0.1, 
                    'barmode': 'group', 
                    'title': posts_ticker_cont+' Occupation Status'}
            }
    return occupation_figure

if __name__ == '__main__':
    app.run_server(debug=True)
