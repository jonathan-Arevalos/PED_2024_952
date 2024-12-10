from dash import dcc, html, Dash
from Welcome_main import menu_dash, run_dash


def menu_main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ejecutar Web Scraping")
        print("2. Limpieza de Datos")
        print("3. Ver Dashboard")
        print("4. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                print("Opción de Web Scraping seleccionada")
            elif opcion == 2:
                print("Opción de Limpieza de Datos seleccionada")
            elif opcion == 3:
                run_dash()
            elif opcion == 4:
                print("Hasta luego.")
                break
            else:
                print("Por favor, seleccione una opción válida.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

if __name__ == "_main_":
    menu_main()