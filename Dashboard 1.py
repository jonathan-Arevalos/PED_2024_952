import pandas as pd
import plotly.express as px

#Conexion a la base de datos
user="root"
password="12345678"
server="localhost"
db="adidas_scrapper"

#Cadena que se usara para realizar la conexion
cadena_conexion = f"mysql+mysqlconnector://{user}:{password}@{server}/{db}"

#Establecer


sql="SELECT * FROM ()"
data=pd.read_sql(sql,)