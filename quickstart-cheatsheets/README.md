# Dash Quickstart Apps #


This is a collection of quickstart apps from the Dash Tutorial, Dash Community Forum and other resources.

---

## __Dash Hello World__

- [Dash Tutorial](https://dash.plotly.com/installation)


```
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
    
    
    
    
    
```


## __DataTable Quickstart__


- [Dash DataTable Tutorial](https://dash.plotly.com/datatable)

```
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
    
    
```    

## __dash-bootstrap Quickstart__


- [dash-bootstrap documentation](https://dash-bootstrap-components.opensource.faculty.ai/docs/quickstart/)
- [bootstrap classname cheatsheet](https://hackerthemes.com/bootstrap-cheatsheet/)


```

import dash
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container(
    dbc.Alert("Hello Bootstrap!", color="success"),
    className="p-5",
)

if __name__ == "__main__":
    app.run_server()


```
## __dash-leaflet quickstart__

- [dash-leaflet documentation](https://dash-leaflet.herokuapp.com/)

```
import dash
import dash_leaflet as dl

app = dash.Dash()
app.layout = dl.Map(dl.TileLayer(), style={'width': '1000px', 'height': '500px'})

if __name__ == '__main__':
    app.run_server()    
```



## __Dash callback quickstart__


- [Dash callbacks tutorial](https://dash.plotly.com/basic-callbacks)

```
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
    
```


## __Dash pattern matching callbacks quickstart__

- [Dash pattern matching callback tutorial](https://dash.plotly.com/pattern-matching-callbacks)

```
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
```


## __Datasets: Plotly datasets and generic Pandas dataframes__

It's often helpful to test an app with sample data.  Here are examples of  built-in sample data from Plotly and some random data 
you can generate with Numpy. 

- Sample data from my favorite Pandas tutorial: [10 minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html).


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


```

## __Callbacks:__

- [Dash advanced callbacks tutorial](https://dash.plotly.com/advanced-callbacks)

In certain cases, you don't want to update the callback output. Here's how:

Using `PreventUpdate`   

All outputs of this callback will not update `if n_clicks is None`:
```
from dash.exceptions import PreventUpdate

# code snippet from a dash callback:

def update_output(n_clicks):
    if n_clicks is None:
        raise PreventUpdate
```

 ---

Using `dash.no_update`  

Here, the first output is not updated and the second one, a graph,  is updated.

```
    return dash.no_update, figure
```

---
Which input triggered a callback?  

Using  `dash.callback_context`  
 
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

## __Components:__

Find out more by typing in your Python terminal:  help(dash_core_components.Checklist) or any other component name.
Here are a few popular components with some sample prop settings:

### dcc.Checklist
see also dcc.RadioItems
```
dcc.Checklist(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montréal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'}
    ],
    value=['NYC', 'MTL'],
    labelStyle={'display': 'inline-block'}
) 
```

---
### dcc.Dropdown
```
dcc.Dropdown(
    options=[
        {'label': 'New York City', 'value': 'NYC'},
        {'label': 'Montreal', 'value': 'MTL'},
        {'label': 'San Francisco', 'value': 'SF'},
    ],
    value=['MTL'],  #if multi=False, this must be a string and not a list (remove the [])
    multi=True,
    clearable=False
    placeholder='Select a city'
)  
```
### dcc.Slider
see also dcc.SliderRange
```
dcc.Slider(
    min=0,
    max=100,
    value=65,
    marks={
        0: {'label': '0 °C', 'style': {'color': '#77b0b1'}},
        26: {'label': '26 °C'},
        37: {'label': '37 °C'},
        100: {'label': '100 °C', 'style': {'color': '#f50'}}
    },
    included=False
)  
```
---

### dcc.Input

```dcc.Input(id="input2", type="text", placeholder="", debounce=True),```

note: allowed types = (
    "text", "number", "password", "email", "search",
    "tel", "url", "range", "hidden",
)

### html.Button
``` html.Button('Button 1', id='btn-nclicks-1', n_clicks=0),```

### dcc.DatePickerRange
see also DatePickerSinge
```
dcc.DatePickerRange(
        id="my-date-picker-range",  
        calendar_orientation="horizontal",  # vertical or horizontal
        day_size=39,  # size of calendar image. Default is 39
        end_date_placeholder_text="Return",  
        with_portal=False,  # if True calendar will open in a full screen overlay portal
        first_day_of_week=0,  # Display of calendar when open (0 = Sunday)
        reopen_calendar_on_clear=True,
        is_RTL=False,  # True or False for direction of calendar
        clearable=True,  # whether or not the user can clear the dropdown
        number_of_months_shown=1,  
        min_date_allowed=date(1995, 8, 5),
        max_date_allowed=date(2020, 8, 5),
        initial_visible_month=date(2020, 8, 5),
        start_date=
        end_date=
        display_format="D-M-Y",  # how selected dates are displayed
        month_format="MMMM, YYYY",  # how calendar headers are displayed when the calendar is opened.
        minimum_nights=1, 
        persistence=True,
        persisted_props=["start_date"],
        persistence_type="session",  # session, local, or memory. Default is 'local'
        updatemode="singledate",  # singledate or bothdates. Determines when callback is triggered
    ),
```