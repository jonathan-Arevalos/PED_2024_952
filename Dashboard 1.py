import pandas as pd
import plotly.express as px
from click import style
from dash import dcc, html, callback, Input, Output
from sqlalchemy import create_engine


# Conexión a la base de datos
user = "root"
password = "12345678"
server = "localhost"
db = "adidas_scrapper"

# Cadena que se usara para realizar la conexión con pymysql
cadena_conexion = f"mysql+pymysql://{user}:{password}@{server}/{db}"

# Establecer conexión con engine
engine = create_engine(cadena_conexion)
conexion = engine.connect()

sql = "SELECT * FROM INFO"
data = pd.read_sql(sql, conexion)

conexion.close()

def histograma():
    fig=px.histogram(data,x="Precio",nbins=10,title="HISTOGRAMA DE PRECIOS",template="plotly_dark")
    fig.update_layout(xaxis_title="Precio",yaxis_title="Cantidad")

    fig_box=px.scratter(
        data,
        x="Precio",
        y="Cantidad",
        title="BOXPLOT DE PRECIOS",
        template="plotly_dark"
    )
    fig_box.update_layout(xaxis_title="Precio",yaxis_title="Cantidad")

    body = html.Div(
        [
            html.H3("HISTOGRAMA DE PRECIOS",style={"text-align":"center"}),
            html.P("EXPLORA EL HISTORIAL DE PRECIOS DE LOS TENIS",style={"text-align":"center"}),
            dcc.Graph(figure=fig),
            dcc.Dropdown(
                options=[
                    {
                        "label":"precio",
                    }
                ],
                value="Precio",
                style={"width":"100%"}
            ),
            html.Div(dcc.Graph(figure=fig_box))
        ],
        style={"background-color":"#2b2b2b"}
    )

    return body
