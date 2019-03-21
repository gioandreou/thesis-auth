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

with pd.option_context('display.max_rows', None, 'display.max_columns', None):
    #print(df_family)
    print(df_occupation.columns)
    #ll = df_family[df_family['Region']=='Greece']['Total'].item()
    #print(ll)