#
# template:
# _intro = '''
#     #### __Quickstart__
#     -
# '''
#
# _code = """```
#
# ```"""
#

"""
===============================================================================
Quickstart apps
"""


hello_world_intro = """        
    #### __Dash Hello World__    
    - [Dash Tutorial](https://dash.plotly.com/installation)
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
    - [dash-bootstrap documentation](https://dash-bootstrap-components.opensource.faculty.ai/docs/quickstart/)
    - [bootstrap classname cheatsheet](https://hackerthemes.com/bootstrap-cheatsheet/)
"""

bootstrap_code = """``` 
    import dash
    import dash_bootstrap_components as dbc
    
    app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
    
    app.layout = dbc.Container(
        dbc.Alert("Hello Bootstrap!", color="success"),
        className="p-5",
    )
    
    if __name__ == "__main__":
        app.run_server(debug=True)
```"""

leaflet_intro = """
    #### __dash-leaflet  Quickstart__
    - [dash-leaflet documentation](https://dash-leaflet.herokuapp.com/)
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
    - [Dash callbacks tutorial](https://dash.plotly.com/basic-callbacks)
"""


callback_code1 = """``` 
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

callback_code = """``` 
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
    - [Dash pattern matching callback tutorial](https://dash.plotly.com/pattern-matching-callbacks)
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
    #### __Datasets: Ploty datasets and generic Pandas dataframes Quickstart__
    - Quick Pandas tutorial: [10 minutes to Pandas](https://pandas.pydata.org/docs/user_guide/10min.html).
"""

datasets_code = """``` 

    '''
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
```"""


callback_extras_intro = """
    #### __Callback Extras __
    -  [Dash advanced callbacks tutorial](https://dash.plotly.com/advanced-callbacks)

    
    `PreventUpdate`
    All outputs of this callback will not update `if n_clicks is None`:
    ```
    from dash.exceptions import PreventUpdate
    
    # code snippet from a dash callback:
    
    def update_output(n_clicks):
        if n_clicks is None:
            raise PreventUpdate
    ```
    
     ---
    
     `dash.no_update`
    First output is not updated and the second one, a graph,  is updated.
    
    ```
        return dash.no_update, figure
    ```
    
    ---
    
    
    `dash.callback_context`
    Use to determine which input triggered the callback
    
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
    
    ---
    This callback will not fire on initial load:
    ```
    @app.callback(Output('container', 'children'),
                   Input('btn-1', 'n_clicks'),
                   Input('btn-2', 'n_clicks'),
                   prevent_initial_call=True
    )
    
    ```
    
    None of the callbacks will fire on initial load:
    ```
    app = Dash(name=__name__, prevent_initial_callbacks=True)
    ```
"""


components_intro = """
  #### __Dash Core Components Quickstart__    
     
     - [Dash Core Components Overview](https://dash.plotly.com/dash-core-components) with code examples.  Find out more 
     by typing in your Python terminal:  `help(dash_core_components.Checklist)` or any other component name. 
     
     - [Dash HTML Components list](https://dash.plotly.com/dash-html-components)

"""

"""
===============================================================================
Tips and Tricks
"""

tips_text = """

    - Try using  a code formatter like [Black](https://black.readthedocs.io/en/stable/). This not only makes your code
    PEP 8 compliant, but it also helps you code faster.  No need to spend a lot of time focusing on things like spacing 
    and alignment - -  Black can do that for you in a sec!  It also makes  your code easier to read and to debug.
    
    - When you have mulitple inputs and outputs, the callbacks can get quite long.  A [best practice](https://github.com/plotly/dash/issues/1054) 
    is to break the callbacks into smaller functions so that a multiple-input callback acts like a router.  (todo AMW - create and link to an example)

    - As you add more features and pages to your app, it can grow to be hundreds( or thousands!) of lines of code.  It then
    becomes even more important to organize your code so it is ieasier to maintain and debug. One method is to use a
    [multi - page app file structure](https://dash.plotly.com/urls)
   
     - To track performance, you can find great information on how long callbacks are taking by using the [Dev tools](https://dash.plotly.com/devtools).
     The callback graph is fascinating!

     -  When using custom colors in your app, consider putting all the colors in a dictionary in the global namespace. Then assign
     the colors using the dictionary. When the colors are defined in one place, it is easier to manage and change the color schemes.
     This becomes even more important as the size of our app grows. See example [here](https://github.com/AnnMarieW/dash-quickstart/blob/master/tips-tricks-and-code-snippets/global_color_dict.py)

    - To see all of the properties available for a component, type this in your Python console:
    ``` help(dash_core_components.Slider)``` or any other component name

    
"""

debugging_text = """  

    - When debugging, it is helpful to use your IDE debug tools, or a debugger such as `ipdb`. Another method is to
    use strategically placed `print` statements(very helpful in callbacks). You can also use `print(fig)` to 
    see how a Plotly figure is defined. 

    -[Here is a great post](https://community.plotly.com/t/solved-dash-layout-not-working-as-expected-general-debugging-tips/4724/4?u=annmariew)
 on the forum about debugging by Chris Parmer, the creator of Dash.  This is from 2017, so some of the information is dated. 
 For example the [Dev tools](https://dash.plotly.com/devtools) have many new features now.  Still, the post has lots of
 helpful debugging tips that still apply.
 
"""


"""
===============================================================================
How to
"""
howto_text = """
  #### __DataTables__  
    
    - How to: [format numbers in a Dash DataTable](https://formattable.pythonanywhere.com/)  This is a handy tutorial
     app to see how the d3-format library is used to format numerical data in a Dash DataTable.  You can make selections 
     and see the code used to format the table.
    
    - How to: [fix a datatable where the first characters are cut off](https://community.plotly.com/t/datatable-incorrectly-displayed-at-left-and-right-edge-and-distort-after-update-columns/41265/6)

    - How to: move the export button.  Add the following to your [css file in the assets folder](https://dash.plotly.com/external-resources)
    ```
    .export
    {
        position: absolute;
    right: 50 %;
    font - type: sans - serif;
    [...]
    }
    ```
    - How to: [move the toggle columns button](https://community.plotly.com/t/datatable-toggle-columns-button-placement-in-python/46768/2)

    - How to: do conditonal formatting.Here is [an app](https://github.com/AnnMarieW/dash-quickstart/blob/master/tips-tricks-and-code-snippets/conditional_formatting.py)
    like the one used in the [Conditional Formatting](https://dash.plotly.com/datatable/conditional-formatting) 
    example from the Dash Tutorial
    
  #### __Bootstrap__

    - How to: make a [model for help text](https://community.plotly.com/t/any-way-to-create-an-instructions-popout/18828/11?u=annmariew)
 
    - How to: make a [live stages progress bar](https://community.plotly.com/t/live-stage-visualization/45095)
    
  #### __Multi-page apps__

    - How to: turn 2 single page apps into a mulit-page app.  We start with [this app](https://dash.plotly.com/interactive-graphing)
    and [this app](https://dash.plotly.com/basic-callbacks) from the Dash Tutorial. See it as a multi-page app in  
    [this directory](https://github.com/AnnMarieW/dash-quickstart/tree/master/tips-tricks-and-code-snippets/multi-page-app).
    This is done following the [Structuring a Multi-Page App](https://dash.plotly.com/urls) example in the Dash Tutorial.
    
    
  #### __Deployment__
    - How to: [deploy your app on Heroku](https://community.plotly.com/t/deploying-your-dash-app-to-heroku-the-magical-guide/46723)

    - How to: [deploy your app on pythonanywhere.com](https://github.com/conradho/dashingdemo)


"""


"""
===============================================================================
More Resources
"""
more_text = """ 


- One of the best sources of information about Dash is in the official Plotly [Dash Tutorial](https://dash.plotly.com/installation)
and documentation.  It's continually being updated as new features are added to Dash and Plotly.  It also has lots of great examples.  

- Check out the  [Dash Community Forum](https://community.plotly.com/). You will probably find an answer in one of the posts,
but if not, try posting a question.

-  Here is a guide on [how to get your questions answered on the forum](https://community.plotly.com/t/how-to-get-your-questions-answered-on-the-plotly-forum/40551).

- Subscribe to  [video tutorials by Charming Data](https://www.youtube.com/channel/UCqBFsuAz41sqWcFjZkqmJqQ/featured)
created by Dash community member Adam Schroeder  
___


This app is a work in progress.  If you have comments or suggestions, please feel free to [start a new issue](https://github.com/AnnMarieW/dash-quickstart/issues/new) 
or do a pull request. I'd be delighted to hear from you!
"""
