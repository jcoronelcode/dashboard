import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objects as go


app = dash.Dash()

#Carga de datos
df_sp500 = pd.read_csv(r'./SP500_data_.csv', encoding='ISO-8859-1', delimiter=',')

#Objetos plotly.graph
data1 = [go.Scatter( 
    x=df_sp500['Date'], 
    y=df_sp500['Close'], 
    mode='lines')
        ]

layout1 = go.Layout(
    title='S&P 500 Cotizacion Prueba',
    xaxis=dict(title='Fecha'),
    yaxis=dict(title='SP500 valor')
)

data2 = [go.Scatter(
    x=df_sp500['Date'], 
    y=df_sp500['Volume'])
        ]

layout2 = go.Layout(
    title='S&P 500 Volumen',
    xaxis=dict(title='Fecha'),
    yaxis=dict(title='SP500 volumen')
)

#Definicion del layout de la app a partir de componentes HTML y core
app.layout = html.Div([
                    html.Label('Seleccionar el tipo de grafico'),
                    dcc.Dropdown(
                        options=[
                            {'label' : 'Apertura', 'value' : 'Open'},
                            {'label' : 'Cierre', 'value' : 'Close'},
                            {'label' : 'Máximo', 'value' : 'High'},
                            {'label' : 'Mínimo', 'value' : 'Low'},
                            {'label' : 'Volumen', 'value' : 'Volume'}
                        ], value='Close',id='dropdown'),
                    dcc.Graph(id='lineplot', figure={'data': data1, 'layout': layout1}),
                    dcc.Graph(id='lineplot2', figure={'data': data2, 'layout': layout2})
                    ])


if __name__ == '__main__':
    app.run_server(port=7000)