from PF_PPLEDD_MEJORADO import adidas
from mysql.connector import connect, Error
from LimpiezaDatos import  limpiar_datos


def menu_main():
    while True:
        print("\n--- Menú Principal ---")
        print("1. Ejecutar Web Scraping")
        print("2. Limpieza de Datos")
        print("3. Salir")

        try:
            opcion = int(input("Seleccione una opción: "))
            if opcion == 1:
                print("Opción de Web Scraping seleccionada")
                busqueda = input("Ingrese el término de búsqueda: ")
                paginas = int(input("Ingrese el número de páginas: "))
                try:
                    dbconecxion = connect(host="localhost", user="root", password="12345678",
                                          database="adidas_scrapper")
                    print("Conexión establecida con la base de datos.")
                    adidas(busqueda, paginas, dbconecxion)

                except Error as e:
                    print(f"Error al conectar con la base de datos: {e}")
            elif opcion == 2:
                print("Comenzando Limpieza de Datos")
                limpiar_datos()
            elif opcion == 3:
                print("Hasta luego.")
                break
            else:
                print("Por favor, seleccione una opción válida.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número.")

if __name__ == "__main__":
    menu_main()