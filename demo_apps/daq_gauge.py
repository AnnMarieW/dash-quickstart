
"""
How to format dash daq gauges using custom css
"""

import dash
import dash_html_components as html
import dash_daq as daq
import dash_bootstrap_components as dbc

app = dash.Dash(__name__)
app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = html.Div(
    [
        daq.Gauge(
            showCurrentValue=True,
            color={
                "gradient": True,
                "ranges": {"green": [0, 2000], "red": [2000, 10000]},
            },
            value=434,
            scale={"start": 0, "interval": 500, "labelInterval": 3},
            label="Default Gauge",
            max=10000,
            min=0,
        ),
        daq.Gauge(
            size=150,
            showCurrentValue=True,
            color={
                "gradient": True,
                "ranges": {"green": [0, 2000], "red": [2000, 10000]},
            },
            value=434,
            scale={"start": 0, "interval": 500, "labelInterval": 3},
            label="Default Gauge with size=120",
            max=10000,
            min=0,
        ),
        daq.Gauge(
            id="my_gauge",
            size=120,
            showCurrentValue=True,
            color={
                "gradient": True,
                "ranges": {"green": [0, 2000], "red": [2000, 10000]},
            },
            scale={"start": 0, "interval": 500, "labelInterval": 3},
            value=434,
            label="Gauge with custom css",
            max=10000,
            min=0,
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)


"""
Put this in the .css file in the assets folder:


/*** css to change the font style in a gauge see daq_gauge.py  ****/
#my_gauge .cRfgdB .scale {
    font-size: 8px;
}
#my_gauge .jjZFEi {
	text-align: center;
	font-size: 25px;
}


"""