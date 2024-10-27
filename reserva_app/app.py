from flask import *
from CSV import *
from reserva_app.funcoes import *
import mysql.connector

abrirConexao = conexao_abrir("127.0.0.1","Mateus","m@tEuS.17","reservas")

app = Flask (__name__)

# Definição de Rotas
# Nome seguido de - // igual o arquivo.html

# login
@app.route('/')
def login_pag():
    return render_template('login.html') 

# Cadastros de usuario
@app.route('/cadastro')
def cadastro_pag():
    return render_template('cadastro.html')

# Reservar sala
@app.route('/reservar-sala')
def reservar_sala_pag():
    return render_template ('reservar-sala.html', salas=ler_csv())

# Reservas
@app.route('/reservas')
def reservas_pag():
    return render_template ('reservas.html')

# Detalhes de Reserva
@app.route('/detalhe-reserva')
def detalhe_reserva_pag():
    return render_template ('reserva/detalhe-reserva.html')

# Cadastros de sala
@app.route('/cadastrar-sala')
def cadastro_sala_pag():
    return render_template ('cadastrar-sala.html')

# POST (interagir com o CSV)

@app.route('/cadastro', methods=['POST'])
def cadastro_post():
    salvar_cadastro()
    return render_template('reservas.html')

@app.route('/cadastrar-sala', methods=['POST'])
def salas_post():
    salvar_sala()
    return render_template('listar-salas.html', salas=ler_csv())

@app.route('/reservar-sala', methods=['POST'])
def reservas_post():
    if request.method == 'POST':
        # Verifica se os dados enviados na solicitação são válidos
        if 'sala' in request.form and 'comeco' in request.form and 'fim' in request.form:
            # Salva a reserva no CSV
            reserva = salvar_reserva(request.form['sala'], request.form['comeco'], request.form['fim'])
            return render_template('reserva/detalhe-reserva.html', reserva=reserva)
        else:
            return 'Erro: Dados inválidos', 400
    else:
        return 'Erro: Solicitação inválida', 400

# Leitura e exibição dos CSVs

@app.route('/listar-salas')
def listar_salas():
    salas = ler_csv()
    print(f"Salas listadas: {salas}")  
    return render_template('listar-salas.html', salas=salas)