import gspread
from oauth2client.service_account import ServiceAccountCredentials


# use creds para criar um cliente para interagir com a API do Google Drive
scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Encontre uma pasta de trabalho pelo nome e abra a primeira planilha
# Certifique-se de usar o nome correto aqui.
sheet = client.open("Teste python").sheet1

# Extraia e imprima todos os valores
list_of_hashes = sheet.get_all_records()
print(list_of_hashes)