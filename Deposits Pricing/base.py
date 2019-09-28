'''
Longley's Economic Regression Data
Source: https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/longley.html

Author: Ashutosh Agrahari
Email ID: akagr.cse@gmail.com
'''

################################################
# Loading Library
################################################
import dash
from dash.dependencies import Input, Output, State
import dash_core_components as dcc 
import dash_html_components as html 
import plotly.graph_objs as go
import pandas as pd
import dash_table as dt 

################################################
# Loading the dataset 
################################################
modelData = pd.read_csv('assets/longley.csv')


################################################
# Initializing the app 
################################################
app = dash.Dash()
server = app.server
app.title= "Economic Model"


################################################
# App Layout 
################################################
app.layout= html.Div([
    html.Header(html.H1("Longley's Economic Regression Model"), style={'text-align':'center'}),
    html.H3(html.A("Source",href = "https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/longley.html"), style={'text-align':'center'}),
    html.Div(className="row", children=[
        html.Div(className="four columns", children=[
            dcc.Graph(id="EmployedPlot",
                figure = {
                    'data':[go.Scatter(
                        x = modelData['Period'],
                        y = modelData['Employed'],
                        mode = 'lines+markers'
                    )],
                    'layout': {
                        'title': "Employed Stat",
                        'yaxis': {'text': 'Employed Value'},
                        'xaxis': {'showgrid': True}
                    }
                }
            )
        ]),
        html.Div(className="three columns", children=[
            html.Div([
                html.B(html.Label('Dependent Variable')),
                dcc.Dropdown(
                    id="depvar",
                    options = [{"label":i, "value":i} for i in modelData.columns],
                    multi = False,                    
                    placeholder = "Please a select dependent variable..."
                )
            ]),       
            html.Br(),
            html.Div([
                html.B(html.Label('Independent Variables')),
                dcc.Dropdown(
                    id="indepvar",
                    options = [{"label":i, "value":i} for i in modelData.columns],
                    multi = True,                    
                    placeholder = "Please select independent variables..."                    
                )
            ]),       
            html.Br(),
            html.Div([
                html.B(html.Label('Start Period')),
                dcc.Dropdown(
                    options =[{"label":i, "value":i} for i in modelData["Period"]],
                    multi = False,
                    placeholder = "Please Model Start Period..."
                )
            ]),       
            html.Br(),
            html.Div([
                html.B(html.Label('End Period')),
                dcc.Dropdown(
                    options =[{"label":i, "value":i} for i in modelData["Period"]],
                    multi = False,
                    placeholder = "Please Model End Period..."
                )
            ]),       
            html.Br(),
            html.Button("Run Model", id="clickModelling"),
            html.H3(id='button-clicks'),            
        ]),
        html.Div(className="five columns", children=[
            html.B("Longley Dataset:"),
            html.Br(),
            dt.DataTable(
                id="modelDf",
                columns = [{"name":i, "id":i} for i in modelData.columns],
                data = modelData.to_dict('records'),
                style_cell={'width': '150px'},               
            )
        ]),
    ])    
]) 


################################################
# Call back code  
################################################
@app.callback(
    Output('button-clicks', 'children'),
    [Input('clickModelling', 'n_clicks')])
def clicks(n_clicks):
    return 'Button has been clicked {} times'.format(n_clicks)


################################################
# Calling the app to run on server  
################################################
if __name__ == '__main__':
    app.run_server(debug=True)