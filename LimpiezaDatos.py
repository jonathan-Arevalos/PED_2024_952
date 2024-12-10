import pandas as pd

def limpiar_datos():
    # Cargar los datos desde un archivo CSV
    df = pd.read_csv("Datasets/productos_adidas.csv")

    #Ver los datos iniciales
    print("Datos iniciales:")
    print(df.head())
    print("\nInformación del DataFrame:")
    print(df.info())


    # Eliminar duplicados
    df.drop_duplicates(inplace=True)


    # Rellenar valores nulos en columna "tipo_envio" con "Sin información"
    df["tipo_envio"].fillna("Sin información", inplace=True)
    # Rellenar valores nulos en columna "colores_disponibles" con "Solo un color disponible"
    df["colores_disponibles"].fillna("Solo un color disponible", inplace=True)
    # Rellenar valores nulos en "precio" con 0
    df["precio"].fillna(0, inplace=True)

    # Convertir "precio" a tipo numérico (por si hay problemas con el formato)
    df["precio"] = pd.to_numeric(df["precio"], errors="coerce").fillna(0)

    # Formatear la columna "titulo" (Eliminar espacios extra)
    df["titulo"] = df["titulo"].str.strip()

    # Revisar si quedaron valores nulos
    print("\nValores nulos después de la limpieza:")
    print(df.isnull().sum())

    # Verificar los cambios
    print("\nDatos después de la limpieza:")
    print(df.head())

    # Guardar los datos limpios en un nuevo archivo
    df.to_csv("datos_limpios_Adidas.csv", index=False)
    print("Datos limpios guardados en 'datos_limpios_Adidas.csv'.")

if __name__ == "__main__":
    limpiar_datos()
