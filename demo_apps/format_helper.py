
import dash
from dash.dependencies import Input, Output, State
import dash_table
import dash_table.FormatTemplate as FormatTemplate
from dash_table.Format import Format, Scheme, Symbol, Group, Align, Prefix, Sign
import dash_html_components as html
import dash_core_components as dcc

import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
from numpy.random import default_rng

rng = default_rng()


FONT_AWESOME = "https://use.fontawesome.com/releases/v5.10.2/css/all.css"

app = dash.Dash(
    __name__,
    suppress_callback_exceptions=True,
    external_stylesheets=[dbc.themes.BOOTSTRAP, FONT_AWESOME],
)

example_app_df = pd.DataFrame(
    {
        "Exchange": ["Canadian Dollar", "Euro", "Japanese Yen", "US Dollar"],
        "CAD": [1, 0.64, 78.91, 0.75],
        "EUR": [1.56, 1, 122.9, 1.17],
        "JPY": [0.013, 0.0081, 1, 0.0095],
        "USD": [1.33, 0.85, 104.96, 1],
    }
)
example_app_df = example_app_df.set_index("Exchange")


df = pd.DataFrame(
    {
        "A": np.random.randint(10000, size=4),
        "B": rng.standard_normal(size=4) / 10000,
        "C": [10 / 3, np.pi, np.e, np.euler_gamma],
        "D": rng.standard_normal(size=4) * 100000,
        "E": rng.standard_normal(size=4) * 1000000000000000,
        "NaN": [np.NAN, np.NAN, np.NAN, np.NAN],
    }
)


align_options = {
    "left": Align.left,
    "right": Align.right,
    "center": Align.center,
    "right sign": Align.right_sign,
}

group_options = ["Group.no", "Group.yes"]

padding_options = ["Padding.no", "Padding.yes"]

prefix_options = [
    Prefix.yocto,
    Prefix.zepto,
    Prefix.atto,
    Prefix.femto,
    Prefix.pico,
    Prefix.nano,
    Prefix.micro,
    Prefix.milli,
    "none",
    Prefix.kilo,
    Prefix.mega,
    Prefix.giga,
    Prefix.tera,
    Prefix.peta,
    Prefix.exa,
    Prefix.zetta,
    Prefix.yotta,
]

prefix_options_dict = {
    "y": Prefix.yocto,
    "z": Prefix.zepto,
    "a": Prefix.atto,
    "f": Prefix.femto,
    "p": Prefix.pico,
    "n": Prefix.nano,
    "µ": Prefix.micro,
    "m": Prefix.milli,
    "none": "None",
    "k": Prefix.kilo,
    "M": Prefix.mega,
    "G": Prefix.giga,
    "T": Prefix.tera,
    "P": Prefix.peta,
    "E": Prefix.exa,
    "Z": Prefix.zetta,
    "Y": Prefix.yotta,
}


scheme_value = [
    Scheme.exponent,
    # Scheme.fixed,
    Scheme.decimal_or_exponent,
    Scheme.decimal,
    Scheme.decimal_si_prefix,
    # Scheme.percentage,
    #  Scheme.percentage_rounded,
    Scheme.binary,
    Scheme.octal,
    Scheme.decimal_integer,
    Scheme.lower_case_hex,
    Scheme.upper_case_hex,
    Scheme.unicode,
]

scheme_label = [
    "e - exponent notation.",
    #  "f - fixed point notation.",
    "g - either decimal or exponent notation, rounded to significant digits.",
    "r - decimal notation, rounded to significant digits.",
    "s - decimal notation with an SI prefix, rounded to significant digits.",
    #  "% - multiply by 100, and then decimal notation with a percent sign.",
    #   "p - multiply by 100, round to significant digits, and then decimal notation with a percent sign.",
    "b - binary notation, rounded to integer.",
    "o - octal notation, rounded to integer.",
    "d - decimal notation, rounded to integer",
    "x - hexadecimal notation, using lower-case letters, rounded to integer.",
    "X - hexadecimal notation, using upper-case letters, rounded to integer.",
    "c - converts the integer to the corresponding unicode character before printing.",
]
scheme_options = dict(zip(scheme_label, scheme_value))

sign_options = ["sign.default", "Sign.negative", "Sign.parantheses", "Sign.space"]

symbol_options = [
    "Symbol.no",
    "Symbol.yes",
    "Symbol.binary",
    "Symbol.octal",
    "Symbol.hex",
]

trim_options = ["Trim.no", "Trim.yes"]


