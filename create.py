import gspread
from oauth2client.service_account import ServiceAccountCredentials
from random import sample


def credentials():
    # use creds para criar um cliente para interagir com a API do Google Drive
    scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
    creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
    client = gspread.authorize(creds)
    return client


def find_sheets():
    # Encontre uma pasta de trabalho pelo nome e abra a primeira planilha
    # Certifique-se de usar o nome correto aqui.
    sheet = credentials().open("Teste python").sheet1
    return sheet


def create_list_of_random_numbers():
    # Gera 10 listas de 50 números aleatórios no intervalo de 0 a 100
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    fixas = len(lista)
    generate_sample_numbers(lista, fixas)
    # print(lista)
    # print('lista_numeros: ', sorted(lista))
    # find_sheets().insert_row(sorted(lista), 1)


def generate_sample_numbers(lista, fixas):
    random_numbers = []
    for i in range(30):
        if i != [item for item in lista]:
            random_numbers.append(sample(range(1, 26), 15 - fixas))
    print('random_numbers: ', random_numbers)
    return random_numbers

def delete_operation():
    delete_columns = find_sheets().delete_columns(1, end_index=7)
    return delete_columns


if __name__ == '__main__':
    create_list_of_random_numbers()
