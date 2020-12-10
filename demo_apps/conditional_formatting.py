import dash
import dash_table
import pandas as pd

data = dict(
    [
        ("Date", ["2015-01-01", "2015-10-24", "2016-05-10", "2017-01-10", "2018-05-10", "2018-08-15"]),
        ("Delivery", ["2015-01-02", "2015-8-24", "2016-05-11", "2017-01-1", "2018-05-11", "2018-08-14"]),
        ("Region", ["Montreal", "Toronto", "New York City", "Miami", "San Francisco", "London"]),
        ("Temperature", [1, -20, 3.512, 4, 10423, -441.2]),
        ("Humidity", [10, 20, 30, 40, 50, 60]),
        ("Pressure", [2, 10924, 3912, -10, 3591.2, 15]),
    ]
)
df = pd.DataFrame(data)

app = dash.Dash(__name__)

df['id'] = df.index
app.layout = dash_table.DataTable(
    data=df.to_dict('records'),
    sort_action='native',
    columns=[
        {'name': 'Date', 'id': 'Date', 'type': 'datetime', 'editable': False},
        {'name': 'Delivery', 'id': 'Delivery', 'type': 'datetime'},
        {'name': 'Region', 'id': 'Region', 'type': 'text'},
        {'name': 'Temperature', 'id': 'Temperature', 'type': 'numeric'},
        {'name': 'Humidity', 'id': 'Humidity', 'type': 'numeric'},
        {'name': 'Pressure', 'id': 'Pressure', 'type': 'any'},
    ],
    editable=True,
    style_data_conditional=[
        {
            'if': {
                'column_id': 'Region',
            },
            'backgroundColor': 'dodgerblue',
            'color': 'white'
        },
        {
            'if': {
                'filter_query': '{Humidity} > 19 && {Humidity} < 41',
                'column_id': 'Humidity'
            },
            'backgroundColor': 'tomato',
            'color': 'white'
        },

        {
            'if': {
                'column_id': 'Pressure',

                # since using .format, escape { with {{
                'filter_query': '{{Pressure}} = {}'.format(df['Pressure'].max())
            },
            'backgroundColor': '#85144b',
            'color': 'white'
        },

        {
            'if': {
                'row_index': 5,  # number | 'odd' | 'even'
                'column_id': 'Region'
            },
            'backgroundColor': 'hotpink',
            'color': 'white'
        },

        {
            'if': {
                'filter_query': '{id} = 4',  # matching rows of a hidden column with the id, `id`
                'column_id': 'Region'
            },
            'backgroundColor': 'RebeccaPurple'
        },

        {
            'if': {
                'filter_query': '{Delivery} > {Date}', # comparing columns to each other
                'column_id': 'Delivery'
            },
            'backgroundColor': '#3D9970'
        },

        {
            'if': {
                'column_editable': False  # True | False
            },
            'backgroundColor': 'rgb(240, 240, 240)',
            'cursor': 'not-allowed'
        },

        {
            'if': {
                'column_type': 'text'  # 'text' | 'any' | 'datetime' | 'numeric'
            },
            'textAlign': 'left'
        },

        {
            'if': {
                'state': 'active'  # 'active' | 'selected'
            },
           'backgroundColor': 'rgba(0, 116, 217, 0.3)',
           'border': '1px solid rgb(0, 116, 217)'
        }

    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)