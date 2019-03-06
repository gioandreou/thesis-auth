import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

df_posts = pd.read_excel('excels/lite/lite-Post-Info.xlsx')
#with pd.option_context('display.max_rows', None, 'display.max_columns', None):

print(df_posts.loc[df_posts['ID']=='974146599436745_974147879436617']['Impressions'].item())