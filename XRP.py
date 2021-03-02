import urllib
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests

import smtplib
import time


url= 'https://www.coingecko.com/es/monedas/xrp/mxn'
sender_email= "bioshock450226@gmail.com"
rec_email= "saidserrano315@gmail.com"
password= "Serranosoto1"
message= "Vende el XPR ya esta al doble"




def comprobarConexion():
    """
    Query internet using python
    :return:
    """
    try:
        urlopen('https://www.google.com', timeout=1)
        return True
    except urllib.error.URLError as Error:
        print(Error)
        return False



while True:


    conexion = comprobarConexion()



    if conexion==True:
        print("si estas conectado")
        page= requests.get(url)

        soup= BeautifulSoup(page.content, 'html.parser')

        #Valor del doge a pesos

        value= soup.find_all('span', class_='no-wrap')

        #print(value[0].text)

        valores= list()

        valorAnalizar=str(value[0].text)

        for i in valorAnalizar:
            valores.append(i)

        valorUnitarioNumerico= valores[3]+'.'+valores[5]+valores[6]

        valorUnitarioNumericoCompara= float(valorUnitarioNumerico)

        if(valorUnitarioNumericoCompara >= 17.8):
            server= smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            print("Login succes")
            server.sendmail(sender_email, rec_email, message)
            print("Avisado estas", rec_email)
            exit()



        print(valorUnitarioNumerico)


        time.sleep(1800)







    else:
        print("Esperando conexion")
