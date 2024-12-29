import dash
from dash import dcc
from dash import html
import pandas as pd
import plotly.graph_objects as go
from dash.dependencies import Input, Output

# Carga de datos
df_temperatura = pd.read_excel('../Datasets y Scripts Plotly Dash/Datasets/5.2/Temperaturas.xlsx')


app = dash.Dash()

# Definicion del layout de la app a partir de componentes HTML y core
app.layout = html.Div([
    dcc.Graph(id='graph_linea'),
    dcc.DatePickerRange(id='selector-fecha', start_date=df_temperatura['FECHA'].min(), end_date=df_temperatura['FECHA'].max())
])

# Creacion de Graficos e interactividad
# Callbacks para actualizar el grafico segun la fecha seleccionada

@app.callback(Output('graph_linea', 'figure'),[Input('selector-fecha', 'start_date'), Input('selector-fecha', 'end_date')])

def update_graph(start_date, end_date):
    df_filtered = df_temperatura[(df_temperatura['FECHA'] >= start_date) & (df_temperatura['FECHA'] <= end_date)]
    
    # Creacion de trazas por cada ciudad de nuestro dataframe
    trazas = []
    
    for ciudad in df_filtered['Ciudad'].unique():
        df_ciudad = df_filtered[df_filtered['Ciudad'] == ciudad]
        traza = go.Scatter(
                        x=df_ciudad['FECHA'], 
                        y=df_ciudad['T_Promedio'], 
                        mode='lines', 
                        name=ciudad,
                        opacity=0.7,
                        marker={'size': 15},
                        text=df_ciudad['Ciudad']
                        )
        trazas.append(traza)
    
    return {'data': trazas, 
            'layout': go.Layout(title='Temperaturas por Ciudad', 
                                xaxis=dict(title='FECHA'), 
                                yaxis=dict(title='Temperatura media (°C)'))
            }
    
# Sentencias para abrir el servidor al ejecutar el script
if __name__ == '__main__':
    app.run_server(port=7000)