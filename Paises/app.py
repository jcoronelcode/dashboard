import pandas as pd
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import dash
import plotly.graph_objects as go

app = dash.Dash()

df_pais = pd.read_excel("./Info_pais.xlsx")

# print(df_pais.head())
# print(df_pais.columns)

variables = df_pais.columns  # Lista de columnas que estaran en el dropdown

# Definicion del layout
app.layout = html.Div(
    [
        html.Div(
            [
                dcc.Dropdown(
                    id="ejex",
                    options=[{"label": i, "value": i} for i in df_pais.columns],
                    value="Renta per capita",
                )
            ],
            style={"width": "48%", "display": "inline-block"},
        ),
        html.Div(
            [
                dcc.Dropdown(
                    id="ejey",
                    options=[{"label": i, "value": i} for i in df_pais.columns],
                    value="Esperanza de vida",
                )
            ],
            style={"width": "48%", "display": "inline-block"},
        ),
        dcc.Graph(id="grafico"),
    ],
    style={"padding": 10},
)


# Aplicamos la logica de la app
@app.callback(
    Output("grafico", "figure"), [Input("ejex", "value"), Input("ejey", "value")]
)
def update_graph(ejex, ejey):
    return {
        "data": [
            go.Scatter(
                x=df_pais[ejex],
                y=df_pais[ejey],
                mode="markers",
                marker={
                    "size": 15,
                    "opacity": 0.5,
                    "line": {"width": 0.5, "color": "white"},
                },
            )
        ],
        
        "layout": go.Layout(
            title="Relacion entre {} y {}".format(ejex, ejey),
            xaxis=dict(title=ejex),
            yaxis=dict(title=ejey),
            hovermode="closest",
        ),
    }


if __name__ == "__main__":
    app.run_server(port=8000)
