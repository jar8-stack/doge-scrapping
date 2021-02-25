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


while True:
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

    print(valorNumericoUnitario)


    time.sleep(1800)
