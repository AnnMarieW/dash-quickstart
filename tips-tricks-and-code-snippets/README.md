# How To:

### __DataTables__

- How to: [format numbers in a Dash DataTable](https://formattable.pythonanywhere.com/)

    This is a handy tutorial app to see how the d3-format library is used to format numerical data
    in a dash datatable. You can make selections and see the code used to format the table
    
- How to: [fix a datatable where the first characters are cut off](https://community.plotly.com/t/datatable-incorrectly-displayed-at-left-and-right-edge-and-distort-after-update-columns/41265/6)

- How to: move the export button --> Add the following to your [css file in the assets folder](https://dash.plotly.com/external-resources)
```
.export{
    position: absolute;
    right: 50%;
    font-type: sans-serif;
    [...]
}
```

- How to: [move the toggle columns button](https://community.plotly.com/t/datatable-toggle-columns-button-placement-in-python/46768/2)


- How to: do conditonal formatting.  Here is [an app](https://github.com/AnnMarieW/dash-quickstart/blob/master/tips-tricks-and-code-snippets/conditional_formatting.py) 
like the one used in the [Conditional Formatting](https://dash.plotly.com/datatable/conditional-formatting) example from the Dash Tutorial


### __Bootstrap__

- How to: make a [model for help text](https://community.plotly.com/t/any-way-to-create-an-instructions-popout/18828/11?u=annmariew)

- How to: make a [live stages progress bar](https://community.plotly.com/t/live-stage-visualization/45095)

### __Multi-page apps__

 - How to: turn 2 single page apps into a multi-page app. We start with [this app](https://dash.plotly.com/interactive-graphing) 
 and [this app](https://dash.plotly.com/basic-callbacks) from the Dash Tutorial.  See it as a multi-page app in 
 [this directory](https://github.com/AnnMarieW/dash-quickstart/tree/master/tips-tricks-and-code-snippets/multi-page-app).
 This is done following the [Structuring a Multi-Page App](https://dash.plotly.com/urls) example.



### __Deployment__
- How to: [deploy your app on Heroku](https://community.plotly.com/t/deploying-your-dash-app-to-heroku-the-magical-guide/46723)

- How to: [deploy your app on pythonanywhere.com](https://github.com/conradho/dashingdemo)

---


# Tips and Tricks

- When you have multiple inputs and outputs, the callbacks can get quite long.  A 
[best practice](https://github.com/plotly/dash/issues/1054) is to break the callbacks into smaller functions
 so that a multiple-input callback acts like a router. (todo AMW - create and link to an example)

- As you add more features and pages to your app, it can grow to be hundreds (or thousands!) of lines of code. 
 It then becomes even more important to organize your code so it's easier to 
maintain and debug. One method is to to use a [multi-page app file structure](https://dash.plotly.com/urls)

- When debugging, it's helpful to use your IDE's debug tools, or a debugger such as `ipdb`.
Another method is to use strategically placed `print` statements (very helpful in callbacks).
Note that you can also use`print(fig)` to see how a  Plotly figure is defined.  See more on debugging in the error
message topic.

- To track performance, you can find great information on how long callbacks are taking by using the 
[Dev tools](https://dash.plotly.com/devtools).  The callback graph is fascinating!

- When using custom colors in your app, put all the colors in a dictionary in the global namespace. Then assign the colors 
using the dictionary.   When the colors are defined in one place, it's easier to manage and change the color schemes.  
This becomes even more important as the size of you app grows. See example [here](https://github.com/AnnMarieW/dash-quickstart/blob/master/tips-tricks-and-code-snippets/global_color_dict.py)
  
- To see all of the properties available for a component,  type this in your Python console:
``` help(dash_core_components.Slider)```   or any other component name

- Use a code formatter like [Black](https://black.readthedocs.io/en/stable/).  This will not only make your code PEP 8 
compliant, but it also helps you code faster.  No need to spend a lot of time focusing things like 
spacing and alignment --  Black can do that for you in a sec!
It also makes your code easier to read and to debug, and makes you look like Python Pro.