"""
===============================================================================
LAYOUT COMPONENTS
"""


def make_help_btn(id):
    return dbc.Button(
        "learn more",
        id=id,
        outline=True,
        className="float-right",
        color="info",
        size="sm",
      #  style={"border": None, "border-radius": "60%"},
    )


"""
===============================================================================
markdown text and help modals
"""

intro_text = dcc.Markdown(
    """
    When this app starts, you will see the default format for numerical data in a Dash Datatable. To present data in a 
    more "human readable" way, formatting can be applied to each column.  The `"format"` property is derived from the
    [d3-format](https://github.com/d3/d3-format) library.
    
    __Try formatting this Dash DataTable__ by selecting different options. The table is editable too, so you can enter 
    your own data.  See the Results section for the code that formats this table.  
    """
)

see_more_text = dcc.Markdown(
    """
    Looking for more information?  See also:    
    - FormatTemplate - a shortcut for the most common use cases: currency and percentage.  
    See the ["DataTable with template formatting" example](dash.plotly.com/datatable/typing)    
    - [Dash documentation - Typing](https://dash.plotly.com/datatable/typing)
    - [Dash DataTable reference](https://dash.plotly.com/datatable/reference)  
    - [Source code for Format object](https://github.com/plotly/dash-table/tree/dev/dash_table)
    - [d3-format library](https://github.com/d3/d3-format)
    """
)

symbol_text = dcc.Markdown(
    """
    __Percentage:__
    multiply by 100, and then decimal notation with a percent sign

    __Show symbol:__
    If selected, the default is "$".  You can override this by placing any symbol or text in the 
    prefix and/or suffix fields.   This is often used for currency, but you can use any symbol.  Try copy and paste one of these:

    € ₽ C$   £  °C °F ​​

    The prefix and suffix fields accepts one space character " "  if you would like to add spacing between the number and
     the symbol. 
"""
)


type_SI_text = (
    dcc.Markdown(
        """
    __Type__      
    From the [d3-format documentation](https://github.com/d3/d3-format) :  
    Depending on the type, the precision either indicates the number of digits that follow the decimal point 
    (types f and %), or the number of significant digits (types , e, g, r, s and p). If the precision is not specified, 
    it defaults to 6 for all types except  (none), which defaults to 12. Precision is ignored for integer formats 
    (types b, o, d, x, X and c). 

    Note:  In this demo app, f and % are selected in the Symbol and Precision sections.
    
    __SI Prefix__
    Learn more about SI prefix [here](https://en.wikipedia.org/wiki/Metric_prefix)  This method is useful when formatting 
    numbers in the same units for easy comparison.  
"""
    ),
)

precision_text = dcc.Markdown(
    """
    To set the number of decimal places:
    - select fixed point
    - enter a number in the precision field
    
    
    The default value for the decimal delimiter is "." but may be changed.  Many locales use a comma ","

    This will set the d3 type to "f".  See more about how precision is used with different types in the Type section.
"""
)

align_text = dcc.Markdown(
    """
    __Padding width__ is the minimum width of the field.  If width of the field is less than the minimum, fill 
    characters will be added

    The __Fill__ can be any character or symbol.

    __Align optons__  
     The first 3 are as you might expect.  The "right sign"  is like right-aligned but with any sign and symbol to the
      left of any padding.
"""
)

group_text = dcc.Markdown(
    """
    Grouping defaults to "thousands" (ie groups of three to the left of the decimal point) and the delimiter defaults 
    to ","  
    
    Any delimiter may be used and  "." is commonly used as a thousands separator in many locales.    

    The groupings may be an array of group sizes.  For example, you could format a 10 digit integer as a telephone number 
    with groups `[3, 3, 4]`.  Note -- this demo app only accepts one digit, but arrays of different sizes are valid.  
     
"""
)

other_text = dcc.Markdown('''
Haha! Just checking if anyone actually clicks on the "learn more" button.  

I didn't think these options needed more explanation --  so instead here is
 [how to create a model for help text](https://community.plotly.com/t/any-way-to-create-an-instructions-popout/18828/11?u=annmariew)

''')

COOKIE = "https://todaysmama.com/.image/t_share/MTU5OTEwMzkyMDIyMTE1NzAz/cookie-monster.png"
other_help = dbc.Modal(
    [
        dbc.ModalHeader(["Cookies!", html.Img(src=COOKIE, style={"width": "100%"})]),
        dbc.ModalBody(other_text),
    ],
    id="modal_other",
    is_open=False,
)

