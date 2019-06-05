import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash(external_stylesheets=[dbc.themes.CERULEAN])

dropdown = dbc.DropdownMenu(
    nav=True,
    in_navbar=True,
    label="Menu",
    children=[
        dbc.DropdownMenuItem("Entry 1"),
        dbc.DropdownMenuItem("Entry 2"),
        dbc.DropdownMenuItem(divider=True),
        dbc.DropdownMenuItem("Entry 3"),
    ],
)

logo = html.Img(src="/assets/HSBC_logo.svg", height="50px")

title = dcc.Link("Price Simulator", href="/", className="navbar-brand")

nav_items = html.Ul(
    [dbc.NavItem(dbc.NavLink("Page 1", href="/page-1")), dropdown],
    className="navbar-nav",
)

navBar_Header = html.Nav(
    dbc.Container(
        dbc.Row(
            [
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

app.layout = html.Div(
    navBar_Header,
)


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)