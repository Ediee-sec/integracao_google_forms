import database
import envia_email
import pandas as pd
from pandas import json_normalize
from oauth2client.service_account import ServiceAccountCredentials
import json


# def get_user():

#     scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

#     credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/ubuntu/codes/python/integracao_google_forms/documents/gcp_emerson.json', scope)

#     client = gspread.authorize(credentials)

#     spreadsheet = client.open_by_key('128cwrG4M8vl3_mGcVbIm8MDR4thqXcmlNJ310aOQyW8')

#     sheet = spreadsheet.sheet1

#     data = sheet.get_all_records()

#     return data

def get_user():
    with open('json/dados_recebidos.json', 'r') as file:
        json_data = json.load(file)

    info = json_data.get("rowData")

    return info

def dataframe():

    df = json_normalize(get_user())

    df = df.rename(columns={
        'coluna_1': 'data_cadastro',
        'coluna_2': 'email',
        'coluna_3': 'discord',
        'coluna_4': 'nickname',
        'coluna_5': 'armas',
        'coluna_6': 'funcao',
        'coluna_7': 'experiencia',
        'coluna_8': 'estilo',
        'coluna_9': 'membro'
    })

    df['recebeu_email'] = 'Sim'
    return df

def insert_db():
    exec = database.ConnPostgres()
    exec.insert_data(dataframe())

def mail():
    query = database.ConnPostgres()
    resultado = query.query_email()

    for index, row in resultado.iterrows():
        email = row['email']
        nickname = row['nickname']

        exec = envia_email.SendEmail(email,nickname)
        exec.send_email()

        





