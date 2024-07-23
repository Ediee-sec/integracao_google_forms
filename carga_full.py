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

    spreadsheet = client.open_by_key('1PnPvkdJLbKN1BuobNpqWo8OwSYo0YEYuSQaXupi2jqw')

    sheet = spreadsheet.sheet1

    data = sheet.get_all_records()

    return data


def dataframe():

    df = pd.DataFrame(get_user())
    df = df.drop(['Status_SAW_emersonrox8@gmail.com (3ptzun) WEBHOOK'], axis=1)
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
    exec.query_truncate_table()
    exec.insert_data(dataframe())

insert_db()
        





