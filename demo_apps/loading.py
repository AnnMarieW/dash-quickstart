import time

import dash
import dash_bootstrap_components as dbc

def serve_layout():
    # add delay to initial layout load so we can see the spinner
    time.sleep(2)
    return dbc.Container(dbc.Alert("Testing"), className="p-5")


app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = serve_layout

if __name__ == "__main__":
    app.run_server(debug=True)
