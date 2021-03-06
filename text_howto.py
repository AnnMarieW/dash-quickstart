
import pathlib
# set relative path
PATH = pathlib.Path(__file__).parent
DEMO_APPS_PATH = PATH.joinpath("./demo_apps").resolve()
# be sure to include a blank line and docstring at start of source file
# with open(DEMO_APPS_PATH.joinpath("conditional_formatting.py")) as f:
#     code = f.read()
# code  = f"```{code}```"

"""
================================================================================
IMAGES
"""

"""

![graph-images-in-bubbles](https://user-images.githubusercontent.com/72614349/100633817-c6dce200-32eb-11eb-81a9-fcc3027f50f0.png)
![real-time-data](https://user-images.githubusercontent.com/72614349/100633819-c7757880-32eb-11eb-828e-594aeb5fad54.gif)
![tabulator](https://user-images.githubusercontent.com/72614349/100633820-c7757880-32eb-11eb-916d-3b395edfa8a5.gif)
![pattern-matching](https://user-images.githubusercontent.com/72614349/100633822-c8a6a580-32eb-11eb-975e-329f50689904.gif)
![format_helper](https://user-images.githubusercontent.com/72614349/100634046-05729c80-32ec-11eb-9dba-a966b36a44ba.png
![progress_bar](https://user-images.githubusercontent.com/72614349/100642053-82eeda80-32f5-11eb-8a5b-dc56d77a85ea.gif)
![cookie_monster](https://todaysmama.com/.image/t_share/MTU5OTEwMzkyMDIyMTE1NzAz/cookie-monster.png#thumbnail)
"""


"""
===============================================================================
How to DataTables
"""

datatable_format_numbers = """    
    #### How to format numbers
     - Here is an [app](https://formattable.pythonanywhere.com/).  to help format numbers in the Dash DataTable.
       You can make selections and see the code used to format the table.
    """

datatable_format_numbers_image = """     
    https://user-images.githubusercontent.com/72614349/100634046-05729c80-32ec-11eb-9dba-a966b36a44ba.png
    """


datatable_format_dates="""
    #### How to format dates
    When formatting numbers in a DataTable with the `format` parameter, only the display format changes. The number 
    itself does not change. For dates, it's necessary to change the datetime object to a string. The following
    code shows different format options using dt.strftime. Note: for dates to sort correctly, the 
    date should be formatted as YYYY-MM-DD.  
"""

datatable_format_dates_code="""```
import dash
import dash_table
import pandas as pd

app = dash.Dash(__name__)

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

df["Date"] = pd.to_datetime(df["Date"])
df["Date1"] = df["Date"].dt.date
df["Date2"] = df["Date"].dt.strftime("%m/%d/%Y")
df["Date3"] = df["Date"].dt.strftime("%a, %b %-d, %Y")


app.layout = dash_table.DataTable(
    data=df.to_dict("records"),
    sort_action="native",
    columns=[
        {"name": "Date", "id": "Date", "type": "datetime", "editable": False},
        {"name": "Date1", "id": "Date1", "type": "datetime"},
        {"name": "Date2", "id": "Date2", "type": "datetime"},
        {"name": "Date3", "id": "Date3", "type": "datetime"},
        {"name": "Region", "id": "Region", "type": "text"},
        {"name": "Temperature", "id": "Temperature", "type": "numeric"},
        {"name": "Humidity", "id": "Humidity", "type": "numeric"},
        {"name": "Pressure", "id": "Pressure", "type": "any"},
    ],
    editable=True,
)

if __name__ == "__main__":
    app.run_server(debug=True)
```"""





datatable_fix_cut_off= """   
    ---
    
    #### How to fix rows with cut off data 
    - When using Bootstrap with the DataTable there is a conflict with the row class that will cause the data to overflow
    the table container.  It can be fixed with some custom css. See more info
    [here](https://dash-bootstrap-components.opensource.faculty.ai/docs/faq/)
    
    Breaking News... as of Dec 2020, this was fixed.  Now all you need to do is upgrade to the latest version of Dash!
    
    """

datatable_move_export_button="""
---
#### How to move the export or toggle button
Here are two ways to move the buttons to the bottom of the table.  Change the "rule" to move the buttons to other
locations.
"""
datatable_move_export_button_code="""
    ```
    import dash
    import dash_table
    import pandas as pd
    
    df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/solar.csv")
    
    app = dash.Dash(__name__)
    
    app.layout = dash_table.DataTable(
        id="table",
        columns=[{"name": i, "id": i, "hideable": True} for i in df.columns],
        export_format="xlsx",
        css=[
            # If export button only,  use this:
            #{"selector": ".export", "rule": "position:absolute; left: 0px; bottom:-30px"},
            
            # If both export button and toggle columns button,  use this:
            {
                "selector": ".dash-spreadsheet-menu",
                "rule": "position:absolute; left:0px; bottom:-30px",
            },
        ],
        data=df.to_dict("records"),
    )
    
    if __name__ == "__main__":
        app.run_server(debug=True)
    ```"""

