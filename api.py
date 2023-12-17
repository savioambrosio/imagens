from flask import Flask, jsonify, request

app = Flask(__name__)

# Chave de API
api_key = 'sua_chave_secreta'

# Rota da API
@app.route('/api/produtos', methods=['GET'])
def obter_produtos():
    # Verifica se a chave de API está presente na URL
    if 'api_key' not in request.args or request.args['api_key'] != api_key:
        return jsonify({'erro': 'Chave de API inválida'}), 401  # Resposta não autorizada

    # Lógica para obter e retornar os produtos
    produtos = [
        {'nome': 'Produto 1', 'preco': 19.99, 'imagem': 'https://github.com/savioambrosio/imagens/blob/main/1158530502_max.jpg?raw=true'},
        {'nome': 'Produto 2', 'preco': 29.99, 'imagem': 'https://github.com/savioambrosio/imagens/blob/main/1158530502_max.jpg?raw=true'},
    ]

    return jsonify({'produtos': produtos})

if __name__ == '__main__':
    app.run(debug=True)
