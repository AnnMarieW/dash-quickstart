import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ClientsideFunction
import plotly.express as px
import pandas as pd
import dash_bootstrap_components as dbc
import dash_quickstart_text as tx


FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)

app = dash.Dash(external_stylesheets=[FONT_AWESOME, dbc.themes.SPACELAB,])


"""
===============================================================================
Make accordion
"""


def make_code_box(title, id_btn, id_md, intro, code):
    return html.Div(
        [
            html.Details(
                [
                    html.Summary(
                        [
                            title,
                            html.Button(
                                id=id_btn,
                                n_clicks=0,
                                className="fa fa-copy",
                                style={"border": "none"},
                            ),
                        ]
                    ),
                    dcc.Markdown(intro),
                    dcc.Markdown(id=id_md, children=code),
                ],
                style={"borderStyle": "solid", "borderWidth": 1,},
            ),
        ]
    )


"""
===============================================================================
Tab content
"""
quickstart_tab = (
    dbc.Row(
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Quickstart Apps")),
                    dbc.CardBody(
                        [
                            html.Div(
                                "Click on a section to see helpful links and code:",
                                className="mb-2",
                            ),
                            html.Div(
                                make_code_box(
                                    "Dash Hello World ",
                                    "copy_quickstart",
                                    "md_quickstart",
                                    tx.hello_world_intro,
                                    tx.hello_world_code,
                                )
                            ),
                            html.Div(
                                make_code_box(
                                    "Dash DataTable ",
                                    "copy_DataTable",
                                    "md_DataTable",
                                    tx.datatable_intro,
                                    tx.datatable_code,
                                )
                            ),
                            html.Div(
                                make_code_box(
                                    "dash-bootstrap",
                                    "copy_bootstrap",
                                    "md_bootstrap",
                                    tx.bootstrap_intro,
                                    tx.bootstrap_code,
                                )
                            ),
                            html.Div(
                                make_code_box(
                                    "dash-leaflet ",
                                    "copy_leaflet",
                                    "md_leaflet",
                                    tx.leaflet_intro,
                                    tx.leaflet_code,
                                )
                            ),
                            html.Div(
                                make_code_box(
                                    "Callbacks ",
                                    "copy_callback",
                                    "md_callback",
                                    tx.callback_intro,
                                    tx.callback_code,
                                )
                            ),
                            html.Div(
                                make_code_box(
                                    "Callback extras ",
                                    "copy_callback_extras",
                                    "md_callback_extras",
                                    tx.callback_extras_intro,
                                    "",
                                )
                            ),
                            html.Div(
                                make_code_box(
                                    "Pattern Matching Callbacks",
                                    "copy_pattern_match",
                                    "md_pattern_match",
                                    tx.pattern_match_intro,
                                    tx.pattern_match_code,
                                )
                            ),
                            html.Div(
                                make_code_box(
                                    "Datasets ",
                                    "copy_datasets",
                                    "md_datasets",
                                    tx.datasets_intro,
                                    tx.datasets_code,
                                )
                            ),
                            html.Div(
                                make_code_box(
                                    "Dash Components",
                                    "copy_components",
                                    "md_components",
                                    tx.components_intro,
                                    "",
                                ),
                            ),
                        ]
                    ),
                ]
            ),
            width=10,
            className="m-4",
        )
    ),
)

tips_tab = [
    dbc.Row(
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Tips & Tricks")),
                    dbc.CardBody([dcc.Markdown(tx.tips_text),]),
                ]
            ),
            width=8,
            className="m-4",
        )
    ),
    dbc.Row(
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Debugging")),
                    dbc.CardBody([dcc.Markdown(tx.debugging_text),]),
                ]
            ),
            width=8,
            className="m-4",
        )
    ),
]


howto_tab = (
    dbc.Row(
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("How To Guide")),
                    dbc.CardBody([dcc.Markdown(tx.howto_text),]),
                ]
            ),
            className="m-4",
        )
    ),
)

more_tab = (
    dbc.Row(
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Where to find more help:")),
                    dbc.CardBody([dcc.Markdown(tx.more_text),]),
                ]
            ),
            className="m-4",
        )
    ),
)


"""
===============================================================================
layout
"""

app.layout = dbc.Container(
    [
        dbc.Jumbotron(
            [
                html.H1("Dash Quickstart", className="text-white"),
                html.H4(
                    "A collection of quickstart apps and Tips & Tricks",
                    className="text-white",
                ),
            ],
            className="text-center bg-primary",
        ),
        dbc.Tabs(
            [
                dbc.Tab(quickstart_tab, label="Quickstart"),
                dbc.Tab(howto_tab, label="How To"),
                dbc.Tab(tips_tab, label="Tips & Tricks"),
                dbc.Tab(more_tab, label="More Resources"),
            ]
        ),
    ],
    fluid=True,
)


"""
===============================================================================
Callbacks
"""

quickstart_codebocks = [
    "quickstart",
    "DataTable",
    "bootstrap",
    "leaflet",
    "callback",
    "pattern_match",
    "datasets",
]
[
    app.clientside_callback(
        ClientsideFunction(namespace="clientside", function_name="copyToClipboard"),
        Output("copy_" + i, "children"),
        Input("copy_" + i, "n_clicks"),
        State("md_" + i, "children"),
    )
    for i in quickstart_codebocks
]


if __name__ == "__main__":
    app.run_server(debug=True)
