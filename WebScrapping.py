#Aporte de Jonathan Arevalos

import time
from typing import final
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from mysql.connector import connect, Error

def insertar_datos(dbconecxion, titulo, precio, categoria, colores_disponibles, tipo_envio):
    try:
        cursor = dbconecxion.cursor()
        sql = "INSERT INTO informacion (titulo, precio, categoria, Colores_disponibles, Tipo_envio) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (titulo, precio, categoria, colores_disponibles, tipo_envio))
        dbconecxion.commit()
        print("Datos insertados correctamente:", titulo)
    except Error as e:
        print(f"Error al insertar datos: {e}")

def adidas(busqueda, paginas, dbconecxion):
    s = Service(ChromeDriverManager().install())
    opc = Options()
    opc.add_argument("--window-size=1020,1200")
    navegador = webdriver.Chrome(service=s, options=opc)
    navegador.get("https://www.adidas.mx/")
    time.sleep(5)

    # Aceptar cookies
    txtInicio = navegador.find_element(By.XPATH, "//*[@id='glass-gdpr-default-consent-accept-button']")
    time.sleep(2)
    txtInicio.click()

    # Buscar el producto
    txtBuscar = navegador.find_element(By.CLASS_NAME, "_input_1f3oz_13")
    txtBuscar.click()
    txtBuscar.send_keys(busqueda)
    time.sleep(2)
    txtBuscar.send_keys(Keys.ENTER)
    time.sleep(5)

    for pag in range(paginas):
        time.sleep(3)
        soup = BeautifulSoup(navegador.page_source, "html5lib")
        productos = soup.find_all("div", attrs={"class": "product-card_product-card-content___bjeq"})

        for item in productos:
            titulo = item.find("p", attrs={"class": "product-card-description_name__xHvJ2"}).text.strip()
            precio = item.find("div", attrs={"data-testid": "primary-price"})
            categoria = item.find("p", attrs={"class": "product-card-description_info__z_CcT"})
            colores_disponibles = item.find("p", attrs={"data-testid": "product-card-colours", "class": "product-card-description_info__z_CcT"})
            tipo_envio = item.find("p", attrs={"data-testid": "product-card-badge", "class": "product-card-description_badge__m75SV"})

            # Manejo de datos nulos
            precio = precio.text.strip().replace("$", "").replace(",", "") if precio else "0.00"
            categoria = categoria.text.strip() if categoria else "Sin categoría"
            colores_disponibles = colores_disponibles.text.strip() if colores_disponibles else "Solo un color disponible"
            tipo_envio = tipo_envio.text.strip() if tipo_envio else "No envíos"

            # Insertar los datos en la base de datos
            insertar_datos(dbconecxion, titulo, precio, categoria, colores_disponibles, tipo_envio)

        # Navegar a la siguiente página
        try:
            btnSiguiente = navegador.find_element(By.XPATH, '//*[@id="__next"]/div[2]/main/nav/div[3]/a')
            btnSiguiente.send_keys(Keys.ENTER)
        except Exception as e:
            print("No hay más páginas.")
            break

    navegador.quit()


#Main para la llamada y conexion en la bd
#Try except

if __name__ == "__main__":
    try:
        #conexion de la base de datos
        dbconecxion = connect(host="localhost", user="root", password="12345678", database="adidas_scrapper")
        print("Conexion exitosa a la base de datos")

        #ejecucion scrapping
        busqueda="tenis"
        paginas=8
        adidas(busqueda, paginas, dbconecxion)

    except Error as e:
        print(f"Error al conectar a la base de datos: {e}")
    """finally:
        if dbconecxion.is_connected():
            dbconecxion.close()
            print("Conexion cerrada")"""