align_help = dbc.Modal(
    [
        dbc.ModalHeader("Fill and Align Help"),
        dbc.ModalBody(align_text),
    ],
    id="modal_align",
    is_open=False,
)

symbol_help = dbc.Modal(
    [
        dbc.ModalHeader("Symbol Help"),
        dbc.ModalBody(symbol_text),
    ],
    id="modal_symbol",
    is_open=False,
)

group_help = dbc.Modal(
    [
        dbc.ModalHeader("Grouping Help"),
        dbc.ModalBody(group_text),
    ],
    id="modal_group",
    is_open=False,
)


precision_help = dbc.Modal(
    [
        dbc.ModalHeader("Precision and Decimal Place Help"),
        dbc.ModalBody(precision_text),
    ],
    id="modal_precision",
    is_open=False,
)


type_SI_help = dbc.Modal(
    [
        dbc.ModalHeader("Type and SI-Prefix Help"),
        dbc.ModalBody(type_SI_text),
    ],
    id="modal_type_SI",
    is_open=False,
)


"""
===============================================================================
Dash DataTable to format
"""
output_table = dbc.Card(
    [
        dbc.CardBody(
            [
                intro_text,
                dash_table.DataTable(
                    id="format_table",
                    columns=[
                        {
                            "name": i,
                            "id": i,
                            "type": "numeric",
                        }
                        for i in df.columns
                    ],
                    data=df.to_dict("records"),
                    editable=True,
                    style_table={"overflowX": "auto"},
                    sort_action='native'
                ),
            ]
        )
    ],
    className="mt-2",
    outline=True,
    color="white",
)


"""
===============================================================================
symbol card
"""
prefix_input = dbc.FormGroup(
    [
        dbc.Label(
            "Symbol prefix", html_for="format_symbol_prefix", style={"minWidth": 150}
        ),
        dbc.Col(dbc.Input(id="format_symbol_prefix", value="")),
    ],
)
suffix_input = dbc.FormGroup(
    [
        dbc.Label(
            "Symbol suffix", html_for="format_symbol_suffix", style={"minWidth": 150}
        ),
        dbc.Col(
            dbc.Input(id="format_symbol_suffix", value=""),
        ),
    ],
)
symbol_card = dbc.Card(
    [
        dbc.CardHeader(["Symbol", make_help_btn("symbol_help")]),
        dbc.CardBody(
            [
                dcc.RadioItems(
                    id="format_symbol_pct_radio",
                    options=[
                        {"label": "None", "value": "none"},
                        {"label": "Percentage", "value": "percentage"},
                        {"label": "Show symbol (default: '$')", "value": "symbol"},
                    ],
                    value="none",
                    labelClassName="d-block",
                    inputClassName="mr-2",
                ),
                dbc.Row(
                    [dbc.Col(prefix_input, width=6), dbc.Col(suffix_input, width=6)],
                    form=True,
                    className="mt-2",
                ),
            ]
        ),
    ],
    className="mt-2",
    style={"min-width": 350},
)


"""
===============================================================================
groups card
"""
group_delimiter_input = dbc.FormGroup(
    [
        dbc.Label(
            'Delimiter (default: ",")',
            html_for="format_group_delimiter",
            style={"minWidth": 150},
        ),
        dbc.Col(
            dbc.Input(id="format_group_delimiter", value="", maxLength=1),
        ),
    ],
)
groups_input = dbc.FormGroup(
    [
        dbc.Label(
            "Groups (default: 3)", html_for="format_groups", style={"minWidth": 150}
        ),
        dbc.Col(
            dbc.Input(id="format_groups", value="", type="number"),
        ),
    ],
)
group_card = dbc.Card(
    [
        dbc.CardHeader(["Grouping", make_help_btn("group_help")]),
        dbc.CardBody(
            [
                dbc.Checklist(
                    id="format_group_checkbox",
                    options=[
                        {"label": "Show groupings (default: thousands)", "value": ""}
                    ],
                ),
                dbc.Row(
                    [
                        dbc.Col(group_delimiter_input, width=6),
                        dbc.Col(groups_input, width=6),
                    ],
                    form=True,
                    className="mt-2",
                ),
            ]
        ),
    ],
    className="mt-2",
    style={"min-width": 350},
)

"""
===============================================================================
other options card
"""

nan_input = dbc.FormGroup(
    [
        dbc.Label("Replace nan with:", html_for="format_nan", style={"minWidth": 125}),
        dbc.Col(dbc.Input(id="format_nan", value=None), width=4),
    ],
    row=True,
)

