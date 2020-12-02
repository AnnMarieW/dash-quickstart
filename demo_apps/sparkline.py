import dash
import dash_table
import pandas as pd
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
from dash_table.Format import Format, Scheme, Group
from dash.exceptions import PreventUpdate

df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv")

external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


formatted = Format().scheme(Scheme.fixed).precision(0).group(Group.yes)
spark_options = [
    "Sparks-Bar-Medium",
    "Sparks-Bar-Wide",
    "Sparks-Dot-Medium",
    "Sparks-Dot-Large",
    "Sparks-Dot-Extralarge",
    "Sparks-Dotline-Extrathin",
    "Sparks-Dotline-Thin",
    "Sparks-Dotline-Medium",
    "Sparks-Dotline-Thick",
    "Sparks-Dotline-Extrathick",
]


app.layout = html.Div(
    [
        html.H2("Sparkline Demo App"),
        html.Div("Fonts from https://github.com/aftertheflood/sparks"),
        html.Div([
        dcc.Dropdown(
            id="spark_style",
            options=[{"label": i, "value": i} for i in spark_options],
            value="Sparks-Bar-Extrawide",
            placeholder="Select sparkline style",
            style={"width": 300},
        ),
        dcc.RadioItems(
            id="stat_radio",
            options=[{"label": i, "value": i} for i in ["pop", "lifeExp", "gdpPercap"]],
            value="gdpPercap",
            labelStyle={"display": "inline-block"},
        ),

        dcc.RangeSlider(
            id="year_slider",
            marks={i: str(i) for i in df["year"].unique().tolist()},
            min=1952,
            max=2007,
            allowCross=False,
            value=[1987, 2007],
        )],style={'width':600, 'margin':20}),
        dash_table.DataTable(
            id="table",
            filter_action="native",
            sort_action="native",
        ),
    ]
)


def make_sparkline(df_wide):
    """

    :param df_wide: dataframe in a "wide" format with the sparkline periods as columns
    :return: a series with the data formatted for the sparkline fonts.
             Example:  '453{10,40,30,80}690'
    """

    # normalize between 0 and 100
    max = df_wide.max(axis=1)
    min = df_wide.min(axis=1)

    # if data is all positive numbers use: (x)/ (x.max)*100
    df_spark = df_wide.div((max), axis="index").mul(100).round(decimals=0)

    # Or use this formula if the data has negative numbers:  ( (x-x.min)/ (x.max-x.min)*100
    #df_spark = df_wide.sub(min, axis="index").div((max - min).round(decimals=0), axis="index") * 100

    # format the normalized numbers like: '25,20,50,80'
    df_spark["spark"] = df_spark.astype(int).astype(str).agg(",".join, axis=1)

    # get the starting and ending numbers
    df_spark["start"] = df_wide[df_wide.columns[0]].astype(int).astype(str)
    df_spark["end"] = df_wide[df_wide.columns[-1]].astype(int).astype(str)

    # put it all together
    return df_spark["start"] + "{" + df_spark["spark"] + "}" + df_spark["end"]




@app.callback(
    Output("table", "columns"),
    Output("table", "data"),
    Output("table", "style_data_conditional"),
    Input("year_slider", "value"),
    Input("stat_radio", "value"),
    Input("spark_style", "value"),
)
def update_table(year, stat, spark_style):
    if year[0] == year[1]:
        raise PreventUpdate

    dff = df[(df["year"] >= year[0]) & (df["year"] <= year[1])]
    dff = dff.pivot(index=["country", "continent"], columns="year", values=stat)
    dff["sparkline"] = make_sparkline(dff)
    dff = dff.reset_index()

    columns = [
        {"name": str(i), "id": str(i), "format": formatted, "type": "numeric"}
        for i in dff.columns
    ]
    data = dff.to_dict("records")

    style = [
        {"if": {"column_id": "sparkline"}, "font-family": spark_style,},
    ]
    return columns, data, style


if __name__ == "__main__":
    app.run_server(debug=True)


