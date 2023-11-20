from dash import Dash, dcc, html
import pandas as pd


# Read the data from the CSV file
data = (
    pd.read_csv('Datas.csv')
    .sort_values(by='Year')
)

# Configure stylesheet for web application
external_stylesheets = [
    {
        'href': (
            'https://fonts.googleapis.com/css2?'
            'family=Lato:wght@400;700&display=swap'
        ),
        'rel': 'stylesheet',
    },
]

# Set up the dashboard
app = Dash(__name__, external_stylesheets=external_stylesheets)
app.title = 'Predicting Livestock Production in Somalia'

app.layout = html.Div(
    children=[

        # Graph Title
        html.Div(
            children=[
                html.P(children='🇸🇴', className='header-emoji'),
                html.H1(
                    children='Livestock Production in Somalia per Year',
                    className='header-title'
                ),
                html.P(
                    children=(
                        'Analyze the behavior of livestock production and'
                        ' the amount of foreign aid Somalia receives (in USD).'
                    ),
                    className='header-description'
                )
            ],
            className='header'
        ),

        html.Div(
            children=[

                # Feature Variable Distribution
                html.Div(
                    children=dcc.Graph(
                        id='feature-chart',
                        config={ 'displayModeBar': False },
                        figure={
                            'data': [
                                {
                                    'x': data['Year'],
                                    'y': data['Aid'],
                                    'type': 'lines',
                                    'hovertemplate': (
                                        '$%{y:.2f}<extra></extra>'
                                    ),
                                },
                            ],
                            'layout': {
                                'title': {
                                    'text': 'Net Developmental Assistance provided (USD)',
                                    'x': 0.05,
                                    'xanchor': 'left',
                                },
                                'xaxis': { 'fixedrange': True },
                                'yaxis': {
                                    'tickprefix': '$',
                                    'fixedrange': True,
                                },
                                'colorway': ['#17b897'],
                            },
                        },
                    ),
                    className='card'
                ),

                # Target Variable Distribution
                html.Div(
                    children=dcc.Graph(
                        id='target-chart',
                        config={ 'displayModeBar': False },
                        figure={
                            'data': [
                                {
                                    'x': data['Year'],
                                    'y': data['Livestock'],
                                    'type': 'lines',
                                },
                            ],
                            'layout': {
                                'title': {
                                    'text': 'Livestock Production Index',
                                    'x': 0.05,
                                    'xanchor': 'left',
                                },
                                'xaxis': { 'fixedrange': True },
                                'yaxis': { 'fixedrange': True },
                                'colorway': ['#E12D39'],
                            },
                        },
                    ),
                    className='card'
                )

            ],
            className='wrapper'
        )
    ]
)


if __name__ == '__main__':
    app.run_server(debug=True)
