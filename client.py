import pandas as pd
import numpy as np
import json

xls = pd.ExcelFile('Clientes.xlsx')

df = xls.parse('Carga de clientes', skiprows=6, index_col=None, na_values=['NA'])

df = df.fillna("")

df = df.rename(
    columns={'Unnamed: 0': '#', 
             'Unnamed: 1': 'Tipo', 
             'Unnamed: 2': 'CNPJ/CPF',
             'Unnamed: 3': 'Razão social / Nome',
             'Unnamed: 4': 'Nome fantasia',
             'Unnamed: 5': 'Inscrição estadual',
             'Unnamed: 6': 'Inscrição municipal',
             'Unnamed: 7': 'Código do cliente',
             'Unnamed: 8': 'É cliente final?',
             'Unnamed: 9': 'CEP',
             'Unnamed: 10': 'Endereço',
             'Unnamed: 11': 'Número',
             'Unnamed: 12': 'Complemento',
             'Unnamed: 13': 'Bairro',
             'Unnamed: 14': 'Cidade',
             'Unnamed: 15': 'Estado',
             'Unnamed: 17': 'Contato',
             'Unnamed: 24': 'Anotações',
             'Unnamed: 25': 'Limite de crédito',
             'Unnamed: 26': 'Bloquear venda para o cliente?'
            })


df = df.dropna(how='all', axis=1)

df = df.drop(columns=['Inscrição municipal', 'Contato', 'Tipo', 'Tipo.1', 'Contato.1', 'Tipo.2', 'Contato.2', 'Tipo.3', 'Contato.3', 'Anotações'])

df = pd.DataFrame(df)

df

for row in df.iterrows():
    data = {
        "Status": "1",
        "Resale": False,
        "Notes": "",
        "PriceTableId": "",
        "CustomerCode": "2",
        "CreditLimit": "0",
        "BlockSale": False,
        "Tags": [],
        "Person": {
            "Type": "2",
            "RegistrationCode": "000000000000000000",
            "CompanyName": "BLA BLA LGPD",
            "SocialName": "BLA BLA LGPD",
            "RegistrationState": "000.000.000.000",
            "RegistrationCity": "",
            "Taxpayer": "",
            "Taxing": "",
            "BusinessSituation": "",
            "PaymentMethodId": None,
            "PreferredSalesPersonId": "",
            "FinalCostumer": False,
            "RegistrationStateRequired": False
        },
    }
    #print(row[1]['CNPJ/CPF'])
    #print(row[1]['CNPJ/CPF'])


import requests
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


TOKEN =''
hed = {'Authorization': 'Bearer ' + TOKEN}
api = 'https://localhost:5001/client'
dt = {'JSON CLIENT'}
response = requests.post(api, json=dt, headers=hed, verify=False)
print(response.status_code)
print(response.json())

contador = 0
for row in df.iterrows():
    contador = contador + 1
    TOKEN ='TOKEN'
    hed = {'Authorization': 'Bearer ' + TOKEN}
    api = 'https://localhost:5001/client/'
    response = requests.get(api, headers=hed, verify=False)
    if response.status_code == 200:
        print('Salvo com sucesso ' + row[1]['CNPJ/CPF'] + ' ' + row[1]['Razão social / Nome'])
    else:
        print(response.json()['errorMessages'] + row[1]['CNPJ/CPF'] + ' ' + row[1]['Razão social / Nome'])
        print(response.json())
    print(contador)
