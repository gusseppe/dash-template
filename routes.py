import dash_bootstrap_components as dbc
from dash import html
from dash.dependencies import Input, Output

from app import app

from utils.constants import home_page_location, gdp_page_location# iris_page_location

from pages.home import home
from pages.gdp import gdp
#from pages.iris import iris


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == home_page_location:
        return home.layout
    elif pathname == gdp_page_location:
        return gdp.layout
    # elif pathname == iris_page_location:
    #     return iris.layout
    # If the user tries to reach a different page, return a 404 message
    jumbotron = html.Div(
        dbc.Container(
            [
                html.H1("404: Not found", className="text-danger"),
                html.Hr(),
                html.P(f"The pathname {pathname} was not recognised..."),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-light rounded-3",
    )
    return jumbotron