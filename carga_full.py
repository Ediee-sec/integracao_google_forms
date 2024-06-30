import database
import envia_email
import pandas as pd
from pandas import json_normalize
from oauth2client.service_account import ServiceAccountCredentials
import json
import gspread


def get_user():

    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']

    credentials = ServiceAccountCredentials.from_json_keyfile_name('documents/gcp_emerson.json', scope)

    client = gspread.authorize(credentials)

    spreadsheet = client.open_by_key('1jmneG6ShPbcnElbK-FQ3taFlih_4iaHfVw2VoRz4E7g')

    sheet = spreadsheet.sheet1

    data = sheet.get_all_records()

    return data


def dataframe():

    df = pd.DataFrame(get_user())
    df = df.drop(['Status_SAW_emersonrox8@gmail.com (2olmqk) WEBHOOK'], axis=1)
    df = df.rename(columns={
        'Carimbo de data/hora': 'dt_cadastro',
        'Endereço de e-mail': 'email',
        'Nome de usuário discord': 'usr_discord',
        'Nickname': 'nickname',
        'Conjunto de armas': 'armas',
        'Função': 'funcao',
        'Experiência no jogo': 'xp_jogo',
        'Seu estilo de jogo': 'estilo',
        'Já é membro da guild': 'membro_guild'
    })

    return df

def insert_db():
    exec = database.ConnPostgres()
    exec.insert_data(dataframe())

insert_db()
        





