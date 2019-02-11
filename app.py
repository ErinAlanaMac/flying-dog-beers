import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

########### Set up the chart with each beer
beers=['Session IPA', 'Ken Dog IPA', 'Ken Dog IIPA DDH', 'Ken Dog Triple IPA']

########### Input IBU data for each beer
bitterness = go.Bar(
    x=beers,
    y=[35, 80, 100, 120],
    name='IBU',
    marker={'color':'green'}
)
########## Input ABV for each beer
alcohol = go.Bar(
    x=beers,
    y=[5.4, 7.1, 9.2, 12.0],
    name='ABV',
    marker={'color':'lightgreen'}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = 'Beer Comparison'
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

########### Display the chart

app = dash.Dash()
server = app.server

app.layout = html.Div(children=[
    html.H1('Ken Dog Brewery'),
    dcc.Graph(
        id='flyingdog',
        figure=beer_fig
    )]
)

if __name__ == '__main__':
    app.run_server()
