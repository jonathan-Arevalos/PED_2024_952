from dash import dcc, html, Dash

# Función para crear el menú con estilos mejorados
def menu_dash():
    body = html.Div([
        html.H1("Menú Principal", style={
            "text-align": "center",
            "color": "#F1C40F",
            "margin-top": "20px",
            "font-family": "'Lucida Console', Monaco, monospace",
            "text-shadow": "2px 2px 5px #000000"
        }),
        html.Hr(style={
            "border": "2px solid #F1C40F",
            "width": "80%",
            "margin": "auto",
            "margin-bottom": "20px"
        }),
        html.Div([
            html.Ul([
                html.Li(dcc.Link("1. Ver Dashboard 1", href="/dashboard1", style={
                    "text-decoration": "none",
                    "color": "#FFFFFF",
                    "font-weight": "bold",
                }),
                style={
                    "background-color": "#E74C3C",
                    "padding": "15px",
                    "margin-bottom": "15px",
                    "border-radius": "10px",
                    "text-align": "center",
                    "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.3)"
                }),
                html.Li(dcc.Link("2. Ver Dashboard 2", href="/dashboard2", style={
                    "text-decoration": "none",
                    "color": "#FFFFFF",
                    "font-weight": "bold",
                }),
                style={
                    "background-color": "#1ABC9C",
                    "padding": "15px",
                    "margin-bottom": "15px",
                    "border-radius": "10px",
                    "text-align": "center",
                    "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.3)"
                }),
                html.Li(dcc.Link("3. Ver Dashboard 3", href="/dashboard3", style={
                    "text-decoration": "none",
                    "color": "#FFFFFF",
                    "font-weight": "bold",
                }),
                style={
                    "background-color": "#3498DB",
                    "padding": "15px",
                    "margin-bottom": "15px",
                    "border-radius": "10px",
                    "text-align": "center",
                    "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.3)"
                }),
                html.Li(dcc.Link("4. Salir", href="/salir", style={
                    "text-decoration": "none",
                    "color": "#FFFFFF",
                    "font-weight": "bold",
                }),
                style={
                    "background-color": "#9B59B6",
                    "padding": "15px",
                    "margin-bottom": "15px",
                    "border-radius": "10px",
                    "text-align": "center",
                    "box-shadow": "0px 4px 6px rgba(0, 0, 0, 0.3)"
                })
            ], style={
                "list-style-type": "none",
                "padding": "0",
                "width": "60%",
                "margin": "auto"
            })
        ]),
        html.Footer("© 2024 Adidas.", style={
            "text-align": "center",
            "margin-top": "40px",
            "font-size": "14px",
            "color": "#BDC3C7",
            "font-family": "'Courier New', Courier, monospace"
        })
    ], style={
        "background-color": "#2C3E50",
        "padding": "30px",
        "height": "100vh",
        "box-sizing": "border-box"
    })
    return body
def run_dash():
    app = Dash(__name__)
    app.layout = menu_dash()
    app.run(debug=True,use_reloader=False)
if __name__ == "_main_":
    run_dash()