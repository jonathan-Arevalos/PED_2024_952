import pandas as pd
import plotly.express as px
from dash import dcc, html, callback, Input, Output
from sqlalchemy import create_engine

# Conexión a la base de datos
user = "root"
password = "12345678"
server = "localhost"
db = "adidas_scrapper"  # Reemplaza con el nombre de tu base de datos

cadena_conexion = f"mysql+pymysql://{user}:{password}@{server}/{db}"
engine = create_engine(cadena_conexion)
conexion = engine.connect()

# Consulta SQL para seleccionar Categoria y Precio
sql = "SELECT Categoria, Precio FROM informacion"
data = pd.read_sql(sql, conexion)

conexion.close()

def histograma():
    # Gráfico de barras de Precio por Categoria
    fig = px.bar(data, x="Categoria", y="Precio", title="Precio por Categoría", template="plotly_dark")
    fig.update_layout(xaxis_title="Categoría", yaxis_title="Precio")

    body = html.Div(
        [
            html.H3("Gráfico de Precios por Categoría", style={"text-align": "center"}),
            dcc.Graph(figure=fig),
            # ... otros elementos del dashboard ...
        ],
        style={"background-color": "#2b2b2b"}
    )

    return body