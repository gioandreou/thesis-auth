# Import Supporting Libraries
import pandas as pd

# Import Dash Visualization Libraries
import dash_core_components as dcc
import dash_html_components as html
import dash_table_experiments as dt
import dash.dependencies
from dash.dependencies import Input, Output, State
import plotly


# Load datasets
US_STATES_URL = 'https://raw.githubusercontent.com/plotly/datasets/master/2014_usa_states.csv'
US_AG_URL = 'https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv'
df_st = pd.read_csv(US_STATES_URL)
df_ag = pd.read_csv(US_AG_URL)

app = dash.Dash(__name__)
server = app.server
app.layout = html.Div([
    html.H2('My Dash App'),
    dt.DataTable(
        id='my-datatable',
        rows=df_ag.to_dict('records'),
        editable=False,
        row_selectable=True,
        filterable=True,
        sortable=True,
        selected_row_indices=[]
    ),
    html.Div(id='selected-indexes'),
    dcc.Graph(
        id='datatable-subplots'
    )
], style={'width': '60%'})

@app.callback(Output('datatable-subplots', 'figure'),
              [Input('my-datatable', 'rows'),
               Input('my-datatable', 'selected_row_indices')])
def update_figure(rows, selected_row_indices):
    dff = pd.DataFrame(rows)
    fig = plotly.tools.make_subplots(
        rows=3, cols=1,
        subplot_titles=('Beef', 'Pork', 'Poultry'),
        shared_xaxes=True)
    marker = {'color': ['#0074D9']*len(dff)}
    for i in (selected_row_indices or []):
        marker['color'][i] = '#FF851B'
    fig.append_trace({
        'x': dff['state'],
        'y': dff['beef'],
        'type': 'bar',
        'marker': marker
    }, 1, 1)
    fig.append_trace({
        'x': dff['state'],
        'y': dff['pork'],
        'type': 'bar',
        'marker': marker
    }, 2, 1)
    fig.append_trace({
        'x': dff['state'],
        'y': dff['poultry'],
        'type': 'bar',
        'marker': marker
    }, 3, 1)
    fig['layout']['showlegend'] = False
    fig['layout']['height'] = 1000
    fig['layout']['width'] = 1200
    fig['layout']['margin'] = {
        'l': 40,
        'r': 10,
        't': 60,
        'b': 200
    }
    return fig


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


if __name__ == '__main__':
    app.run_server(debug=True)