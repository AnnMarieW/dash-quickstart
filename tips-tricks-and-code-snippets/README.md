# Tips and Tricks

- When you have multiple inputs and outputs, the callbacks can get quite verbose.  It's a 
[best practice](https://github.com/plotly/dash/issues/1054) to break the callbacks into smaller functions
 so that a multiple-input callback is more a router. (todo AMW - create an example)

- As you add more features and pages to your app, it can grow to be hundreds (or thousands!) of lines of code. 
 It then becomes even more important to organize your code so it's easier to 
maintain and debug. One method is to to use a [multi-page app file structure](https://dash.plotly.com/urls)

- When debugging, it's helpful to use your IDE's debug tools, or a debugger such as `ipdb`.
Another method is to use strategically placed `print` statements (very helpful in callbacks).
Note that you can also use`print(fig)` to see how a  Plotly figure is defined.

- To track performance, you can find great information on how long callbacks are taking by using the 
[Dev tools](https://dash.plotly.com/devtools).  The callback graph is fascinating!

# How To:

### __DataTables__
- [How to: format numbers in a Dash DataTable](https://formattable.pythonanywhere.com/)

    This is a handy tutorial app to see how the d3-format library is used to format numerical data
    in a dash datatable. You can make selections and see the code used to format the table
    
- [How to: fix a datatable where the first characters are cut off](https://community.plotly.com/t/datatable-incorrectly-displayed-at-left-and-right-edge-and-distort-after-update-columns/41265/6)

- How to: move the export button --> Add the following to your [css file in the assets folder](https://dash.plotly.com/external-resources)
```
.export{
    position: absolute;
    right: 50%;
    font-type: sans-serif;
    [...]
}
```

- [How to: move the toggle columns button](https://community.plotly.com/t/datatable-toggle-columns-button-placement-in-python/46768/2)

### __It's Live!__
- [How to: deploy your app on Heroku](https://community.plotly.com/t/deploying-your-dash-app-to-heroku-the-magical-guide/46723)

- [How to: deploy your app on pythonanywhere.com](https://github.com/conradho/dashingdemo)