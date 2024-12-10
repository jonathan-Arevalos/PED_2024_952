
from dash import dcc, html, Dash, callback, Output, Input
import Dashboard_1 as d1
import Dashboard_2 as d2  # Importa Dashboard_2
from Welcome_main import menu_dash



app = Dash(__name__)

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

@callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/dashboard1':
        return d1.histograma()
    elif pathname == '/dashboard2':
        return d2.histograma()  # Llama a la función de Dashboard_2
    else:
        return menu_dash()  # Muestra el menú principal por defecto

if __name__ == '__main__':
    app.run_server(debug=True)



""" 
            elif opcion == 3:
                print("Mostrando el dashboard...")
                app = Dash(__name__)
                app.layout = html.Div([
                    d1.histograma()  # Llama a la función para generar el dashboard
                ])
                app.run_server(debug=True)
"""