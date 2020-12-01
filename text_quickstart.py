
"""
===============================================================================
Quickstart apps
"""


hello_world_intro = """        
    #### __Dash Hello World__    
    - Start the [Dash Tutorial](https://dash.plotly.com/installation)
"""

hello_world_code = """```
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
df = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
})

fig = px.bar(df, x="Fruit", y="Amount", color="City", barmode="group")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),
    dcc.Graph(
        id='example-graph',
        figure=fig
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
```"""

datatable_intro = """
    #### __DataTable Quickstart__
    - [Dash DataTable Tutorial](https://dash.plotly.com/datatable)  
    - [Dash DataTable Reference](https://dash.plotly.com/datatable/reference) 
"""

datatable_code = """```                            
    import dash
    import dash_table
    import pandas as pd

    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')

    app = dash.Dash(__name__)

    app.layout = dash_table.DataTable(
        id='table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
    )

    if __name__ == '__main__':
        app.run_server(debug=True)
```"""


bootstrap_intro = """
    ### __dash-bootstrap Quickstart__
    - See the dash-bootstrap [tutorial and documentation](https://dash-bootstrap-components.opensource.faculty.ai/docs/quickstart/)
    - The best Bootstrap className [cheatsheet](https://hackerthemes.com/bootstrap-cheatsheet/)
"""

bootstrap_code = """``` 
    import dash
    import dash_bootstrap_components as dbc
    
    app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
    
    app.layout = dbc.Container(
        dbc.Alert("Hello Bootstrap!", color="success"),
        className="p-5",
        fluid=True,
    )
    
    if __name__ == "__main__":
        app.run_server(debug=True)
```"""

leaflet_intro = """
    #### __dash-leaflet  Quickstart__
    - See the [dash-leaflet documentation](https://dash-leaflet.herokuapp.com/) for more examples
"""


leaflet_code = """``` 
    import dash
    import dash_leaflet as dl
    
    app = dash.Dash()
    app.layout = dl.Map(dl.TileLayer(), style={'width': '1000px', 'height': '500px'})
    
    if __name__ == '__main__':
        app.run_server()
```"""


callback_intro = """
    #### __Callbacks Quickstart__
    - See the [Dash callbacks tutorial](https://dash.plotly.com/basic-callbacks)
"""


callback_code = """``` 
    import dash
    from dash.dependencies import Input, Output
    import dash_html_components as html
    import dash_core_components as dcc
    
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    app.layout = html.Div([
        dcc.Dropdown(
            id='city-dropdown',
            options=[
                {'label': 'New York City', 'value': 'NYC'},
                {'label': 'Montreal', 'value': 'MTL'},
                {'label': 'San Francisco', 'value': 'SF'}
            ],
            value='NYC'
        ),
        html.Div(id='output-div')
    ])
    
    @app.callback(Output('output-div', 'children'), Input('city-dropdown', 'value'))
    def update(city):
        return f'You have selected {city}'
    
    if __name__ == '__main__':
        app.run_server(debug=True)

```"""

callback_code1 = """``` 
    import dash
    import dash_table
    import pandas as pd
    import dash_core_components as dcc
    import dash_html_components as html
    from dash.dependencies import Input, Output
    
    df = pd.read_csv(
        "https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv"
    )
    
    external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
    
    app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
    
    app.layout = html.Div(
        [
            dcc.Dropdown(
                id="dropdown",
                options=[{"label": i, "value": i} for i in df["country"].unique()],
                multi=True,
                value=[],
            ),
            dash_table.DataTable(
                id="table",
                columns=[{"name": i, "id": i} for i in df.columns],
                data=df.to_dict("records"),
            ),
        ]
    )
    
    
    @app.callback(
        Output("table", "data"), Input("dropdown", "value"),
    )
    def update_table(country_dd):
        dff = df.copy() if country_dd == [] else df[df["country"].isin(country_dd)]
        return dff.to_dict("records")
    
    
    if __name__ == "__main__":
        app.run_server(debug=True)
```"""




pattern_match_intro = """
    #### __Pattern Matching Callbacks Quickstart__
    - See the [Dash pattern matching callback tutorial](https://dash.plotly.com/pattern-matching-callbacks)
"""


