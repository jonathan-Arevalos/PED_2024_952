import time
from selenium.webdriver import Keys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
from mysql.connector import connect, Error
import os
import csv

def insertar_datos(dbconecxion, titulo, precio, categoria, colores_disponibles, tipo_envio):
    try:
        cursor = dbconecxion.cursor()
        sql = "INSERT INTO informacion (titulo, precio, categoria, Colores_disponibles, Tipo_envio) VALUES (%s, %s, %s, %s, %s)"
        cursor.execute(sql, (titulo, precio, categoria, colores_disponibles, tipo_envio))
        dbconecxion.commit()
        print("Datos insertados correctamente:", titulo)
    except Error as e:
        print(f"Error al insertar datos: {e}")

def guardar_en_csv(titulo, precio, categoria, colores_disponibles, tipo_envio):
    if not os.path.exists('Datasets'):
        os.makedirs('Datasets')
    ruta_csv = os.path.join('Datasets', 'productos_adidas.csv')
    with open('productos_adidas.csv', mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([titulo, precio, categoria, colores_disponibles, tipo_envio])

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

    ruta_csv = os.path.join('datasets', 'productos_adidas.csv')
    with open(ruta_csv, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(['Título', 'Precio', 'Categoría', 'Colores Disponibles', 'Tipo de Envío'])

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

            # Guardar los datos en el archivo CSV
            guardar_en_csv(titulo, precio, categoria, colores_disponibles, tipo_envio)

        # Navegar a la siguiente página
        try:
            btnSiguiente = navegador.find_element(By.XPATH, '//*[@id="__next"]/div[2]/main/nav/div[3]/a')
            btnSiguiente.send_keys(Keys.ENTER)
        except Exception as e:
            print("No hay más páginas.")
            break

    navegador.quit()

if __name__ == "__main__":
    try:
        # Conexión a la base de datos
        dbconecxion = connect(host="localhost", user="root", password="12345678", database="adidas_scrapper")
        print("Conexión establecida con la base de datos.")

        # Ejecutar el scraper
        busqueda = "tenis"
        paginas = 1
        adidas(busqueda, paginas, dbconecxion)

    except Error as e:
        print(f"Error al conectar con la base de datos: {e}")