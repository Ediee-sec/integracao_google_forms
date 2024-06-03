import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials
import gspread

# Autenticação e autorização com o Google Sheets
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('/home/ubuntu/codes/python/integracao_google_forms/documents/gcp_emerson.json', scope)
client = gspread.authorize(credentials)
spreadsheet = client.open_by_key('1N0PA01G3TPukjXbEop_hCejO3LazJgyWxOsglJtULMg')
sheet = spreadsheet.sheet1

# Obter valores das colunas 'NOME' e 'DKP ATUAL'
nomes = sheet.col_values(1)  # Coluna 'NOME' é a primeira coluna (coluna 1)
dkp_atual = sheet.col_values(2)  # Coluna 'DKP ATUAL' é a segunda coluna (coluna 2)

# Remover o cabeçalho (primeiro elemento) de cada lista
nomes.pop(0)
dkp_atual.pop(0)

# Criar DataFrame
data = {'NOME': nomes, 'DKP ATUAL': dkp_atual}
df = pd.DataFrame(data)

# Exibir DataFrame
print(df)
