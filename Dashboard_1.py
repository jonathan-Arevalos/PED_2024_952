import pandas as pd
import plotly.express as px
from dash import dcc, html, callback, Input, Output
from sqlalchemy import create_engine

# Conexión a la base de datos
user = "root"
password = "12345678"
server = "localhost"
db = "adidas_scrapper"  # Reemplaza con el nombre de tu base de datos

# Cadena de conexión
cadena_conexion = f"mysql+pymysql://{user}:{password}@{server}/{db}"
engine = create_engine(cadena_conexion)
conexion = engine.connect()

# Consulta SQL para seleccionar Tipo_envio, Categoria y Precio
sql = "SELECT Tipo_envio, Categoria, Precio FROM informacion"  # Asegúrate de que el nombre de la tabla sea correcto
data = pd.read_sql(sql, conexion)

conexion.close()

def histograma():
    # Gráfico de barras para la cantidad de productos por tipo de envío
    fig_barras = px.bar(
        data,
        x="Tipo_envio",
        color="Categoria",  # Agrupa por categoría
        title="CANTIDAD DE PRODUCTOS POR TIPO DE ENVÍO Y CATEGORÍA",
        template="plotly_dark"
    )
    fig_barras.update_layout(xaxis_title="Tipo de Envío", yaxis_title="Cantidad")

    # Gráfico de dispersión para Precio vs. Categoría, agrupado por Tipo_envio
    fig_scatter = px.scatter(
        data,
        x="Categoria",
        y="Precio",
        color="Tipo_envio",  # Agrupa por tipo de envío
        title="PRECIO VS. CATEGORÍA POR TIPO DE ENVÍO",
        template="plotly_dark"
    )
    fig_scatter.update_layout(xaxis_title="Categoría", yaxis_title="Precio")

    body = html.Div(
        [
            html.H3("CANTIDAD DE PRODUCTOS POR TIPO DE ENVÍO Y CATEGORÍA", style={"text-align": "center"}),
            dcc.Graph(figure=fig_barras),
            html.H3("PRECIO VS. CATEGORÍA POR TIPO DE ENVÍO", style={"text-align": "center"}),
            dcc.Graph(figure=fig_scatter)
        ],
        style={"background-color": "#2b2b2b"}
    )

    return body