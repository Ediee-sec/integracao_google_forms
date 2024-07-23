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

    return json_data

def dataframe():

    df = json_normalize(get_user())

    df = df.rename(columns={
        'Carimbo de data/hora': 'dt_cadastro',
        'Endereço de e-mail': 'email',
        'Nome de usuário Discord': 'usr_dc',
        'Nome exibido no Discord': 'nome_exibido_dc',
        'Qual sua classe principal': 'classe_principal',
        'Qual sua classe secundária': 'classe_secundaria',
        'Informe o período que você tem mais disponibilidade para comparecer no jogo de segunda-feira à sexta-feira': 'disponibilidade_seg_sex',
        'Informe o período que você tem mais disponibilidade para comparecer no jogo final de semana (Sábado e Domingo)': 'disponibilidade_sab_dom',
        'Experiência no jogo': 'xp_jogo',
        'Pretende investir quantos R$ no jogo?': 'pretencao_investimento',
        'Pretende adquirir algum dos pacotes de pré-venda?': 'pretencao_pacotes',
        'Já é membro da guild': 'membro_guild',
        'Nickname que você costuma usar in-game': 'nickname',
        'Jogou em outra guild no KR - ClosedBeta - OpenBeta? Descreva:':'jogou_outra_guild',
        'Você tem algum amigo na guild? Diga o nick:': 'amigo_guild'
    })  

    return df

def insert_db():
    exec = database.ConnPostgres()
    exec.insert_data(dataframe())

def mail(email,nickname,classe):
    
    exec = envia_email.SendEmail(email,nickname,classe)
    exec.send_email()

        





