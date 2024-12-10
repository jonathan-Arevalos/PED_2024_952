import pandas as pd
import plotly.express as px
from dash import dcc, html, Dash, callback, Input, Output

from dash import html

def welcome():
    body = html.Div(
        [
            html.Div(
                [
                    html.H1("BIENVENIDO A LA PAGINA DE EXTRACCION DE DATOS", style={"text-align": "center"}),
                    html.P("PROYECTO FINAL: ADIDAS 952", style={"text-align": "center"}),

                    html.Img(
                        src="https://clipart-library.com/img1/753924.jpg",
                        style={"display": "block", "margin": "20px auto", "width": "300px", "height": "auto"},
                        title="Adidas"
                    ),

                    html.P(
                        "OBJETIVO: IMPULSAR LA TOMA DE DECISIONES MOSTRANDO DATOS RELEVANTES COMO PRECIO,COLOR,CATEGORIA,ETC",
                        style={"textAlign": "justify", "fontSize": "16px", "lineHeight": "1.6"},
                    ),
                    html.H2("REQUERIMIENTOS", style={"text-align": "center"}),
                    html.Ul(
                        [
                            html.Li("1 - COMO ES LA DISTRIBUCIOND DE LOS PRECIOS?"),
                            html.Li("2 - PUEDE EL TIPO DE ENVIO INFLUIR EN EL PRECIO?"),
                            html.Li("3 - COMO IDENTIFICAR DISTRIBUCION DE LA CANTIDAD DE COLORES EN LOS TENIS?")
                        ],
                        style={"lineHeight": "1.8", "paddingLeft": "20px", "fontSize": "15px"},
                    ),
                ],
                style={"backgroundColor": "#FFFFFF", "border": "1px solid #DDDDDD", "padding": "20px", "borderRadius": "5px"},
            ),
            html.Hr(style={"margin": "30px 0"}),
        ]
    )

    return body