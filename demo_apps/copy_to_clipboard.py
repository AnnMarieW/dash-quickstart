"""
Add this to a .js file in the assets folder in the app root directory


window.dash_clientside = Object.assign({}, window.dash_clientside, {
    clientside: {
        copyToClipboard: function (n, text) {
          if (!navigator.clipboard) {
            alert("copy not available, use ctrl-c");
            return;
          }
          if (n > 0) {
            // removes code block markdown syntax  ```
            const trimmed_text = text.replace(/(^```)|(```$)/g, '');
            navigator.clipboard.writeText(trimmed_text).then(function() {
                alert("Copied.  crl-v to paste")
              }, function() {
                alert('copy error')
              });
          }
        }
    }
});
"""



import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ClientsideFunction

FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)
external_stylesheets = "https://codepen.io/chriddyp/pen/bWLwgP.css"

app = dash.Dash(__name__, external_stylesheets=[FONT_AWESOME, external_stylesheets])


sample_code = """```
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


app.layout = html.Div(
    [
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
                dcc.Markdown(id="code", children= sample_code),
            ],
            style={"borderStyle": "solid", "borderWidth": 1,},
        ),
    ]
)


app.clientside_callback(
    ClientsideFunction(namespace="clientside", function_name="copyToClipboard"),
    Output("copy_code", "children"),  # this function has no output, but Dash requires an Output
    Input("copy_code", "n_clicks"),   # when the copy button is clicked on:
    State("code", "children"),        # copies the children of this component to the clipboard
)


if __name__ == "__main__":
    app.run_server(debug=True)
