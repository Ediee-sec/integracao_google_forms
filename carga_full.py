import database
import envia_email
import pandas as pd
from pandas import json_normalize
from oauth2client.service_account import ServiceAccountCredentials
import json
import gspread


def get_user():

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/ubuntu/codes/python/integracao_google_forms/documents/gcp_emerson.json', scope)

    client = gspread.authorize(credentials)

    spreadsheet = client.open_by_key('1fkhqBR4zOJMNJrVYTBJRx2mAD9RRPkAnUA7d2dhGB-Q')

    sheet = spreadsheet.sheet1

    data = sheet.get_all_records()

    return data


def dataframe():

    df = pd.DataFrame(get_user())

    df = df.rename(columns={
        'Carimbo de data/hora': 'data_cadastro',
        'Endereço de e-mail': 'email',
        'Nome de usuário discord': 'discord',
        'Nickname': 'nickname',
        'Conjunto de armas': 'armas',
        'Função': 'funcao',
        'Experiência no jogo': 'experiencia',
        'Seu estilo de jogo': 'estilo',
        'Já é membro da guild': 'membro'
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

insert_db()
        