datatable_conditional_formatting="""
---
#### How to do conditional formatting

- Here is an [app](https://github.com/AnnMarieW/dash-quickstart/blob/master/demo_apps/conditional_formatting.py)
like the one used in the [Conditional Formatting](https://dash.plotly.com/datatable/conditional-formatting) 
chapter in the Dash Tutorial.  This is a helpful quickstart app.
"""

image="- ![conditional_format](https://user-images.githubusercontent.com/72614349/100655403-7758df00-3308-11eb-9d6e-079d3114b5eb.png)"
datatable_conditional_formatting2="""

- The following is an example app to show how to set the background color for column based on the values in the column:  
"""
datatable_conditional_formatting2_code="""```
    import dash
    import dash_table
    import pandas as pd
    
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
    
    # keys are the "Humidity" data
    colors = {
        10: "#c54040",
        20: "#c58d36",
        30: "#65c336",
        40: "#32c1be",
        50: "#483dbe",
        60: "#000000",
    }
    
    app = dash.Dash(__name__)
    
    app.layout = dash_table.DataTable(
        data=df.to_dict("records"),    
        columns=[{"name": i, "id": i} for i in df.columns],
        style_data_conditional=[
            {
                "if": {
                    "column_id": "Humidity",
                    "filter_query": "{{Humidity}} = {}".format(i),
                },
                "backgroundColor": colors[i],
                "color": "white",
            }
            for i in colors
        ],
    )
    
    if __name__ == "__main__":
        app.run_server(debug=True)
    ```"""

datatable_spark_intro="""
---
#### How to add sparklines 
- See this discussion on the forum for more information and code for the app in image below: [Sparklines as Fonts in a DataTable](https://community.plotly.com/t/sparklines-as-fonts-embedding-minimal-sparklines-in-tables-components/39468)
  
"""

datatable_spark_image="""    
    https://user-images.githubusercontent.com/72614349/101054462-27fff200-3546-11eb-8e25-48b594bb307f.gif
    """


"""
===============================================================================
How to Bootstrap
"""

bootstrap_modal = """
    #### How to use modals
    - See an example here: [modal for help text](https://community.plotly.com/t/any-way-to-create-an-instructions-popout/18828/11?u=annmariew)
    """
bootstrap_live_stages= """ 
    #### How to make a progress bar
    - How to: make a [live stages progress bar](https://community.plotly.com/t/live-stage-visualization/45095)
    """
bootstrap_live_stages_image= """ 
    https://user-images.githubusercontent.com/72614349/100642053-82eeda80-32f5-11eb-8a5b-dc56d77a85ea.gif
    """



"""
===============================================================================
How to Markdown
"""

markdown_css="""
#### How to style blockquotes and tables in dcc.Markdown
- Blockquotes and tables are unstyled by default in Bootstrap. When using dcc.Markdown with Bootstrap add the following 
to the .css file in the assets folder to add style to the Block quotes and Tables
"""

markdown_css_code="""```

/*  when using Bootstrap, this will add row borders to the table in dcc.Markdown
 *   Table
–––––––––––––––––––––––––––––––––––––––––––––––––– */
table {
  border-collapse: collapse;
}
th:not(.CalendarDay),
td:not(.CalendarDay) {
  padding: 12px 15px;
  text-align: left;
  border-bottom: 1px solid #E1E1E1; }
th:first-child:not(.CalendarDay),
td:first-child:not(.CalendarDay) {
  padding-left: 0; }
th:last-child:not(.CalendarDay),
td:last-child:not(.CalendarDay) {
  padding-right: 0; }



/* When using Bootstrap, this will add the left border style to blockquotes in dcc.Markdown */
/* Blockquotes
–––––––––––––––––––––––––––––––––––––––––––––––––– */
blockquote {
  border-left: 4px lightgrey solid;
  padding-left: 1rem;
  margin-top: 2rem;
  margin-bottom: 2rem;
  margin-left: 0rem;
}

```"""

markdown_image_size = '''
---
#### How to resize an image

 - To resize an image when using dcc.Markdown, add a URL parameter to the file name.  In this example it's #thumbnail:  
 
    `![cookie_monster](https://todaysmama.com/.image/t_share/MTU5OTEwMzkyMDIyMTE1NzAz/cookie-monster.png#thumbnail)`
    
    Then adjust the size in the .css file:
    ```
    img[src*="#thumbnail"] {
       width:100px;
       height:100px;
    }
    ```
    ![cookie_monster](https://todaysmama.com/.image/t_share/MTU5OTEwMzkyMDIyMTE1NzAz/cookie-monster.png#thumbnail)  
     
    If the image is in the assets directory, use this:
    `dcc.Markdown('![]({})'.format(app.get_asset_url('my_image.svg#thumbnail')))`
    
    To embed the image with other text, it needs to be a single string:  
    
    `dcc.Markdown("My intro text" + '![]({})'.format(app.get_asset_url('my_image.svg#thumbnail')) + "My other text")`
        
    '''


