"""
This app is a quickstart guide for Plotly Dash app

hosted at: https://dashquickstart.pythonanywhere.com/

All of the markdown content is in the text_*.py files
 todo:  https://www.xaprb.com/blog/how-to-style-images-with-markdown/
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

app = dash.Dash(__name__, external_stylesheets=[FONT_AWESOME, dbc.themes.SPACELAB,])



"""
===============================================================================
Make code box
"""


def make_code_box(title, id, children):
    """
    :param title: text to show when twistie box is closed
    :param id of the code box
    :param children: content to copy to the clipboard - typically a code block
    :return: a div with a twistie box
    """
    return html.Div(
        [
            html.Details(
                open=False,
                id="open_"+id,
                children=[
                    html.Summary(
                        [
                            title,
                            html.Button(
                                id="copy_"+id,
                                n_clicks=0,
                                className="fa fa-copy",
                                style={"border": "none"},
                            ),
                        ]
                    ),
                    dcc.Markdown(id="md_"+id, children=children, className="p-2"),
                ],
                className="shadow mt-2",
            ),
        ]
    )


"""
===============================================================================
Quickstart Tab content
   (remember to add id's to clientside callback list)
"""


quickstart_tab = (
    dbc.Card(
        [
            dbc.CardHeader(html.H4("Quickstart Links and Apps")),
            dbc.CardBody(
                [
                    dbc.Row(
                        [
                            dbc.Col(
                                html.Div(
                                    "cntr-click on link to open in new browser window",
                                    style={"font-size": "75%"},
                                ),
                                width=3,
                            ),
                            dbc.Col(
                                dbc.Button("open/close all code boxes", id="open_button", size="sm"),
                            ),
                        ],
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                [dcc.Markdown(qstart.hello_world_intro)],
                                width=3,
                                className="border-right",
                            ),
                            dbc.Col(
                                make_code_box(
                                    "Dash Hello World quickstart code",
                                    "quickstart",
                                    qstart.hello_world_code,
                                ),
                            ),
                        ],
                        className="border mt-1",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Markdown(qstart.datatable_intro,),
                                width=3,
                                className="border-right",
                            ),
                            dbc.Col(
                                [
                                    make_code_box(
                                        "Dash DataTable quickstart code ",
                                        "DataTable",
                                        qstart.datatable_code,
                                    ),
                                    make_code_box(
                                        "Dash DataTable conditional formatting quickstart code ",
                                        "conditional_formatting",
                                        qstart.conditional_formatting_code,
                                    ),
                                ],
                            ),
                        ],
                        className="border",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Markdown(qstart.bootstrap_intro,),
                                width=3,
                                className="border-right",
                            ),
                            dbc.Col(
                                make_code_box(
                                    "dash-bootstrap quickstart",
                                    "bootstrap",
                                    qstart.bootstrap_code,
                                ),
                            ),
                        ],
                        className="border",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Markdown(qstart.leaflet_intro,),
                                width=3,
                                className="border-right",
                            ),
                            dbc.Col(
                                make_code_box(
                                    "dash-leaflet quickstart",
                                    "leaflet",
                                    qstart.leaflet_code,
                                ),
                            ),
                        ],
                        className="border",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Markdown(qstart.callback_intro),
                                width=3,
                                className="border-right",
                            ),
                            dbc.Col(
                                make_code_box(
                                    "Callbacks quickstart",
                                    "callback",
                                    qstart.callback_code,
                                ),
                            ),
                        ],
                        className="border",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Markdown(qstart.callback_extras_intro),
                                width=3,
                                className="border-right",
                            ),
                            dbc.Col(
                                make_code_box(
                                    "Advanced Callbacks Cheatsheet",
                                    "callback_extras",
                                    qstart.callback_extras_code,
                                ),
                            ),
                        ],
                        className="border",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Markdown(qstart.pattern_match_intro),
                                width=3,
                                className="border-right",
                            ),
                            dbc.Col(
                                make_code_box(
                                    "Pattern Matching Callbacks",
                                    "pattern_match",
                                    qstart.pattern_match_code,
                                ),
                            ),
                        ],
                        className="border",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Markdown(qstart.datasets_intro),
                                width=3,
                                className="border-right",
                            ),
                            dbc.Col(
                                make_code_box(
                                    "Plotly and Pandas Datasets",
                                    "datasets",
                                    qstart.datasets_code,
                                ),
                            ),
                        ],
                        className="border",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Markdown(qstart.components_intro),
                                width=3,
                                className="border-right",
                            ),
                        ],
                        className="border",
                    ),
                    dbc.Row(
                        [
                            dbc.Col(
                                dcc.Markdown(qstart.figure_intro),
                                width=3,
                                className="border-right",
                            ),
                        ],
                        className="border",
                    ),
                ]
            ),
        ],
        className="m-4",
    ),
)


"""
===============================================================================
How to Tab - content
"""


def make_image_row(id, howto_image):
    """
    :param id: str id for the modal
    :param howto_image:  image
    :return: row for with a modal to enlarge the image when clicked on
    """

    return html.Div(
        [
            html.Div(
                [
                    html.Div("click on image to enlarge", className="ml-4"),
                    html.Img(
                        id={"type": "row_modal", "index": id},
                        src=howto_image,
                        width=150,
                        height=125,
                    ),
                ],
                className="ml-4 mb-4",
            ),
            dbc.Modal(
                dbc.ModalBody(html.Img(src=howto_image)),
                id={"type": "modal", "index": id},
                scrollable=True,
                size="xl",
            ),
        ],
    )


howto_tab = html.Div(
    [
        ## DATATABLES
        #
        html.H3("DataTables", className="bg-primary text-white my-4"),
        # DataTable Formatting numbers
        dcc.Markdown(howto.datatable_format_numbers),
        #make_image_row("format_numbers", howto.datatable_format_numbers_image),

        # DataTable Formatting dates
        dcc.Markdown(howto.datatable_format_dates),
        html.Div(
            make_code_box(
                "formatting dates  example code",
                "formatting_dates",
                howto.datatable_format_dates_code,
            ),
            className="ml-4",
        ),

        # DataTable Move export button
        dcc.Markdown(howto.datatable_move_export_button),
        html.Div(
            make_code_box(
                "move the export and toggle buttons  example code",
                "move_export",
                howto.datatable_move_export_button_code
            ),
            className="ml-4",
        ),


        # DataTable Conditional formatting
        dcc.Markdown(howto.datatable_conditional_formatting),
        dcc.Markdown(howto.datatable_conditional_formatting2),
        html.Div(
            make_code_box(
                "conditional formatting example code",
                "conditional_formatting2",
                howto.datatable_conditional_formatting2_code,
            ),
            className="ml-4",
        ),
        # DataTable Sparklines
        dcc.Markdown(howto.datatable_spark_intro),
        make_image_row("dt_spark", howto.datatable_spark_image),
        # DataTable Markdown (row edges)
        dcc.Markdown(howto.datatable_fix_cut_off),
        #
        ## BOOTSTRAP
        #
        html.H3("Bootstrap", className="bg-primary text-white my-4"),
        # Bootstrap - progress bar
        dcc.Markdown(howto.bootstrap_live_stages),
        make_image_row("dbc_stages", howto.bootstrap_live_stages_image),
        # Bootstrap - modal
        dcc.Markdown(howto.bootstrap_modal),
        #
        ## MARKDOWN
        #
        html.H3("Markdown", className="bg-primary text-white my-4"),
        # Markdoown - bootstrap fixes
        dcc.Markdown(howto.markdown_css),
        #dcc.Markdown(howto.markdown_css_code, className="ml-4"),
        html.Div(
            make_code_box(
                "CSS for styling blockquotes and tables",
                "markdown_css",
                howto.markdown_css_code
            ),
            className="ml-4",
        ),
        # Markdown - image size
        dcc.Markdown(howto.markdown_image_size),
        #
        ## Dash DAQ
        #
        html.H3("Dash DAQ", className="bg-primary text-white my-4"),
        #
        dcc.Markdown(howto.dash_daq),
        html.Div(
            make_code_box(
                "dash daq style with css example code",
                "dash_daq",
                howto.dash_daq_code
            ),
            className="ml-4",
        ),
        dcc.Markdown(howto.dash_daq2),


        ## GENERAL
        #
        html.H3("General", className="bg-primary text-white my-4"),
        # Multi-page
        dcc.Markdown(howto.gen_multi_page),
        # Pattern Matching
        dcc.Markdown(howto.gen_pattern_matching),
        make_image_row("pattern_match", howto.gen_pattern_matching_image),
        # Tabulator
        dcc.Markdown(howto.gen_tabulator),
        make_image_row("tabulator", howto.gen_tabulator_image),
        # Graphing
        dcc.Markdown(howto.gen_image_in_bubble),
        make_image_row("bubble", howto.gen_image_in_bubble_image),
        dcc.Markdown(howto.gen_real_time_data),
        make_image_row("real_time", howto.gen_real_time_data_image),
        # Copy
        #dcc.Markdown(howto.gen_copy_to_clipboard),
        # Deployment
        dcc.Markdown(howto.deployment),
        # Options
        dcc.Markdown(howto.gen_options),
        html.Div(
            make_code_box(
                "dropdown options example code",
                "dropdown_options",
                howto.gen_options_code,
            ),
            className="ml-4",
        ),
    ], className='m-4'
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
                dbc.Tab(
                    dcc.Markdown(tips.tips, className="mt-4"), label="Tips & Tricks"
                ),
                dbc.Tab(
                    dcc.Markdown(more.more_text, className="mt-4"),
                    label="More Resources",
                ),
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
    "conditional_formatting",
    "callback_extras",
    "bootstrap",
    "leaflet",
    "callback",
    "pattern_match",
    "datasets",
    # in howto tab
    "formatting_dates",
    "move_export",
    "conditional_formatting2",
    "dropdown_options",
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
    [Output("open_" + i,'open') for i in quickstart_codebocks],
    Input("open_button", "n_clicks"),
    State("open_quickstart",'open'),
)
def open_twistie(n, open):
    if n:
        return [not open] * len(quickstart_codebocks)
    return [open] * len(quickstart_codebocks)



@app.callback(
    Output({"type": "modal", "index": MATCH}, "is_open"),
    Input({"type": "row_modal", "index": MATCH}, "n_clicks"),
)
def open_row_modal(n):
    """ opens a model in the how-to tables"""
    return True if n else False


if __name__ == "__main__":
    app.run_server(debug=True)
