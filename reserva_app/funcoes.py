# Definir Funções
# Nome seguido de _ e verbos

from flask import request  
import csv, CSV


cad_usuarios = 'CSV/cadastro-usuario.csv'

def salvar_cadastro():
    if request.method == 'POST':
        # Requisições dos Formulários
        nome = request.form['nome']
        email = request.form['email']
        senha = request.form['senha']

        # Registra no CSV
        with open(cad_usuarios, 'a', newline='') as usuarios_cadastros:
            escrever = csv.writer(usuarios_cadastros)
            escrever.writerow([nome, email, senha])