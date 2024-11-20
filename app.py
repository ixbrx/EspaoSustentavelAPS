from flask import Flask, request, jsonify, send_from_directory, render_template
import os

app = Flask(__name__, static_folder='static')  # Define a pasta 'assets' para os arquivos estáticos (CSS, JS, imagens)

# Fatores de emissão (em kg de CO₂ por kg de combustível)
fatores_emissao = {
    "RP-1": 3.15,
    "Hidrogênio Líquido": 0,  # LH2 não emite CO₂ diretamente
    "Metano": 2.75,
    "Combustível Sólido": 2.7
}

# Função para calcular as emissões de CO₂
def calcular_emissoes(tipo_combustivel, quantidade_combustivel):
    fator_emissao = fatores_emissao.get(tipo_combustivel, 0)
    emissoes = quantidade_combustivel * fator_emissao
    return emissoes

# Rota principal para carregar o HTML da calculadora
@app.route('/')
def index():
    return render_template('calculadora.html')  # Carrega o template HTML 'calculadora.html'

# Rota para processar os dados do formulário e calcular as emissões
@app.route('/calcular', methods=['POST'])
def calcular():
    tipo_combustivel = request.form.get('combustivel')
    quantidade_combustivel = float(request.form.get('quantidade', 0))
    lancamentos = int(request.form.get('lancamentos', 1))

    emissoes_totais = calcular_emissoes(tipo_combustivel, quantidade_combustivel) * lancamentos
    emissoes_totais_ton = emissoes_totais / 1000
    creditos_carbono = emissoes_totais_ton

    resultado = {
        "emissoes_totais": emissoes_totais_ton,
        "creditos_carbono": creditos_carbono
    }

    return jsonify(resultado)

# Servir arquivos estáticos (CSS, JS, imagens) da pasta 'assets'
@app.route('/assets/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.static_folder, filename)

# Iniciar o servidor Flask
if __name__ == '__main__':
    app.run(debug=True)


