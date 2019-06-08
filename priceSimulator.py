# -*- coding: utf-8 -*-

# importing the libraries
import dash 
import dash_core_components as dcc 
import dash_html_components as html 
import dash_bootstrap_components as dbc
import dash_table as dt
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output, State


df = pd.read_csv('datasets/indicators.csv')
rateDf = pd.read_csv('datasets/Rate.csv')

available_indicators = df['Indicator Name'].unique()


# creata app object of dash.Dash()  css: BOOTSTRAP, GRID, CERULEAN
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.CERULEAN])
server = app.server
# define title of app
app.title = "Price Simulator"

logo = html.Img(src="/assets/HSBC_logo.svg", height="50px")
title = dcc.Link(html.B(html.H2("Price Simulator")), href="/", className="navbar-brand")

def create_time_series(dff, bankName):
    return {
        'data': [go.Scatter(
                x=rateDf['Period'],
                y=rateDf[bankName],
                mode='lines+markers'
            )],
            'layout': {
                'height': 225,
                'margin': {'l': 20, 'b': 30, 'r': 10, 't': 10},
                'annotations': [{
                    'x': 0, 'y': 0.85, 'xanchor': 'left', 'yanchor': 'bottom',
                    'xref': 'paper', 'yref': 'paper', 'showarrow': False,
                    'align': 'left', 'bgcolor': 'rgba(255, 255, 255, 0.5)',
                    'text': bankName
                }],
                'yaxis': {'type': 'Rate%'},
                'xaxis': {'showgrid': True}
            }
    }


# Configure navbar 
nav_items = html.Ul(
    [dbc.NavItem(dbc.NavLink(html.H4("Home"), href="/page-1")),
     dbc.NavItem(dbc.NavLink(html.H4("Models"), href="/page-1")),
     dbc.NavItem(dbc.NavLink(html.H4("Reports"), href="/page-1")),
     dbc.NavItem(dbc.NavLink(html.H4("Login"), href="/page-1"))
    ],
    className="navbar-nav",
)

navBar_Header = html.Nav(
    dbc.Container(
        dbc.Row([
                dbc.Col(logo, width="auto"),
                dbc.Col(title, width="auto"),
                dbc.Col(nav_items, width="auto"),
            ],
            justify="between",
            align="center",            
            style={"width": "100%"},
        )
    ),
    className="navbar navbar-light navbar-expand-md bg-light sticky-top",
)

body_layout = html.Div([
    html.Div([
        html.Div([
            html.Div([
                html.B(html.Label('Proposition Selection')),
                dcc.Dropdown(
                    options =[
                        {'label': "Jade", 'value': "Jade"},
                        {'label': "Advance", 'value': "Advance"},
                        {'label': "Mass", 'value': "Mass"},
                    ],
                    multi = False,
                    value = "PropositionSelection",
                    placeholder = "Please a select proposition..."
                )
            ]),       
            html.Br(), 
            html.Div([            
                html.B(html.Label('Product Selection')),
                dcc.Dropdown(
                    options =[
                        {'label': "Saving Account", 'value': "SA"},
                        {'label': "Current Account", 'value': "CA"},
                        {'label': "Term Deposit", 'value': "TD"},
                    ],
                    multi = True,
                    value = "ProductSelection",
                    placeholder = "Please select products..."
                )
            ]),
            html.Br(),
            html.Div([   
                html.B(html.Label('Money Flow')),
                dcc.Dropdown(                
                    options =[
                        {'label': "Inflow Model", 'value': "Inflow"},
                        {'label': "OutFlow Model", 'value': "Outflow"},
                        {'label': "Internalflow Model", 'value': "Internalflow"},
                    ],
                    multi = True,
                    value = "ModelSelection",
                    placeholder = "Please select flows..."
                )
            ], style={'borderBottom': 'thin lightgrey solid'}),
            html.Br(),
            html.Div([
                dcc.Graph(id='HSBC-Rate',
                    figure = create_time_series(dff = rateDf, bankName = "HSBC")
                ),                
                dcc.Graph(id='CITI-Rate', 
                    figure = create_time_series(dff = rateDf, bankName = "CITI")
                ),
                dcc.Graph(id='HASE-Rate',
                    figure = create_time_series(dff = rateDf, bankName = "HASE")
                ),
                dcc.Graph(id='DBS-Rate',
                    figure = create_time_series(dff = rateDf, bankName = "DBS")
                ),
            ])

        ], style={'width': '30%','padding': '10px 20px', 'float': 'left'}),

        html.Div([
            html.B('Rate Table'),        
            dt.DataTable(
                id = "rateTable",
                columns = [{"name": i, "id": i} for i in rateDf.columns],
                data = rateDf.to_dict('records')
            )], style={'width': '70%','display': 'inline-block','float' : 'right', 'padding': '20px 20px' })
    ], style={
        'borderBottom': 'thin lightgrey solid',
        'backgroundColor': 'rgb(250, 250, 250)'        
    })
      
])















# Define layout
app.layout = html.Div([
    navBar_Header, body_layout    
])


# define server run option to lunch dash app
if __name__ == '__main__':
    app.run_server(debug = True)


