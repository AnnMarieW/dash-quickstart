
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

"""


"""
===============================================================================
How to DataTables
"""
datatable_format_numbers = """     
     - [Format numbers in a Dash DataTable](https://formattable.pythonanywhere.com/).  This is a handy tutorial
     app to see how the d3-format library is used to format numbers in a Dash DataTable.  You can make selections 
     and see the code used to format the table.
    """

datatable_format_numbers_image = """      
    https://user-images.githubusercontent.com/72614349/100634046-05729c80-32ec-11eb-9dba-a966b36a44ba.png
    """

datatable_fix_cut_off= """    
    - [Fix a datatable where the first characters are cut off](https://community.plotly.com/t/datatable-incorrectly-displayed-at-left-and-right-edge-and-distort-after-update-columns/41265/6)
    """

datatable_move_export_button="""
    - Move the export button.  Add the following to your [css file in the assets folder](https://dash.plotly.com/external-resources)
    
    - And a related issue:  - [Move the toggle columns button](https://community.plotly.com/t/datatable-toggle-columns-button-placement-in-python/46768/2)
    """
datatable_move_export_button_code="""
    ```
    .export
    {
        position: absolute;
    right: 50 %;
    font - type: sans - serif;
    [...]
    }
    ```"""

datatable_conditional_formatting="""
    - Apply conditional formatting: [Here is an app](https://github.com/AnnMarieW/dash-quickstart/blob/master/demo_apps/conditional_formatting.py)
    like the one used in the [Conditional Formatting](https://dash.plotly.com/datatable/conditional-formatting) 
    example from the Dash Tutorial   
  """

image="- ![conditional_format](https://user-images.githubusercontent.com/72614349/100655403-7758df00-3308-11eb-9d6e-079d3114b5eb.png)"
datatable_conditional_formatting2="""
    - Conditional formatting:  Setting background color for column values from a dictionary    
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



"""
===============================================================================
How to Bootstrap
"""

bootstrap_modal = """
    - How to: make a [model for help text](https://community.plotly.com/t/any-way-to-create-an-instructions-popout/18828/11?u=annmariew)
    """
bootstrap_live_stages= """ 
    - How to: make a [live stages progress bar](https://community.plotly.com/t/live-stage-visualization/45095)
    """
bootstrap_live_stages_image= """ 
    https://user-images.githubusercontent.com/72614349/100642053-82eeda80-32f5-11eb-8a5b-dc56d77a85ea.gif
    """

"""
===============================================================================
How to Multi-page apps
"""

multi_page= """
    - How to: turn 2 single page apps into a mulit-page app.  We start with [this app](https://dash.plotly.com/interactive-graphing)
    and [this app](https://dash.plotly.com/basic-callbacks) from the Dash Tutorial. See it as a multi-page app in  
    [this directory](https://github.com/AnnMarieW/dash-quickstart/tree/master/demo_apps/multi-page-app).
    This is done following the [Structuring a Multi-Page App](https://dash.plotly.com/urls) example in the Dash Tutorial.
    """



"""
===============================================================================
How to Deployment
"""

deployment_heroku="""
    - How to: [deploy your app on Heroku](https://community.plotly.com/t/deploying-your-dash-app-to-heroku-the-magical-guide/46723)
    """
deployment_pythonanywhere="""
    - How to: [deploy your app on pythonanywhere.com](https://github.com/conradho/dashingdemo)
    """


"""
===============================================================================
How to General
"""

gen_image_in_bubble="""
    - How to make a [Graph with images inside bubble](https://community.plotly.com/t/put-images-inside-bubbles/41364/2)
    """
gen_image_in_bubble_image="""
    https://user-images.githubusercontent.com/72614349/100633817-c6dce200-32eb-11eb-81a9-fcc3027f50f0.png    
    """

gen_real_time_data="""
    - [Dash with real time data](https://stackoverflow.com/questions/63589249/plotly-dash-display-real-time-data-in-smooth-animation)
    """

gen_real_time_data_image="""
    https://user-images.githubusercontent.com/72614349/100633819-c7757880-32eb-11eb-828e-594aeb5fad54.gif
    """

gen_pattern_matching="""
    [Pattern Matching Callback](https://community.plotly.com/t/pattern-call-backs-regarding-adding-dynamic-graphs/40724/4?u=annmariew)
    with deleteable charts.
    """
gen_pattern_matching_image="""
    https://user-images.githubusercontent.com/72614349/100633822-c8a6a580-32eb-11eb-975e-329f50689904.gif
    """

gen_tabulator="""
    [Dash Tabulator component example](https://community.plotly.com/t/tabulator-dash-component/42261/21?u=annmariew)
    Some nice Tabulator features: 
    
        - case insensitive filters
        - calculations like sums and averages on columns
        - group by       
    
    """
gen_tabulator_image="""
    https://user-images.githubusercontent.com/72614349/100633820-c7757880-32eb-11eb-916d-3b395edfa8a5.gif
    """