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

df_family = pd.read_excel('excels/elstat/formated oikogeneiaki katastasi.xlsx')
df_education = pd.read_excel('excels/elstat/formated epipedo ekpaideusis.xlsx')
df_occupation = pd.read_excel('excels/elstat/formated katastasi asxolias regions_.xlsx')

shadesblue=['#838B8B','#668B8B','#2F4F4F','#528B8B','#388E8E','#8FD8D8','#70DBDB']
shadesred=['#FFA07A','#FA8072','#E9967A','#F08080','#CD5C5C','#DC143C','#B22222']


#EDUCATION
education_labels = list(df_education.columns)
education_labels=education_labels[3:14] #3:end without Total column
y_men_edu=[]
y_women_edu=[]
for item in education_labels:
    y_men_edu.append(df_education[(df_education['Region']=='Greece') & (df_education['Gender']=='Male')][item].item())
    y_women_edu.append(df_education[(df_education['Region']=='Greece') & (df_education['Gender']=='Female')][item].item())

percentagesMen_edu=[]
percentagesWomen_edu=[]
for i in range(len(y_men_edu)):
    temp_men = round((df_education[(df_education['Region']=='Greece') & (df_education['Gender']=='Male')][education_labels[i]].item() / df_education[(df_education['Region']=='Greece') & (df_education['Gender']=='Male')]['Total'].item())*100,2)
    temp_men = str(temp_men)+'%'
    percentagesMen_edu.append(temp_men)

    temp_women = round((df_education[(df_education['Region']=='Greece') & (df_education['Gender']=='Female')][education_labels[i]].item() / df_education[(df_education['Region']=='Greece') & (df_education['Gender']=='Female')]['Total'].item())*100,2)
    temp_women = str(temp_women)+'%'
    percentagesWomen_edu.append(temp_women)



#FAMILY
family_labels = list(df_family.columns)
elstat_regions = df_family['Region']
options_region=[]
for region in elstat_regions:
    options_region.append({'label':'{} '.format(region), 'value':region})

x_bothGender_family=family_labels[1:9]
x_men_family=family_labels[10:18]
x_women_family=family_labels[19:27]

y_bothGender_family=[]
y_men_family=[]
y_women_family=[]

for item in x_bothGender_family:
    y_bothGender_family.append(df_family[df_family['Region']=='Greece'][item].item())
for item in x_men_family:
    y_men_family.append(df_family[df_family['Region']=='Greece'][item].item())
for item in x_women_family:
    y_women_family.append(df_family[df_family['Region']=='Greece'][item].item())

percentagesBoth_family=[]
percentagesMen_family=[]
percentagesWomen_family=[]

for i in range(len(y_bothGender_family)):
    temp = round((df_family[df_family['Region']=='Greece'][x_bothGender_family[i]].item()/df_family[df_family['Region']=='Greece']['Total'].item())*100,2)
    temp = str(temp)+'%'
    percentagesBoth_family.append(temp)  

for i in range(len(y_men_family)):
    temp = round((df_family[df_family['Region']=='Greece'][x_men_family[i]].item()/df_family[df_family['Region']=='Greece']['Men Total'].item())*100,2)
    temp = str(temp)+'%'
    percentagesMen_family.append(temp)

for i in range(len(y_women_family)):
    temp = round((df_family[df_family['Region']=='Greece'][x_women_family[i]].item()/df_family[df_family['Region']=='Greece']['Women Total'].item())*100,2)
    temp = str(temp)+'%'
    percentagesWomen_family.append(temp)

#OCCUPATION
agelist = df_occupation['Age'][1:15] #change 1->0 for Total Age bar
age_dict = {}
percent_age_dict={}

for age in agelist:
    age_dict.update({age:[]})
    percent_age_dict.update({age:[]})
occupation_labels = list(df_occupation.columns)
occupation_labels=occupation_labels[3:14]

for item in occupation_labels:
    for age in agelist:
        age_dict[age].append(df_occupation[(df_occupation['Region']=='Greece') & (df_occupation['Age']==age)][item].item())
        temp = round(df_occupation[(df_occupation['Region']=='Greece') & (df_occupation['Age']==age)][item].item() / df_occupation[(df_occupation['Region']=='Greece') & (df_occupation['Age']==age)]['Total'].item()*100,2)
        percent_age_dict[age].append(str(temp)+'%')

