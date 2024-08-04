# Definir Funções
# Nome seguido de _ e verbos

from flask import *  
from CSV import *
import csv


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
        capacidade = request.form['capacidade']
        tipo = request.form['tipo']
        descricao = request.form['descricao']

        # Bota no CSV
        with open(cad_sala, 'a', newline='') as salas_cadastros:
            escrever = csv.writer(salas_cadastros)
            escrever.writerow([capacidade, tipo, descricao])

def salvar_reserva():
    if request.method == 'POST':
       # Forms
        sala = request.form['sala']
        comeco = request.form['comeco']
        fim = request.form['fim']

        # Bota no CSV       
        with open(res_sala, 'a', newline='') as reservas_salas:
            escrever = csv.writer(reservas_salas)
            escrever.writerow([sala, comeco, fim])

        return {
            'sala' : sala,
            'comeco' : comeco,
            'fim' : fim
        }
    
# Exibição e leitura dos CSVs
def ler_csv():
    salas = []
    with open(cad_sala, 'r', newline='') as reservas_salas:
        leitor = csv.reader(reservas_salas)
        next(leitor)  # Pula o header 

        for idx, linha in enumerate(leitor, start=1):
            sala = {
                'id': idx,
                'capacidade': linha[0],
                'tipo': linha[1],
                'descricao': linha[2]
            }
            salas.append(sala)

    return salas