options_checklist = dcc.Checklist(
    id="format_checklist",
    options=[
        {"label": "Negative values in () parentheses", "value": "parantheses"},
        {"label": "Positive values show + symbol", "value": "plus_minus"},
        {"label": "Trim trailing zeros", "value": "trim"},
    ],
    value=[],
    inputClassName="mr-2",
    labelStyle={"display": "block"},
)


options_card = dbc.Card(
    [
        dbc.CardHeader(["Other Options", make_help_btn("other_help")]),
        dbc.CardBody(
            [
                options_checklist,
                html.Div(nan_input, className="ml-4"),
            ]
        ),
    ],
    className="mt-4",
    style={"min-width": 350},
)

"""
===============================================================================
precision card
"""

fixed_input = html.Div(
    dbc.Checklist(
        id="format_fixed_checkbox",
        options=[
            {
                "label": "Fixed point",
                "value": "yes",
            }
        ],
    ),
    className="mb-4",
)


decimal_delimiter_input = dbc.FormGroup(
    [
        dbc.Label(
            'Decimal delimiter (default: ".")',
            html_for="format_decimal_delimiter",
            style={"width": 250},
        ),
        dbc.Col(
            dbc.Input(id="format_decimal_delimiter", value="", maxLength=1), width=4
        ),
    ],
    row=True,
)
precision_input = dbc.FormGroup(
    [
        dbc.Label(
            "Precision (number of digits)",
            html_for="format_precision",
            style={"width": 250},
        ),
        dbc.Col(dbc.Input(id="format_precision", value=""), width="4"),
    ],
    row=True,
)


precision_card = dbc.Card(
    [
        dbc.CardHeader(
            ["Precision and Decimal Place", make_help_btn("precision_help")],
        ),
        dbc.CardBody(
            [
                html.Div(
                    "Check this box to set decimal place", className="text-info"
                ),
                fixed_input,
                precision_input,
                decimal_delimiter_input,
            ],
            className="ml-2",
        ),
    ],
    className="mt-4",
    style={"min-width": 350},
)


"""
===============================================================================
type card
"""
scheme_dropdown = dbc.FormGroup(
    [
        html.Div(
            [
                dbc.Label(
                    "All d3-format types",
                    html_for="format_scheme_dropdown",
                    style={"width": 250},
                ),
            ],
            style={"display": "flex", "flex-direction": "row"},
        ),
        dcc.Dropdown(
            id="format_scheme_dropdown",
            options=[{"label": l, "value": v} for l, v in scheme_options.items()],
            style={"minWidth": 350},
            optionHeight=50,
        ),
    ],
    row=True,
)
si_prefix_input = dbc.FormGroup(
    [
        html.Div(
            [
                dbc.Label(
                    "SI-prefix", html_for="format_si_prefix", style={"width": 250}
                ),
            ],
            style={"display": "flex", "flex-direction": "row"},
        ),
        dcc.Dropdown(
            id="format_si_prefix",
            value="",
            # options=[{"label": str(si), "value": si} for si in prefix_options],
            options=[
                {"label": l + ": " + str(v), "value": v}
                for l, v in prefix_options_dict.items()
            ],
            style={"minWidth": 300},
        ),
    ],
    row=True,
)
type_card = dbc.Card(
    [
        dbc.CardHeader(
            ["Type and SI-Prefix", make_help_btn("type_SI_help")],
        ),
        dbc.CardBody(
            [scheme_dropdown, si_prefix_input],
            className="ml-2",
        ),
    ],
    className="mt-4",
    style={"min-width": 350},
)


"""
===============================================================================
align card
"""
padding_width_input = dbc.FormGroup(
    [
        dbc.Label("Padding width", html_for="format_padding_width"),
        dbc.Col(dbc.Input(id="format_padding_width", value="")),
    ],
    row=True,
)
fill_input = dbc.FormGroup(
    [
        dbc.Label("Fill character", html_for="format_fill"),
        dbc.Col(dbc.Input(id="format_fill", value="", maxLength=1)),
    ],
    row=True,
)
align_input = dbc.FormGroup(
    [
        dbc.Label("Align options", html_for="format_align", className="mr-2"),
        dcc.Dropdown(
            id="format_align",
            value="",
            options=[{"label": l, "value": v} for l, v in align_options.items()],
            style={"width": 200},
        ),
    ],
    row=True,
)
align_card = dbc.Card(
    [
        dbc.CardHeader(["Fill and Alignment", make_help_btn("align_help")]),
        dbc.CardBody(
            [
                dbc.Row("Complete all 3 fields (or none)", className='text-info'),
                dbc.Row(
                    [
                        padding_width_input,
                        fill_input,
                        align_input,
                    ],
                    form=True,
                    className="mt-2",
                ),
            ],
            className="ml-2",
        ),
    ],
    className="mt-4",
    style={"min-width": 350},
)


