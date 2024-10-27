# Definir Funções
# Nome seguido de _ e verbos

from flask import request, render_template, Flask
from CSV import *
import csv
import mysql.connector

def conexao_abrir(host, usuario, senha, banco):
    return mysql.connector.connect(host=host, user=usuario, password=senha, database=banco)

cad_usuarios = 'CSV/cadastro-usuario.csv'
cad_sala = 'CSV/cadastro-sala.csv'
res_sala = 'CSV/reserva-sala.csv'

def salvar_cadastro():
    if request.method == 'POST':
        # Forms
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        # Bota no CSV
        with open(cad_usuarios, 'a', newline='') as usuarios_cadastros:
            escrever = csv.writer(usuarios_cadastros)
            escrever.writerow([nome, email, senha])
        return render_template('reservas.html')

# Mesma coisas para os próximos
def salvar_sala():
    if request.method == 'POST':
        # Forms
        tipo = request.form['tipo']
        capacidade = request.form['capacidade']
        descricao = request.form['descricao']

        # Bota no CSV
        with open(cad_sala, 'a', newline='') as salas_cadastros:
            escrever = csv.writer(salas_cadastros)
            escrever.writerow([tipo, capacidade, descricao])

def salvar_reserva(sala, comeco, fim):
       # Forms
    sala = request.form['sala']
    comeco = request.form['comeco']
    fim = request.form['fim']

    # Bota no CSV       
    with open(res_sala, 'a', newline='') as reservas_salas:
        escrever = csv.writer(reservas_salas)
        escrever.writerow([sala, comeco, fim])
        reserva = {
                    'sala' : sala,
                    'comeco' : comeco,
                    'fim' : fim
                }
    return reserva
    
# Exibição e leitura dos CSVs
def ler_csv():
    salas = []
    with open(cad_sala, 'r', newline='') as reservas_salas:
        leitor = csv.reader(reservas_salas)
        next(leitor)  # Pula o header 

        for idx, linha in enumerate(leitor, start=1):
            sala = {
                'id': idx,
                'tipo': linha[0],
                'capacidade': linha[1],
                'descricao': linha[2]
            }
            salas.append(sala)

    return salas

# insere no MySql (estan me matando)
def usuarioInserir(con, usuario, senha, nome, email):
     cursor = con.cursor()
     sql = "INSERT INTO cliente (usuario, senha, nome, email) VALUES ('%s', '%s', '%s', '%s')"
     cursor.execute(sql, (usuario, senha, nome, email))
     con.commit() 
     cursor.close()
        
