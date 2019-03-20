import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime
import pycountry
import pandas as pd


app = dash.Dash()

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
    
],style={'border':'1px solid', 'border-radius': 10})



if __name__ == '__main__':
    app.run_server(debug=True)
