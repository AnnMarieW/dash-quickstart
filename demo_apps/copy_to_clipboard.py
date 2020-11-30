import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ClientsideFunction
import pandas as pd


FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)
external_stylesheets = "https://codepen.io/chriddyp/pen/bWLwgP.css"

app = dash.Dash(__name__, external_stylesheets=[FONT_AWESOME, external_stylesheets])

with open('global_color_dict.py') as f:
    code = f.read()

fence = '"""'
code = ''.join([fence, code, fence])
print(code)

fence = '```'
code = ''.join([fence, code, fence])



disclosure = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna
aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint
occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. 
"""

code1 = """```
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

fig = px.scatter(df, x="gdp per capita", y="life expectancy",
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)

```"""



'''
===============================================================================
layout
'''

app.layout = html.Div(
    [
        html.Details(
            [
                html.Summary(
                    [
                        "Disclosure Statement",
                        html.Button(
                            id="copy",
                            n_clicks=0,
                            className="fa fa-copy",
                            style={"border": "none"},

                        ),
                    ]
                ),
                dcc.Markdown(id="disclosure", children=disclosure,),
            ],
            style={"borderStyle": "solid", "borderWidth": 1,},
        ),
        html.Details(
            [
                html.Summary(
                    [
                       "Code sample",
                        html.Button(
                            id="copy_code",
                            n_clicks=0,
                            className="fa fa-copy",
                            style={"margin": 10},
                        ),
                    ]
                ),
              #  html.Pre(html.Code(id="code", children=code)),
                dcc.Markdown(id="code", children= code),
            ],
            style={"borderStyle": "solid", "borderWidth": 1,},
        ),

        html.Div(dcc.Textarea(placeholder='paste here'))

    ]
)


app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="copyToClipboard"),
    Output("copy_code", "children"),
    Input("copy_code", "n_clicks"),
    State("code", "children"),
)


app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="copyToClipboard"),
    Output("copy", "children"),
    Input("copy", "n_clicks"),
    State("disclosure", "children"),
)


if __name__ == "__main__":
    app.run_server(debug=True)