#BAR PLOTS
#Occupation
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

#family
bothGenderDefault_fam = go.Bar(
    x=x_bothGender_family,
    y=y_bothGender_family,
    name='Both Gender',
    text=percentagesBoth_family,
    marker=dict(
        color='#6B8E23'
    )
)
menDefault_fam = go.Bar(
    x=x_men_family,
    y=y_men_family,
    name='Men',
    text=percentagesMen_family,
    marker=dict(
        color=shadesblue[1]
    )
)
womenDefault_fam = go.Bar(
    x=x_women_family,
    y=y_women_family,
    name='Women',
    text=percentagesWomen_family,
    marker=dict(
        color=shadesred[1]
    )
)
#education
menDefault_edu = go.Bar(
    x=education_labels,
    y=y_men_edu,
    name='Men',
    text=percentagesMen_edu,
    marker=dict(
        color=shadesblue[-2]
    )
)
womenDefault_edu = go.Bar(
    x=education_labels,
    y=y_women_edu,
    name='Women',
    text=percentagesWomen_edu,
    marker=dict(
        color=shadesred[2]
    )
)


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

app.layout = html.Div(children=[
    html.H1(
            children='Elstat Demographic Data',
            style=style_fonts),
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
                style={'fontSize':24, 'marginLeft':'30px','border':'1px solid', 'border-radius': 20}),
                ], 
                style={'display':'inline-block'}),
    
    dcc.Graph(
        id='family-graph',
        figure={
            'data': [bothGenderDefault_fam,menDefault_fam,womenDefault_fam],
            'layout': { 'xaxis':{'tickfont':{'size':14,'color':'rgb(107, 107, 107)'},
                            'automargin':True,},
                    
                    'yaxis':{'title':'Log Scale',
                        'type':'log',
                        'autorange':True
                        },
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': graph_fonts,
                    'bargap': 0.1, 
                    'bargroupgap': 0.1, 
                    'barmode': 'relative', 
                    'title': 'Greece Family Status'}
            }),
    
    dcc.Graph(
        id='education-graph',
        figure={
            'data': [menDefault_edu,womenDefault_edu],
            'layout': { 'xaxis':{'tickfont':{'size':14,'color':'rgb(107, 107, 107)'},
                            'automargin':True,},
                    
                    'yaxis':{'title':'Scale',
                        
                        'autorange':True
                        },
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': graph_fonts,
                    'bargap': 0.1, 
                    'bargroupgap': 0.1, 
                    'barmode': 'relative', 
                    'title': 'Greece Education Status'}
            }),
    
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
            })

    
    
    
],style={'border':'1px solid', 'border-radius': 20})


@app.callback(
    Output('family-graph', 'figure'),
    [Input('submit-button-region', 'n_clicks')],
    [State('my_ticker_symbol_region', 'value')])