pattern_match_code = """``` 
    import dash
    import dash_core_components as dcc
    import dash_html_components as html
    from dash.dependencies import Input, Output, State, MATCH, ALL
    
    app = dash.Dash(__name__, suppress_callback_exceptions=True)
    
    app.layout = html.Div([
        html.Button("Add Filter", id="add-filter", n_clicks=0),
        html.Div(id='dropdown-container', children=[]),
        html.Div(id='dropdown-container-output')
    ])
    
    @app.callback(
        Output('dropdown-container', 'children'),
        [Input('add-filter', 'n_clicks')],
        [State('dropdown-container', 'children')])
    def display_dropdowns(n_clicks, children):
        new_dropdown = dcc.Dropdown(
            id={
                'type': 'filter-dropdown',
                'index': n_clicks
            },
            options=[{'label': i, 'value': i} for i in ['NYC', 'MTL', 'LA', 'TOKYO']]
        )
        children.append(new_dropdown)
        return children
    
    @app.callback(
        Output('dropdown-container-output', 'children'),
        [Input({'type': 'filter-dropdown', 'index': ALL}, 'value')]
    )
    def display_output(values):
        return html.Div([
            html.Div('Dropdown {} = {}'.format(i + 1, value))
            for (i, value) in enumerate(values)
        ])
    
    
    if __name__ == '__main__':
        app.run_server(debug=True)
```"""


datasets_intro = """
    ##### __Datasets: Ploty datasets and generic Pandas dataframes Quickstart__
    - Quick Pandas tutorial: [10 minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html).
"""

datasets_code = """

```
    import pandas as pd
    import numpy as np
    df = pd.DataFrame(np.random.randn(6, 4), columns=list('ABCD'))
```
    
- Datasets frequently used in the Dash and Plotly tutorials:  


```
    import plotly.express as px
    
    df = px.data.gapminder()
    df = px.data.iris()
    df = px.data.tips()
    
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/solar.csv')
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/gapminderDataFiveYear.csv')
    
    data = dict(
        [
            ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
            ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
            ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
            ("Humidity", [10, 20, 30, 40, 50, 60]),
            ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
        ]
    )
    df = pd.DataFrame(data)
"""


callback_extras_intro = """
#### __Dash Callback Extras Cheatsheet__    
- See: [Dash advanced callbacks tutorial](https://dash.plotly.com/advanced-callbacks)  

|What to use||When to use it |  
| :----|:----| :----|  
|```  PreventUpdate ```| |Prevents _all_ outputs of a callback from updating| 
|`dash.no_update`|| Prevents _certain_ outputs of a callback from updating|
|`prevent_initial_call=True`|| Prevents initial call of a  _certain_ callback|
|`prevent_initial_callbacks=True` || Prevents _all_ initial calls|
| `dash.callback_context`|| Determine which Input triggered a callback|


---
#### Code snippets:

```  PreventUpdate ```
```
    from dash.exceptions import PreventUpdate    
    ...   
    def update_output(n_clicks):
        if n_clicks is None:
            raise PreventUpdate
```

---
`dash.no_update`    
```
        # first  Output not updated
        return dash.no_update, figure
```
 
    
---
`prevent_initial_call=True`
```
    @app.callback(Output('container', 'children'),
                   Input('btn-1', 'n_clicks'),
                   Input('btn-2', 'n_clicks'),
                   prevent_initial_call=True
    )
```
---
`prevent_initial_callbacks=True`
```
    app = Dash(name=__name__, prevent_initial_callbacks=True)
```
    
   
---

`dash.callback_context`    
```
    @app.callback(Output('container', 'children'),
                   Input('btn-1', 'n_clicks'),
                   Input('btn-2', 'n_clicks'))
    def display(btn1, btn2):
        ctx = dash.callback_context
        input_id = ctx.triggered[0]['prop_id'].split('.')[0]
    
        if input_id == 'btn-1':
            # do something...
```

    
    
    
 
"""


components_intro = """
  #### __Dash Core Components Quickstart__    
     
     - [Dash Core Components Overview](https://dash.plotly.com/dash-core-components) with code examples.  Find out more 
     by typing in your Python terminal:  `help(dash_core_components.Checklist)` or any other component name. 
     
     - [Dash HTML Components list](https://dash.plotly.com/dash-html-components)

"""
