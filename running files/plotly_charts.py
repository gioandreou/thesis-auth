import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


app = dash.Dash()

df_age_gender = pd.read_excel('excels/lite/lite-Ages-Gender.xlsx')

df_regions = pd.read_excel('excels/lite/RegionDF.xlsx')

df_page_info = pd.read_excel('excels/lite/lite-Page-Info.xlsx')

df_page_post = pd.read_excel('excels/lite/lite-Page-Post.xlsx')

colors = {
    'background': '#ffffff',
    'text': '#191919',
    'pattern':'Images/what-the-hex.png'
}
graph_fonts={
                    'family':'sans-serif',
                    'size':'18',
                    'color':colors['text']
                }
style_fonts = style={
            'textAlign': 'center',
            'color': colors['text'],
            'fontFamily':'Helvetica',
            'fontSize':'30px'
        }
app.layout = html.Div(children=[
    html.H1(
        children='Andreou George Thesis',
        style=style_fonts
    ),

    html.Div(
        children='The Informations and Stats about the Fans of our Page',
        style=style_fonts
    ),
    #Age-Gender
    dcc.Graph(
        id='age-gender',
        figure={
            
            'data': [
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
                'title': 'Age and Gender of FB PAGE'
            }
        }
    ),
    #Regions
    dcc.Graph(
        id='regions',
        figure={
            
            'data': [
                {'x': df_regions['Regions'], 'y': df_regions['Fans'], 'type': 'bar', 'name': 'Regions'},
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': graph_fonts,
                'title': 'Regions of Fans '
            }
        }
    ),
    #Page Info
    dcc.Graph(
        id='page-info',
        figure={
            
            'data': [
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
                    'size':'15px','color':'#000'
                },
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': graph_fonts,
                'title': 'Informations about the Page'
            }
        }
    ),
    #Post Info
    dcc.Graph(
        id='page-post',
        figure={
            
            'data': [
                {'x': df_page_post['Date'], 'y': df_page_post['Page Post Impressions'], 'type': 'lines', 'name': 'Page Post Impressions'},
                {'x': df_page_post['Date'], 'y': df_page_post['Page Post Engagements'], 'type': 'lines', 'name': 'Page Post Engagements'},
                {'x': df_page_post['Date'], 'y': df_page_post['Page Consumptios'], 'type': 'lines', 'name': 'Page Consumptios'},
                {'x': df_page_post['Date'], 'y': df_page_post['Page Post Impressions Paid'], 'type': 'lines', 'name': 'Page Post Impressions Paid'},
                {'x': df_page_post['Date'], 'y': df_page_post['Page Post Impressions Organic'], 'type': 'lines', 'name': 'Page Post Impressions Organic'},
                {'x': df_page_post['Date'], 'y': df_page_post['Page Post Impressions Viral'], 'type': 'lines', 'name': 'Page Post Impressions Viral'}
                
            ],
            'layout': {
                'legend':{
                    'size':'15px','color':'#000'
                },
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': graph_fonts,
                'title': 'Informations about the Post of the Page'
            }
        }
    ),

    ],
    style=style_fonts
)

if __name__ == '__main__':
    app.run_server(debug=True)