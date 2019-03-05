import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd


app = dash.Dash()

df = pd.read_excel('excels/lite/lite-Ages-Gender.xlsx')

colors = {
    'background': '#ffffff',
    'text': '#191919'
}

app.layout = html.Div(children=[
    html.H1(
        children='FB PAGE PLOTS',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'fontFamily':'Helvetica'
        }
    ),

    html.Div(
        children='The Informations and Stats about the Fans of our Page',
        style={
            'textAlign': 'center',
            'color': colors['text'],
            'fontFamily':'Helvetica'
        }
    ),

    dcc.Graph(
        id='example-graph',
        figure={
            
            'data': [
                {'x': df['Date'], 'y': df['F.13-17'], 'type': 'lines', 'name': 'F.13-17'},
                {'x': df['Date'], 'y': df['F.18-24'], 'type': 'lines', 'name': 'F.18-24'},
                {'x': df['Date'], 'y': df['F.25-34'], 'type': 'lines', 'name': 'F.25-34'},
                {'x': df['Date'], 'y': df['F.35-44'], 'type': 'lines', 'name': 'F.35-44'},
                {'x': df['Date'], 'y': df['F.45-54'], 'type': 'lines', 'name': 'F.45-54'},
                {'x': df['Date'], 'y': df['F.55-64'], 'type': 'lines', 'name': 'F.55-64'},
                {'x': df['Date'], 'y': df['F.65+'],   'type': 'lines', 'name': 'F.65+'},

                {'x': df['Date'], 'y': df['M.13-17'], 'type': 'lines', 'name': 'M.13-17'},
                {'x': df['Date'], 'y': df['M.18-24'], 'type': 'lines', 'name': 'M.18-24'},
                {'x': df['Date'], 'y': df['M.25-34'], 'type': 'lines', 'name': 'M.25-24'},
                {'x': df['Date'], 'y': df['M.35-44'], 'type': 'lines', 'name': 'M.35-44'},
                {'x': df['Date'], 'y': df['M.45-54'], 'type': 'lines', 'name': 'M.45-54'},
                {'x': df['Date'], 'y': df['M.55-64'], 'type': 'lines', 'name': 'M.55-64'},
                {'x': df['Date'], 'y': df['M.65+'],   'type': 'lines', 'name': 'M.65+'}
            ],
            'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']
                },
                'title': 'Age and Gender of FB PAGE'
            }
        }
    )],
    style={'backgroundColor': colors['background']}
)

if __name__ == '__main__':
    app.run_server(debug=True)