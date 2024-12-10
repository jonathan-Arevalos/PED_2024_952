import pandas as pd
import plotly.express as px
from dash import dcc, html, callback, Input, Output
from sqlalchemy import create_engine

# Conexión a la base de datos
user = "root"
password = "12345678"
server = "localhost"
db = "adidas_scrapper"

cadena_conexion = f"mysql+pymysql://{user}:{password}@{server}/{db}"
engine = create_engine(cadena_conexion)
conexion = engine.connect()

# Consulta SQL para seleccionar Categoria y Precio
sql = "SELECT Categoria, Colores_disponibles FROM informacion"  # Consulta modificada
data = pd.read_sql(sql, conexion)

conexion.close()

def histograma():

    # Gráfico de barras para la cantidad de productos por categoría
    fig_barras = px.bar(
        data,
        x="Categoria",  # Usar columna "Categoria"
        color="Colores_disponibles",  # Colorear por "Colores_disponibles"
        title="CANTIDAD DE PRODUCTOS POR CATEGORIA Y COLOR",
        template="plotly_dark"
    )
    fig_barras.update_layout(xaxis_title="Categoria", yaxis_title="Cantidad")

    body = html.Div(
        [
            html.H3("CANTIDAD DE PRODUCTOS POR CATEGORIA Y COLOR", style={"text-align": "center"}),
            html.Div(dcc.Graph(figure=fig_barras))
        ],
        style={"background-color": "#2b2b2b"}
    )

    return body