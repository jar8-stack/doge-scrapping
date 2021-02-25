__version__ = "1.0"

"""
El módulo *comprobarConexion* permite comprobar la conexión a internet.
"""

# Versión Python: 3.5.2

from ctypes import windll, byref
from ctypes.wintypes import DWORD
from socket import gethostbyname, create_connection, error


from bs4 import BeautifulSoup
import requests
import pandas as pd
import smtplib
import time


url= 'https://doge.es.currencyrate.today/mxn'
sender_email= "bioshock450226@gmail.com"
rec_email= "saidserrano315@gmail.com"
password= "Serranosoto1"
message= "El doge ya alcanzo su limite puto, vende"


# =================== FUNCIÓN comprobarConexion ====================

def comprobarConexion():
    flags = DWORD()
    conexion = windll.wininet.InternetGetConnectedState(byref(flags), None)

    if conexion:
        return "Hay conexión a internet..."
    else:
        return "No hay conexión a internet..."


# ================= FUNCIÓN comprobarConexionUno ===================

def comprobarConexionUno():
    try:
        gethostbyname("google.com")
        conexion = create_connection(("google.com", 80), 1)
        conexion.close()
        return "Hay conexión a internet..."
    except error:
        return "No hay conexión a internet..."






while True:


    conexion = comprobarConexion()
    conexionUno = comprobarConexionUno()


    if conexion=="Hay conexión a internet..." and conexionUno=="Hay conexión a internet...":
        print("si estas conectado")
        page= requests.get(url)

        soup= BeautifulSoup(page.content, 'html.parser')

        #Valor del doge a pesos

        value= soup.find_all('span', class_='cc-result')


        valores= list()

        for i in value:
            valores.append(i.text)


        valorUnitario= valores[1]

        valorNumericoUnitario= valorUnitario[0]+valorUnitario[1]+valorUnitario[2]+valorUnitario[3]

        if(float(valorNumericoUnitario) >= 15):
            server= smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            print("Login succes")
            server.sendmail(sender_email, rec_email, message)
            print("Avisado estas", rec_email)
            exit()




        time.sleep(1800)
    else:
        print("Esperando conexion")