def update_regions_family(n_clicks, posts_ticker_cont):
    
    y_bothGender_func=[]
    y_men_func=[]
    y_women_func=[]
    for item in x_bothGender_family:
        y_bothGender_func.append(df_family[df_family['Region']==posts_ticker_cont][item].item())
    for item in x_men_family:
        y_men_func.append(df_family[df_family['Region']==posts_ticker_cont][item].item())
    for item in x_women_family:
        y_women_func.append(df_family[df_family['Region']==posts_ticker_cont][item].item())

    percentagesBoth=[]
    percentagesMen=[]
    percentagesWomen=[]
    for i in range(len(y_bothGender_func)):
        temp = round((df_family[df_family['Region']==posts_ticker_cont][x_bothGender_family[i]].item()/df_family[df_family['Region']==posts_ticker_cont]['Total'].item())*100,2)
        temp = str(temp)+'%'
        percentagesBoth.append(temp)
        
    for i in range(len(y_men_func)):
        temp = round((df_family[df_family['Region']==posts_ticker_cont][x_men_family[i]].item()/df_family[df_family['Region']==posts_ticker_cont]['Men Total'].item())*100,2)
        temp = str(temp)+'%'
        percentagesMen.append(temp)

    for i in range(len(y_women_func)):
        temp = round((df_family[df_family['Region']==posts_ticker_cont][x_women_family[i]].item()/df_family[df_family['Region']==posts_ticker_cont]['Women Total'].item())*100,2)
        temp = str(temp)+'%'
        percentagesWomen.append(temp)

    bothGenderDefault_func = go.Bar(
    x=x_bothGender_family,
    y=y_bothGender_func,
    name='Both Gender',
    text=percentagesBoth,
    marker=dict(
        color='#6B8E23')
    )
    menDefault_func = go.Bar(
        x=x_men_family,
        y=y_men_func,
        name='Men',
        text=percentagesMen,
        marker=dict(
            color=shadesblue[1])
    )
    womenDefault_dunc = go.Bar(
        x=x_women_family,
        y=y_women_func,
        name='Women',
        text=percentagesWomen,
        marker=dict(
            color=shadesred[1])
    )
    
    figure_regions_fam = {
            'data': [bothGenderDefault_func, menDefault_func, womenDefault_dunc],
            'layout': { 'xaxis':{'tickfont':{'size':14,'color':'rgb(107, 107, 107)'},
                            'automargin':True,},
                    
                    'yaxis':{'title':'Log Scale',
                        'type':'log',
                        'autorange':True
                        },
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': graph_fonts,
                    'bargap': 0.1, 
                    'bargroupgap': 0.1, 
                    'barmode': 'relative', 
                    'title': posts_ticker_cont+' Family Status'}
            }
    return figure_regions_fam


@app.callback(
    Output('education-graph', 'figure'),
    [Input('submit-button-region', 'n_clicks')],
    [State('my_ticker_symbol_region', 'value')])
def update_regions_education(n_clicks, posts_ticker_cont):
    y_men_edu=[]
    y_women_edu=[]
    for item in education_labels:
        y_men_edu.append(df_education[(df_education['Region']==posts_ticker_cont) & (df_education['Gender']=='Male')][item].item())
        y_women_edu.append(df_education[(df_education['Region']==posts_ticker_cont) & (df_education['Gender']=='Female')][item].item())


    percentagesMen_edu=[]
    percentagesWomen_edu=[]
    for i in range(len(y_men_edu)):
        temp_men = round((df_education[(df_education['Region']==posts_ticker_cont) & (df_education['Gender']=='Male')][education_labels[i]].item() / df_education[(df_education['Region']==posts_ticker_cont) & (df_education['Gender']=='Male')]['Total'].item())*100,2)
        temp_men = str(temp_men)+'%'
        percentagesMen_edu.append(temp_men)

        temp_women = round((df_education[(df_education['Region']==posts_ticker_cont) & (df_education['Gender']=='Female')][education_labels[i]].item() / df_education[(df_education['Region']==posts_ticker_cont) & (df_education['Gender']=='Female')]['Total'].item())*100,2)
        temp_women = str(temp_women)+'%'
        percentagesWomen_edu.append(temp_women)

    menDefault_edu_func = go.Bar(
        x=education_labels,
        y=y_men_edu,
        name='Men',
        text=percentagesMen_edu,
        marker=dict(
            color=shadesblue[-2])
    )
    womenDefault_edu_func = go.Bar(
        x=education_labels,
        y=y_women_edu,
        name='Women',
        text=percentagesWomen_edu,
        marker=dict(
            color=shadesred[2])
    )

    figure_regions_edu = {
            'data': [menDefault_edu_func,womenDefault_edu_func],
            'layout': { 'xaxis':{'tickfont':{'size':14,'color':'rgb(107, 107, 107)'},
                            'automargin':True,},
                    
                    'yaxis':{'title':'Scale',
                        
                        'autorange':True
                        },
                    'plot_bgcolor': colors['background'],
                    'paper_bgcolor': colors['background'],
                    'font': graph_fonts,
                    'bargap': 0.1, 
                    'bargroupgap': 0.1, 
                    'barmode': 'relative', 
                    'title': posts_ticker_cont+' Education Status'}
            }
    return figure_regions_edu


@app.callback(
    Output('occupation-graph', 'figure'),
    [Input('submit-button-region', 'n_clicks')],
    [State('my_ticker_symbol_region', 'value')])
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
