import sqlite3
import csv
from banco.sql import execute_sql



conn = sqlite3.Connection("livraria.db")
cursor = conn.cursor()
nome_tabela = "livros"
dados_create = ["id INTEGER PRIMARY KEY", "titulo TEXT", "autor Text", "ano integer", "preco real"]
nome_arquivo = "livros.csv"

def import_csv(cursor, nome_tabela, nome_arquivo):
    with open(nome_arquivo, newline='', encoding='utf-8') as csvFile:
        leitor = csv.reader(csvFile)
        next(leitor)  # Pular o cabeçalho
        for linha in leitor:
            cursor.execute(f"INSERT INTO {nome_tabela} (titulo, autor, ano, preco) VALUES (?, ?, ?, ?)",
                           (linha[0], linha[1], int(linha[2]), float(linha[3])))
    conn.commit()
    
execute_sql.create_sql(cursor, nome_tabela, dados_create)

import_csv(cursor, nome_tabela, nome_arquivo)


conn.close()