"""
This app is a quickstart guide for Plotly Dash app

hosted at: https://dashquickstart.pythonanywhere.com/
(amw .com finxter)

This is the main app.  Content for each tab is in the files:  text_*.py
To update the quickstart app....
  etc - tbd

"""


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State, ClientsideFunction, MATCH
import dash_bootstrap_components as dbc

# app content
import text_quickstart as qstart
import text_more as more
import text_tips as tips
import text_howto as howto


FONT_AWESOME = (
    "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css"
)

app = dash.Dash(external_stylesheets=[FONT_AWESOME, dbc.themes.SPACELAB,])


"""
===============================================================================
Make code box
"""


def make_code_box(title, id_btn, id_md, intro, code):
    """
    :param title: text to show when twistie box is closed
    :param id_btn: id of the copy button
    :param id_md: id of the content to copy to clipboard
    :param intro: markdown content that does not get copied with button click
    :param code: content to copy to the clipboard - typically a code block
    :return: a div with a twistie box
    """
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
Tables for Howto Tab  - functions to create the rows
"""

def make_image_row(id, howto_text, howto_image):
    """
    :param id: str id for the modal
    :param howto_text: text for the first column
    :param howto_image:  image for the second column
    :return: row for the table with a modal to enlarge the image when clicked on
    """

    row_modal = html.Div(
        dbc.Modal(
            dbc.ModalBody(html.Img(src=howto_image)),
            id={'type': "modal", 'index':id},
            scrollable=True,
            size="xl",
        ),
    )
    row = html.Tr(
        [
            html.Td(
                html.Div(dcc.Markdown(howto_text),style={"maxHeight": 250, "minWidth": 400, "overflow": "auto"}),
            ),
            html.Td(
                [
                    "click on image to enlarge",
                    html.Div(
                        html.Img(id={'type': "row_modal", 'index':id},
                                 src=howto_image, width=500),
                        style={"maxHeight": 250, "overflow": "auto"},
                    ),
                ]
            ),
            row_modal,
        ],
    )
    return row

def make_md_row(howto_text, example_text):
    """

    :param howto_text: text for the first column
    :param example_text: text for the second column
    :return: row for the table
    """
    return html.Tr(
        [
            html.Td(dcc.Markdown(howto_text)),
            html.Td(
                html.Div(
                    dcc.Markdown(example_text),
                    style={"maxHeight": 250, "maxWidth": 500, "overflow": "auto"},
                )

            ),
        ]
    )

def make_dbc_row(title, table_name):
    return dbc.Row(
        dbc.Col(
            [
                html.H5(title),
                table_name,
            ],
            className="my-4",
        ),
    )


"""
===============================================================================
Build the tables  -- add new content here
"""

table_header = [html.Thead(html.Tr([html.Th("How To"), html.Th("Example")]))]

howto_datatables= dbc.Table(
    table_header
    +
    [html.Tbody(
        [
            make_image_row("dt_format", howto.datatable_format_numbers, howto.datatable_format_numbers_image),
            make_md_row(howto.datatable_move_export_button, howto.datatable_move_export_button_code),
            make_md_row(howto.datatable_conditional_formatting, ""),
            make_md_row(howto.datatable_conditional_formatting2, howto.datatable_conditional_formatting2_code),
            make_md_row(howto.datatable_fix_cut_off, ""),
        ]
    )],
    bordered=True
)

howto_bootstrap= dbc.Table(
    table_header
    +
    [html.Tbody(
        [
            make_image_row("dbc_stages", howto.bootstrap_live_stages, howto.bootstrap_live_stages_image),
            make_md_row(howto.bootstrap_modal, ""),
        ]
    )],
    bordered=True
)


howto_deployment= dbc.Table(
    table_header
    +
    [html.Tbody(
        [
            make_md_row( howto.deployment_heroku,""),
            make_md_row(howto.deployment_pythonanywhere, ""),
        ]
    )],
    bordered=True
)


howto_general= dbc.Table(
    table_header
    +
    [html.Tbody(
        [
            make_image_row('pattern_match', howto.gen_pattern_matching, howto.gen_pattern_matching_image),
            make_image_row("tabulator", howto.gen_tabulator, howto.gen_tabulator_image),
            make_image_row("bubble",howto.gen_image_in_bubble, howto.gen_image_in_bubble_image),
            make_image_row("real_time",howto.gen_real_time_data, howto.gen_real_time_data_image),

        ]
    )],
    bordered=True
)




"""
===============================================================================
Quickstart Tab content
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
                            make_code_box(
                                "Dash Hello World ",
                                "copy_quickstart",
                                "md_quickstart",
                                qstart.hello_world_intro,
                                qstart.hello_world_code,
                            ),
                            make_code_box(
                                "Dash DataTable ",
                                "copy_DataTable",
                                "md_DataTable",
                                qstart.datatable_intro,
                                qstart.datatable_code,
                            ),
                            make_code_box(
                                "dash-bootstrap",
                                "copy_bootstrap",
                                "md_bootstrap",
                                qstart.bootstrap_intro,
                                qstart.bootstrap_code,
                            ),
                            make_code_box(
                                "dash-leaflet ",
                                "copy_leaflet",
                                "md_leaflet",
                                qstart.leaflet_intro,
                                qstart.leaflet_code,
                            ),
                            make_code_box(
                                "Callbacks ",
                                "copy_callback",
                                "md_callback",
                                qstart.callback_intro,
                                qstart.callback_code,
                            ),
                            make_code_box(
                                "Callback extras ",
                                "copy_callback_extras",
                                "md_callback_extras",
                                qstart.callback_extras_intro,
                                "",
                            ),
                            make_code_box(
                                "Pattern Matching Callbacks",
                                "copy_pattern_match",
                                "md_pattern_match",
                                qstart.pattern_match_intro,
                                qstart.pattern_match_code,
                            ),
                            make_code_box(
                                "Datasets ",
                                "copy_datasets",
                                "md_datasets",
                                qstart.datasets_intro,
                                qstart.datasets_code,
                            ),
                            make_code_box(
                                "Dash Components",
                                "copy_components",
                                "md_components",
                                qstart.components_intro,
                                "",
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


"""
================================================================================
Build How To Tab - determines order of the tables in the tab

"""
howto_tab = [
    make_dbc_row("DataTables", howto_datatables),
    make_dbc_row("Bootstrap", howto_bootstrap),
    make_dbc_row("General", howto_general),
    make_dbc_row("Deployment", howto_deployment),

]
"""
================================================================================
tips tabs - content

"""

tips_tab = [
    dbc.Row(
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Tips & Tricks")),
                    dbc.CardBody([dcc.Markdown(tips.tips_text),]),
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
                    dbc.CardBody([dcc.Markdown(tips.debugging_text),]),
                ]
            ),
            width=8,
            className="m-4",
        )
    ),
]


"""
================================================================================
More tab - content

"""



more_tab = (
    dbc.Row(
        dbc.Col(
            dbc.Card(
                [
                    dbc.CardHeader(html.H4("Where to find more help:")),
                    dbc.CardBody([dcc.Markdown(more.more_text),]),
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

# This adds the copy to clipboard functionality to code blocks.  Just add the ID of the
#  code block to this list
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



@app.callback(
    Output({'type': "modal", "index": MATCH}, "is_open"),
    Input({'type': "row_modal", "index": MATCH}, "n_clicks")
)
def open_row_modal(n):
    """ opens a model in the how-to tables"""
    return True if n else False





if __name__ == "__main__":
    app.run_server(debug=True)