"""gauge.png
===============================================================================
How to Dash DAQ
"""

dash_daq="""
    #### How to style a daq.Gauge with custom css
    Dash DAQ has a set of controls that make it simpler to integrate 
    data acquisition and controls into your Dash apps.
    See the [overview](https://dash.plotly.com/dash-daq) for more info.    
    
    This example shows how to use custom css to change the size of the text. See this 
    [discussion](https://community.plotly.com/t/dash-daq-gauge-font-size/25453/6?u=annmariew) on the forum    
    
    ![gauge](https://user-images.githubusercontent.com/72614349/102272420-f986fd00-3edd-11eb-87c3-a8c7d10d84f5.png#gauge)

"""

dash_daq2="""
    -----
    #### How to style a daq.Guage with a custom scale
    See this example on the [forum](https://community.plotly.com/t/how-to-change-space-between-radio-button-and-label-font-size-of-gauges/39912/7)

"""

with open(DEMO_APPS_PATH.joinpath("daq_gauge.py")) as f:
    dash_daq_code = f.read()
dash_daq_code  = f"```{dash_daq_code}```"

"""
===============================================================================
How to Deployment
"""

deployment="""
    ---
    #### How to deploy your app
    - How to: [deploy your app on Heroku](https://community.plotly.com/t/deploying-your-dash-app-to-heroku-the-magical-guide/46723)

    - How to: [deploy your app on pythonanywhere.com](https://github.com/conradho/dashingdemo)
    """


"""
===============================================================================
How to General
"""


gen_multi_page= """
    #### How to make a multi-page app
    - The [multi-page app in this directory](https://github.com/AnnMarieW/dash-quickstart/tree/master/demo_apps/multi-page-app)
    was created using these two single page apps from the Dash Tutorial as [app1](https://dash.plotly.com/interactive-graphing) and [app2](https://dash.plotly.com/basic-callbacks) 
    It follows the [Structuring a Multi-Page App](https://dash.plotly.com/urls) example to create
    the multi page app.  
    """



gen_image_in_bubble="""
    ---
    #### How to make a graph with images inside bubbles
    - See the code [here](https://community.plotly.com/t/put-images-inside-bubbles/41364/2)
    """
gen_image_in_bubble_image="""
    https://user-images.githubusercontent.com/72614349/100633817-c6dce200-32eb-11eb-81a9-fcc3027f50f0.png    
    """

gen_real_time_data="""
    #### How to make a graph with real time data
    - See the code [here](https://stackoverflow.com/questions/63589249/plotly-dash-display-real-time-data-in-smooth-animation)
    """

gen_real_time_data_image="""
    https://user-images.githubusercontent.com/72614349/100633819-c7757880-32eb-11eb-828e-594aeb5fad54.gif
    """

gen_pattern_matching="""
    ---
    #### How to do pattern matching callbacks
    Here is an example of [pattern matching callbacks](https://community.plotly.com/t/pattern-call-backs-regarding-adding-dynamic-graphs/40724/4?u=annmariew)
    This app has deletable charts.  See pattern matching callbacks tutorial [here](https://dash.plotly.com/pattern-matching-callbacks).
    """
gen_pattern_matching_image="""
    https://user-images.githubusercontent.com/72614349/100633822-c8a6a580-32eb-11eb-975e-329f50689904.gif
    """

gen_tabulator="""
    ---
    #### How to use dash-tabulator 
    This is an example app using the [Dash Tabulator component](https://community.plotly.com/t/tabulator-dash-component/42261/21?u=annmariew)
    The Tabulator table has some nice features that the Dash DataTable does not have yet, such as case insensitive filters
    and group-by functionality.  There is also an option to include calculations like sums and averages.
       
    """
gen_tabulator_image="""
    https://user-images.githubusercontent.com/72614349/100633820-c7757880-32eb-11eb-916d-3b395edfa8a5.gif
    """

gen_copy_to_clipboard="""
    ---
    #### How to copy to the clipboard
    Here is how to [copy text to a clipboard](https://github.com/AnnMarieW/dash-quickstart/blob/master/demo_apps/copy_to_clipboard.py)
     on a button click - like on the Quickstart page of this app
"""


gen_options="""
---
#### How to create options for dropdowns
How to make options for dropdowns from 2 columns of a dataframe
"""

gen_options_code="""```
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

data = dict(
        [
            ("Account", [1000, 1001, 1010, 1020, 1030]),
            ("Description", ["Assets", "Cash", "Accounts Receivable", "Prepaid Expenses", "Inventory",]),

        ]
    )
df = pd.DataFrame(data)

options= [{'label': l, 'value':v} for l,v in dict(zip(df['Description'], df['Account'])).items()]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
app.layout = html.Div([
    dcc.Dropdown(
        id='account-dropdown',
        options=options,
        value=1000
    ),
    html.Div(id='output-div')
])


@app.callback(Output('output-div', 'children'), Input('account-dropdown', 'value'))
def update(account):
    return f'You have selected {account}'


if __name__ == '__main__':
    app.run_server(debug=True)
```"""