"""
===============================================================================
results card
"""

table_def = html.Pre(
    html.Code(
        [
            """
    dash_table.DataTable(
        id="format_table",
        columns=[
            {
                "name": i,
                "id": i,
                "type": "numeric",  # Required!
                "format": formatted
            }
            for i in df.columns
        ],
        data=df.to_dict("records"),
        editable=True,
    )         
         """
        ]
    )
)

results_card = dbc.Card(
    [
        dbc.CardHeader(html.H3("Results -- code for your app 😀")),
        dbc.CardBody(
            [
                html.H5("Format using the Format helper object:"),
                html.Code("formatted = Format()", className="ml-4"),
                html.Br(),
                html.Code(id="format_code_sample", className="ml-4"),
                html.H5("or format manually:", className="mt-4"),
                html.Code(id="format_json", className="ml-4"),
                html.H5("Dash DataTable definition", className="mt-4"),
                table_def,
            ]
        ),
    ],
    color="light",
    className="mt-4",
)

"""
===============================================================================
Foreign exchange app -- Code to show in App
"""
app1_text = dcc.Markdown(
    """
```
# -*- coding: utf-8 -*-
import dash
import dash_table
import dash_table.FormatTemplate as FormatTemplate
from dash_table.Format import Format, Scheme, Symbol, Group
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
from dash.dependencies import Input, Output

app = dash.Dash(__name__)

df = pd.DataFrame(
    {
        "Exchange": ["Canadian Dollar", "Euro", "Japanese Yen", "US Dollar"],
        "CAD": [1, 0.64, 78.91, 75],
        "EUR": [1.56, 1, 122.9, 1.17],
        "JPY": [0.013, 0.0081, 1, 0.0095],
        "USD": [1.33, 0.85, 104.96, 1],
    }
)
df = df.set_index("Exchange")
app.layout = html.Div(
    [
        html.Div(
            [
                "Enter Amount to Exchange",
                dcc.Input(id="exchange_amount", type="number", value=100),
            ],
            style={"width": 250},
        ),
        html.Div(
            dash_table.DataTable(
                id="exchange_rate_table",
                columns=[
                    {"name": "Currency Exchange Table", "id": "Exchange"},
                    {
                        "name": "Canadian Dollar",
                        "id": "CAD",
                        "type": "numeric",
                        "format": Format()  # formatted using the Format() object
                        .scheme(Scheme.fixed)
                        .precision(2)
                        .symbol_prefix("$")
                        .symbol(Symbol.yes)
                        .symbol_suffix(" CAD")
                        .group(Group.yes),
                    },
                    {
                        "name": "Euro",
                        "id": "EUR",
                        "type": "numeric",
                        "format": {  # formatted "manually"
                            "specifier": "$,.2f",
                            "locale": {
                                "symbol": ["€", " EUR"],
                                "group": ".",
                                "decimal": ",",
                            },
                        },
                    },
                    {
                        "name": "Japanese Yen",
                        "id": "JPY",
                        "type": "numeric",
                        "format": {  # formatted "manually"
                            "specifier": "$,.0f",
                            "locale": {"symbol": ["¥", " JPX"]},
                        },
                    },
                    {
                        "name": "US Dollar",
                        "id": "USD",
                        "type": "numeric",
                        # formatted using FormatTemplate:
                        "format": FormatTemplate.money(2),
                    },
                ],
                data=df.to_dict("records"),
            )
        ),
    ]
)


@app.callback(
    Output("exchange_rate_table", "data"), [Input("exchange_amount", "value")]
)
def update_exchange_rate_table(amount):  
    dff = df.multiply(amount, fill_value=0) if amount else df.copy()
    return dff.reset_index().to_dict("records")


if __name__ == "__main__":
    app.run_server(debug=True)

```
"""
)

"""
===============================================================================
Layout of Foreign exchange app 
"""