'''
===============================================================================
Move the following css to the assets folder in your root directory.  

===============================================================================


@font-face {
  font-family: 'Sparks-Bar-Narrow';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Bar-Narrow.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Bar-Narrow.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff2/Sparks-Bar-Narrow.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Bar-Narrow.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Bar-Narrow.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Bar-Narrow.svg#Sparks-Bar-Narrow') format('svg');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Sparks-Bar-Medium';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Bar-Medium.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Bar-Medium.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff2/Sparks-Bar-Medium.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Bar-Medium.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Bar-Medium.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Bar-Medium.svg#Sparks-Bar-Medium') format('svg');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Sparks-Bar-Wide';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Bar-Wide.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Bar-Wide.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff2/Sparks-Bar-Wide.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Bar-Wide.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Bar-Wide.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Bar-Wide.svg#Sparks-Bar-Wide') format('svg');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Sparks-Bar-Extrawide';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Bar-Extrawide.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Bar-Extrawide.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff2/Sparks-Bar-Extrawide.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Bar-Extrawide.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Bar-Extrawide.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Bar-Extrawide.svg#Sparks-Bar-Extrawide') format('svg');
  font-weight: normal;
  font-style: normal;
}

/* Dots */

@font-face {
  font-family: 'Sparks-Dot-Extrasmall';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dot-Extrasmall.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dot-Extrasmall.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff2/Sparks-Dot-Extrasmall.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Dot-Extrasmall.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Dot-Extrasmall.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Dot-Extrasmall.svg#Sparks-Dot-Extrasmall') format('svg');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Sparks-Dot-Small';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dot-Small.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dot-Small.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff2/Sparks-Dot-Small.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Dot-Small.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Dot-Small.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Dot-Small.svg#Sparks-Dot-Small') format('svg');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Sparks-Dot-Medium';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dot-Medium.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dot-Medium.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff2/Sparks-Dot-Medium.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Dot-Medium.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Dot-Medium.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Dot-Medium.svg#Sparks-Dot-Medium') format('svg');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Sparks-Dot-Large';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dot-Large.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dot-Large.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff2/Sparks-Dot-Large.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Dot-Large.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Dot-Large.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Dot-Large.svg#Sparks-Dot-Large') format('svg');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Sparks-Dot-Extralarge';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dot-Extralarge.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dot-Extralarge.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff2/Sparks-Dot-Extralarge.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Dot-Extralarge.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Dot-Extralarge.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Dot-Extralarge.svg#Sparks-Dot-Extralarge') format('svg');
  font-weight: normal;
  font-style: normal;
}

/* Dot-lines */

@font-face {
  font-family: 'Sparks-Dotline-Extrathin';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dotline-Extrathin.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dotline-Extrathin.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff2/Sparks-Dotline-Extrathin.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Dotline-Extrathin.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Dotline-Extrathin.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Dotline-Extrathin.svg#Sparks-Dotline-Extrathin') format('svg');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Sparks-Dotline-Thin';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dotline-Thin.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dotline-Thin.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff2/Sparks-Dotline-Thin.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Dotline-Thin.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Dotline-Thin.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Dotline-Thin.svg#Sparks-Dotline-Thin') format('svg');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Sparks-Dotline-Medium';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dotline-Medium.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dotline-Medium.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff/2Sparks-Dotline-Medium.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Dotline-Medium.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Dotline-Medium.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Dotline-Medium.svg#Sparks-Dotline-Medium') format('svg');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Sparks-Dotline-Thick';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dotline-Thick.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dotline-Thick.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff2/Sparks-Dotline-Thick.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Dotline-Thick.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Dotline-Thick.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Dotline-Thick.svg#Sparks-Dotline-Thick') format('svg');
  font-weight: normal;
  font-style: normal;
}

@font-face {
  font-family: 'Sparks-Dotline-Extrathick';
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dotline-Extrathick.eot');
  src: url('https://tools.aftertheflood.com/sparks/output/eot/Sparks-Dotline-Extrathick.eot?#iefix') format('embedded-opentype'),
       url('https://tools.aftertheflood.com/sparks/output/woff2/Sparks-Dotline-Extrathick.woff2') format('woff2'),
       url('https://tools.aftertheflood.com/sparks/output/woff/Sparks-Dotline-Extrathick.woff') format('woff'),
       url('https://tools.aftertheflood.com/sparks/output/ttf/Sparks-Dotline-Extrathick.ttf') format('truetype'),
       url('https://tools.aftertheflood.com/sparks/output/svg/Sparks-Dotline-Extrathick.svg#Sparks-Dotline-Extrathick') format('svg');
  font-weight: normal;
  font-style: normal;
}

.sparks {
  font-variant-ligatures: normal;
}

.bar-narrow {
  font-family: Sparks-Bar-Medium;
}
.bar-medium {
  font-family: Sparks-Bar-Medium;
}
.bar-wide {
  font-family: Sparks-Bar-Wide;
}
.bar-extrawide {
  font-family: Sparks-Bar-Wide;
  font-size:18px
}

.dot-extrasmall {
  font-family: Sparks-Dot-Extrasmall;
}
.dot-small {
  font-family: Sparks-Dot-Small;
}
.dot-medium {
  font-family: Sparks-Dot-Medium;
}
.dot-large {
  font-family: Sparks-Dot-Large;
}
.dot-extralarge {
  font-family: Sparks-Dot-Extralarge;
}

.dotline-extrathin {
  font-family: Sparks-Dotline-Extrathin;
}
.dotline-thin {
  font-family: Sparks-Dotline-Thin;
}
.dotline-medium {
  font-family: Sparks-Dotline-Medium;
}
.dotline-thick {
  font-family: Sparks-Dotline-Thick;
}
.dotline-extrathick {
  font-family: Sparks-Dotline-Extrathick;
}


'''