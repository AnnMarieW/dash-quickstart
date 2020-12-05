
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
    #### Formatting numbers
     - Here is an [app](https://formattable.pythonanywhere.com/).  to help format numerical data in the datatable.
       You can make selections and see the code used to format the table.
    """

datatable_format_numbers_image = """     
    https://user-images.githubusercontent.com/72614349/100634046-05729c80-32ec-11eb-9dba-a966b36a44ba.png
    """

datatable_fix_cut_off= """   
    ---
    
    #### Fix rows with cut off data 
    - When using Bootstrap with the datatable there is a conflict with the row class that will cause the data to overflow
    the table container.  It can be fixed with some custom css. See more info
    [Here](https://dash-bootstrap-components.opensource.faculty.ai/docs/faq/)"""

datatable_move_export_button="""
---
#### Move export button
- Add the following to your [css file in the assets folder](https://dash.plotly.com/external-resources) to move the export button.  
- And a related issue -- here is how to [Move the toggle columns button](https://community.plotly.com/t/datatable-toggle-columns-button-placement-in-python/46768/2)
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
---
#### Conditional Formatting

- [Here is an app](https://github.com/AnnMarieW/dash-quickstart/blob/master/demo_apps/conditional_formatting.py)
like the one used in the [Conditional Formatting](https://dash.plotly.com/datatable/conditional-formatting) 
chapter in the Dash Tutorial.
"""

image="- ![conditional_format](https://user-images.githubusercontent.com/72614349/100655403-7758df00-3308-11eb-9d6e-079d3114b5eb.png)"
datatable_conditional_formatting2="""

- The following is an example of how to set the background color for column based on the values in the column:  
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
#### Sparklines 
- How to add [Sparklines as Fonts in a DataTable](https://community.plotly.com/t/sparklines-as-fonts-embedding-minimal-sparklines-in-tables-components/39468)  
"""

datatable_spark_image="""    
    https://user-images.githubusercontent.com/72614349/101054462-27fff200-3546-11eb-8e25-48b594bb307f.gif
    """


"""
===============================================================================
How to Bootstrap
"""

bootstrap_modal = """
    - How to: make a [modal for help text](https://community.plotly.com/t/any-way-to-create-an-instructions-popout/18828/11?u=annmariew)
    """
bootstrap_live_stages= """ 
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



"""
===============================================================================
How to Deployment
"""

deployment="""
    ---
    #### Deployment
    - How to: [deploy your app on Heroku](https://community.plotly.com/t/deploying-your-dash-app-to-heroku-the-magical-guide/46723)

    - How to: [deploy your app on pythonanywhere.com](https://github.com/conradho/dashingdemo)
    """


"""
===============================================================================
How to General
"""


gen_multi_page= """
    #### Multi Page Apps
    - The [multi-page app in this directory](https://github.com/AnnMarieW/dash-quickstart/tree/master/demo_apps/multi-page-app)
    was created using these two single page apps as [app1](https://dash.plotly.com/interactive-graphing) and [app2](https://dash.plotly.com/basic-callbacks) 
    from the Dash Tutorial.  It follows the [Structuring a Multi-Page App](https://dash.plotly.com/urls) example to create
    the multi page app.  
    """



gen_image_in_bubble="""
    ---
    #### Graphs
    - How to make a [Graph with images inside bubble](https://community.plotly.com/t/put-images-inside-bubbles/41364/2)
    """
gen_image_in_bubble_image="""
    https://user-images.githubusercontent.com/72614349/100633817-c6dce200-32eb-11eb-81a9-fcc3027f50f0.png    
    """

gen_real_time_data="""
    - Here is a graph with [real time data](https://stackoverflow.com/questions/63589249/plotly-dash-display-real-time-data-in-smooth-animation)
    """

gen_real_time_data_image="""
    https://user-images.githubusercontent.com/72614349/100633819-c7757880-32eb-11eb-828e-594aeb5fad54.gif
    """

gen_pattern_matching="""
    ---
    #### Pattern Matching Callbacks
    Here is an example of a [Pattern Matching Callback](https://community.plotly.com/t/pattern-call-backs-regarding-adding-dynamic-graphs/40724/4?u=annmariew)
    with deletable charts.
    """
gen_pattern_matching_image="""
    https://user-images.githubusercontent.com/72614349/100633822-c8a6a580-32eb-11eb-975e-329f50689904.gif
    """

gen_tabulator="""
    ---
    #### Dash Tabulator 
    This is an example app using the [Dash Tabulator component](https://community.plotly.com/t/tabulator-dash-component/42261/21?u=annmariew)
    The Tabulator table has some nice features that the Dash DataTable does not have yet such as case insensitive filters,
    and group-by functionality.  There is also an option to include calculations ike sums and averages.
       
    """
gen_tabulator_image="""
    https://user-images.githubusercontent.com/72614349/100633820-c7757880-32eb-11eb-916d-3b395edfa8a5.gif
    """

gen_copy_to_clipboard="""
    ---
    #### Copy to Clipboard
    Here is how to [copy text to a clipboard](https://github.com/AnnMarieW/dash-quickstart/blob/master/demo_apps/copy_to_clipboard.py)
     on a button click - like on the Quickstart page of this app


"""