example_app_layout = html.Div(
    [
        html.Div(
            [
                "Enter Amount to Exchange",
                dcc.Input(id="exchange_amount", type="number", value=100),
            ],
            style={"width": 250},
        ),
        html.Div(
            dash_table.DataTable(
                id="exchange_rate_table",
                columns=[
                    {"name": "Currency Exchange Table", "id": "Exchange"},
                    {
                        "name": "Canadian Dollar",
                        "id": "CAD",
                        "type": "numeric",
                        "format": Format()  # formatted using the Format() object
                        .scheme(Scheme.fixed)
                        .precision(2)
                        .symbol(Symbol.yes)
                        .symbol_prefix('$')
                        .symbol_suffix(" CAD")
                        .group(Group.yes),
                    },
                    {
                        "name": "Euro",
                        "id": "EUR",
                        "type": "numeric",
                        "format": {  # formatted "manually"
                            "specifier": "$,.2f",
                            "locale": {
                                "symbol": ["€", " EUR"],
                                "group": ".",
                                "decimal": ",",
                            },
                        },
                    },
                    {
                        "name": "Japanese Yen",
                        "id": "JPY",
                        "type": "numeric",
                        "format": {  # formatted "manually"
                            "specifier": "$,.0f",
                            "locale": {"symbol": ["¥", " JPX"]},
                        },
                    },
                    {
                        "name": "US Dollar",
                        "id": "USD",
                        "type": "numeric",
                        # formatted using FormatTemplate:
                        "format": FormatTemplate.money(2),
                    },
                ],
                data=example_app_df.to_dict("records"),
                style_table={"overflowX": "auto"},
            )
        ),
    ]
)


app1_text2 = dcc.Markdown(
    """
The columns in this app are formatted in three different ways:

1.  Using the Format() object 
2. Formatting "manually"
3. Using the FormatTemplate

Note that `"type": "numeric",` is required in order for formatting to be applied
"""
)


app_card = dbc.Card(
    [
        dbc.CardHeader(html.H3("Example:  Foreign exchange App")),
        dbc.Card(app1_text2, className="mx-4 mt-4"),
        dbc.Card(example_app_layout, className="m-4"),
        dbc.Card(app1_text, className="m-4"),
    ],
    color="light",
    className="mt-4",
)


"""
===============================================================================
layout
"""

app.layout = dbc.Container(
    [
        dbc.Row(
            dbc.Col(
                (
                    html.H2(
                        "How to format numbers in a Dash DataTable",
                        className="text-center m-2, p-2",
                    )
                )
            )
        ),
        dbc.Row(dbc.Col(output_table)),
        dbc.Row(dbc.CardDeck([symbol_card, group_card])),
        dbc.Row(dbc.CardDeck([precision_card, type_card])),
        dbc.Row(dbc.CardDeck([align_card, options_card])),
        dbc.Row(dbc.Col(results_card), className="mb-5"),
        dbc.Row(dbc.Col(see_more_text), className="mb-5"),
        dbc.Row(
            dbc.Col([symbol_help, precision_help, type_SI_help, align_help, group_help, other_help])
        ),
        dbc.Row(dbc.Col(app_card)),
    ],
)


"""
===============================================================================
callbacks
"""


