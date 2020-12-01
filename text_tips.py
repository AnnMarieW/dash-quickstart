
"""
===============================================================================
Tips and Tricks
"""

tips_text = """

    - Try using  a code formatter like [Black](https://black.readthedocs.io/en/stable/). This not only makes your code
    PEP 8 compliant, but it also helps you code faster.  No need to spend a lot of time focusing on things like spacing 
    and alignment - -  Black can do that for you in a sec!  It also makes  your code easier to read and to debug.
    
    - When you have mulitple inputs and outputs, the callbacks can get quite long.  A [best practice](https://github.com/plotly/dash/issues/1054) 
    is to break the callbacks into smaller functions so that a multiple-input callback acts like a router. 

    - As you add more features and pages to your app, it can grow to be hundreds( or thousands!) of lines of code.  It then
    becomes even more important to organize your code so it is easier to maintain and debug. One method is to use a
    [multi - page app file structure](https://dash.plotly.com/urls)
   
     - To track performance, you can find great information on how long callbacks are taking by using the [Dev tools](https://dash.plotly.com/devtools).
     The callback graph is fascinating!

     -  When using custom colors in your app, consider putting all the colors in a dictionary in the global namespace. Then assign
     the colors using the dictionary. When the colors are defined in one place, it is easier to manage and change the color schemes.
     This becomes even more important as the size of our app grows. See example [here](https://github.com/AnnMarieW/dash-quickstart/blob/master/demo_apps/global_color_dict.py)

    - To see all of the properties available for a component, type this in your Python console:
    ``` help(dash_core_components.Slider)``` or any other component name

    
"""

debugging_text = """  

    - When debugging, it is helpful to use your IDE debug tools, or a debugger such as `ipdb`. Another method is to
    use strategically placed `print` statements(very helpful in callbacks). You can also use `print(fig)` to 
    see how a Plotly figure is defined. 

    - Here is a [great post](https://community.plotly.com/t/solved-dash-layout-not-working-as-expected-general-debugging-tips/4724/4?u=annmariew)
 on the forum about debugging by @chirddyp.  This is from 2017, so be sure to check out the upgrades to the Dev tools [here](https://dash.plotly.com/devtools) 
 
"""

"""
Notes for more debugging text:
    When callbacks don't fire:
        put a print stmt inside to verify
        check no blank line between callback decorator and function
        double, triple check spelling, dashes vs underscores,  capital vs lower case for the component ids
        make sure that the number of input variables matches the number of inputs in decorator - including n_intervals
        
    When figures don't show up:
        check that there is data sent - sometimes the user selected filter, filters ALL the data
        
    When datatables are blank
        check that id and name are not reversed
        column names cannot be integer (verify?)
        check that data is returned in the right format.  Can't be a df
        
        


"""
