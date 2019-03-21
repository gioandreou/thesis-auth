import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime
import pycountry
import pandas as pd
import plotly.plotly as py
import plotly.graph_objs as go

colorss = {
    'bothgender':"#191226",
    'women':'#F2355B',
    'men':'#3B707F',
    'male1':'#31D2FF',
    'male2':'#2CBDE5',
    'male3':'#259DBF',
    'male4':'#18697F'
    'male5':'#0C3440'
}

app = dash.Dash()

df_family = pd.read_excel('excels/elstat/formated oikogeneiaki katastasi.xlsx')
df_education = pd.read_excel('excels/elstat/formated epipedo ekpaideusis.xlsx')

'''
with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    print(df_education)
    print(df_education.columns)
    #ll = df_family[df_family['Region']=='Greece']['Total'].item()
    #print(ll)
'''
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


bothGenderDefault_fam = go.Bar(
    x=x_bothGender_family,
    y=y_bothGender_family,
    name='Both Gender',
    text=percentagesBoth_family,
    marker=dict(
        color='#014021'
    )
)
menDefault_fam = go.Bar(
    x=x_men_family,
    y=y_men_family,
    name='Men',
    text=percentagesMen_family,
    marker=dict(
        color='#82C5FF'
    )
)
womenDefault_fam = go.Bar(
    x=x_women_family,
    y=y_women_family,
    name='Women',
    text=percentagesWomen_family,
    marker=dict(
        color='#CC5954'
    )
)
menDefault_edu = go.Bar(
    x=education_labels,
    y=y_men_edu,
    name='Men',
    text=percentagesMen_edu,
    marker=dict(
        color='#82C5FF'
    )
)
womenDefault_edu = go.Bar(
    x=education_labels,
    y=y_women_edu,
    name='Women',
    text=percentagesWomen_edu,
    marker=dict(
        color='#CC5954'
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
                style={'fontSize':24, 'marginLeft':'30px'}),
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
        color='#014021')
    )
    menDefault_func = go.Bar(
        x=x_men_family,
        y=y_men_func,
        name='Men',
        text=percentagesMen,
        marker=dict(
            color='#82C5FF')
    )
    womenDefault_dunc = go.Bar(
        x=x_women_family,
        y=y_women_func,
        name='Women',
        text=percentagesWomen,
        marker=dict(
            color='#CC5954')
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
            color='#82C5FF')
    )
    womenDefault_edu_func = go.Bar(
        x=education_labels,
        y=y_women_edu,
        name='Women',
        text=percentagesWomen_edu,
        marker=dict(
            color='#35A2FF')
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

if __name__ == '__main__':
    app.run_server(debug=True)