@app.callback(
    Output("format_table", "columns"),
    Output("format_code_sample", "children"),
    Output("format_json", "children"),
    #
    Input("format_fixed_checkbox", "value"),
    Input("format_decimal_delimiter", "value"),
    Input("format_precision", "value"),
    Input("format_si_prefix", "value"),
    #
    Input("format_checklist", "value"),
    Input("format_nan", "value"),
    #
    Input("format_scheme_dropdown", "value"),
    #
    Input("format_symbol_pct_radio", "value"),
    Input("format_symbol_prefix", "value"),
    Input("format_symbol_suffix", "value"),
    #
    Input("format_padding_width", "value"),
    Input("format_fill", "value"),
    Input("format_align", "value"),
    #
    Input("format_group_checkbox", "value"),
    Input("format_group_delimiter", "value"),
    Input("format_groups", "value"),
)
def update_format_table(
    fixed_checkbox,
    decimal_char,
    precision,
    si_prefix,
    options_checklist,
    nan,
    scheme_dd,
    symbol_pct_radio,
    prefix,
    suffix,
    width,
    fill_char,
    align_val,
    group_checkbox,
    group_char,
    groupings,
):
    code = {}
    formatted = Format()

    if fixed_checkbox:
        formatted = formatted.scheme(Scheme.fixed)
        code[1] = ".scheme(Scheme.fixed)"
    if decimal_char:
        formatted = formatted.decimal_delimiter(decimal_char)
        code[2] = f".decimal_delimiter('{decimal_char}')"
    if precision:
        formatted = formatted.precision(int(precision))
        code[3] = f".precision({int(precision)})"
    if si_prefix:
        si_prefix = None if si_prefix == "None" else si_prefix
        formatted = formatted.si_prefix(si_prefix)
        code[4] = f".si_prefix({si_prefix})"
    if symbol_pct_radio == "percentage":
        formatted = formatted.scheme(Scheme.percentage)
        code[5] = f".scheme(Scheme.percentage)"
    if "plus_minus" in options_checklist:
        formatted = formatted.sign(Sign.positive)
        code[6] = f".sign(Sign.positive)"
    if "parantheses" in options_checklist:
        formatted = formatted.sign(Sign.parantheses)
        code[7] = f".sign(Sign.parantheses)"
    if "trim" in options_checklist:
        formatted = formatted.trim(Trim.yes)
        code[8] = f".trim(Trim.yes)"
    if nan:
        print("nan", nan)
        formatted = formatted.nully(nan)
        code[9] = f".nully('{nan}')"
    if scheme_dd:
        formatted = formatted.scheme(scheme_dd)
        code[10] = f".scheme('{scheme_dd}')"
    if symbol_pct_radio == "symbol":
        formatted = formatted.symbol(Symbol.yes)
        code[11] = f".symbol(Symbol.yes)"
    if symbol_pct_radio == "none":
        code[11] = None
        code[5] = None
    if prefix:
        formatted = formatted.symbol_prefix(prefix)
        code[12] = f".symbol_prefix('{prefix}')"
    if suffix:
        formatted = formatted.symbol_suffix(suffix)
        code[13] = f".symbol_suffix('{suffix}')"
    if width:
        formatted = formatted.padding_width(int(width))
        code[14] = f".padding_width({int(width)})"
    if fill_char:
        formatted = formatted.fill(fill_char)
        code[15] = f".fill('{fill_char}')"
    if align_val:
        formatted = formatted.align(align_val)
        code[16] = f".align('{align_val}')"
    if group_checkbox:
        formatted = formatted.group(Group.yes)
        code[17] = f".group(Group.yes)"
    if group_char:
        formatted = formatted.group_delimiter(group_char)
        code[18] = f".group_delimiter('{group_char}')"
    if groupings:
        formatted = formatted.groups(int(groupings))
        code[19] = f".groups({int(groupings)})"

    columns = [
        {"name": i, "id": i, "type": "numeric", "format": formatted} for i in df.columns
    ]

    code = ["formatted = formatted"] + list(code.values())
    code = [] if code == ["formatted = formatted", None, None] else code
    to_json = ["formatted = "] + [str(formatted.to_plotly_json())]

    return columns, code, to_json


@app.callback(
    Output("format_symbol_pct_radio", "value"),
    Input("format_symbol_prefix", "value"),
    Input("format_symbol_suffix", "value"),
)
def update_checkbox(prefix, suffix):
    if prefix or suffix:
        return "symbol"
    else:
        return dash.no_update


@app.callback(
    Output("format_group_checkbox", "value"),
    Input("format_group_delimiter", "value"),
    Input("format_groups", "value"),
)
def update_checkbox(group_char, groups):
    if group_char or groups:
        return ["yes"]
    else:
        return dash.no_update


@app.callback(
    Output("format_fixed_checkbox", "value"),
    Output("format_checklist", "value"),
    Input("format_scheme_dropdown", "value"),
)
def update_checkbox(d3):
    if d3 and d3 != "f":
        return [], []
    if d3 and d3 == "f":
        return "yes", []
    else:
        return dash.no_update, dash.no_update


@app.callback(
    Output("exchange_rate_table", "data"), [Input("exchange_amount", "value")]
)
def update_exchange_rate_table(amount):
    dff = example_app_df.multiply(amount, fill_value=0) if amount else example_app_df.copy()
    return dff.reset_index().to_dict("records")


"""
===============================================================================
Help text Modal callbacks
"""


@app.callback(
    Output("modal_symbol", "is_open"),
    [Input("symbol_help", "n_clicks")],
    [State("modal_symbol", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("modal_precision", "is_open"),
    [Input("precision_help", "n_clicks")],
    [State("modal_precision", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("modal_type_SI", "is_open"),
    [Input("type_SI_help", "n_clicks")],
    [State("modal_type_SI", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("modal_align", "is_open"),
    [Input("align_help", "n_clicks")],
    [State("modal_align", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


@app.callback(
    Output("modal_group", "is_open"),
    [Input("group_help", "n_clicks")],
    [State("modal_group", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open

@app.callback(
    Output("modal_other", "is_open"),
    [Input("other_help", "n_clicks")],
    [State("modal_other", "is_open")],
)
def toggle_modal(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(debug=True)


# add error message is Format is used and column is not type numeric?
# update docstring in Format so that help(Format) has better documentation
# unicode doesn't work
# default for NaN is currently "". https://github.com/plotly/dash-table/blob/dev/dash_table/Format.py#L75
#  Documentation unclear about whether this should display something other than a blank. Update?
# FormatTemplate.percentage(1, rounded=True) - doesn't round to 1 decimal point. It shows 1 significant digit.  Bug?


# From table reference
# code:  https://github.com/plotly/dash-table/pull/377/files/58ae65e2a6be3b0c48f631dc7a7c3c69326eb0f2
"""
format (dict; optional): The formatting applied to the column's data. This prop is derived from the d3-format 
library specification. Apart from being structured slightly differently (under a single prop), the usage is the 
same. 'locale': represents localization specific formatting information. When left unspecified, will use the 
default value provided by d3-format. The keys are as follows: 'symbol': (default: ['$', '']) a list of two strings 
representing the prefix and suffix symbols. Typically used for currency, and implemented using d3's currency 
format, but you can use this for other symbols such as measurement units; 'decimal': (default: '.') the string 
used for the decimal separator; 'group': (default: ',') the string used for the groups separator; 'grouping':
(default: [3]) a list of integers representing the grouping pattern. 'numerals': a list of ten strings used as 
replacements for numbers 0-9; 'percent': (default: '%') the string used for the percentage symbol; 
'separate_4digits': (default: True) separate integers with 4-digits or less. 'nully': a value that will be used in place 
of the nully value during formatting. If the value type matches the column type, it will be formatted normally. 
'prefix': a number representing the SI unit to use during formatting. See dash_table.Format.Prefix 
enumeration for the list of valid values 'specifier': (default: '') represents the rules to apply when formatting the
number. dash_table.FormatTemplate contains helper functions to rapidly use certain typical number formats. 
format has the following type: dict containing keys 'locale', 'nully', 'prefix', 'specifier'. Those keys have the 
following types: - locale (dict; optional): locale has the following type: dict containing keys 'symbol', 'decimal', 
'group', 'grouping', 'numerals', 'percent', 'separate_4digits'. Those keys have the following types: - symbol (list of 
strings; optional) - decimal (string; optional) - group (string; optional) - grouping (list of numbers; optional) - 
numerals (list of strings; optional) - percent (string; optional) - separate_4digits (boolean; optional) - nully 
(boolean | number | string | dict | list; optional) - prefix (number; optional) - specifier (string; optional)

# Suggested change:

format (dict; optional): The formatting applied to the column's data. Columns must be defined as "type": "numeric"
This prop is derived from the d3-format library specification. https://github.com/d3/d3-format
Apart from being structured slightly differently (under a single prop), the usage is the same. 

format (dict; optional)  format dict may contain the following keys: 'locale', 'nully', 'prefix', 'specifier'.     

'locale': (dict; optional) locale dict may contain the following:   
        'symbol': (default: ['$', '']) a list of two strings representing the prefix and suffix symbols.
                  Typically used for currency, and implemented using d3's currency format, but you can 
                  use this for other symbols such as measurement units; 
        'decimal': (default: '.') the string used for the decimal separator; 
        'group': (default: ',') the string used for the groups separator; 
        'grouping': (default: [3]) a list of integers representing the grouping pattern. (eg - thousands)
        'numerals': a list of ten strings used as replacements for numbers 0-9; 
        'percent': (default: '%') the string used for the percentage symbol; 
        'separate_4digits': (default: True) separate integers with 4-digits or less.         

'nully': (default: "NaN") a value (boolean |number | string | dict | list) that will be used in place of the 
        nully value during formatting.  If the value type matches the column type, it will be formatted normally. 
'prefix': (number) a number representing the SI unit to use during formatting. 
         See dash_table.Format.Prefix enumeration for the list of valid values 
'specifier': (default: '') represents the d3-format rules to apply when formatting the number. 

Note:  dash_table.FormatTemplate contains helper functions to rapidly use certain typical number formats. 
.
"""
