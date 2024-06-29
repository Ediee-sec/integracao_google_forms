from flask import Flask, send_file, request
import json
import logging
import main

app = Flask(__name__)
app.config['TIMEOUT'] = 60

# Configuração do logger do Flask
logging.basicConfig(filename='/home/ubuntu/codes/python/integracao_google_forms/log/flask_debug.log', level=logging.DEBUG)

@app.route('/webhook', methods=['POST'])
def webhook():

    try:
        data = request.json

        with open('/home/ubuntu/codes/python/integracao_google_forms/json/dados_recebidos.json', 'w') as f:
            json.dump(data, f, indent=4)

        main.insert_db()
        main.mail()

        return 'OK', 200
    except Exception as e:
        return f'ERRO OCORREU UM ERRO NA APLICAÇÃO {e}', 100
    
    
@app.route('/debug')
def debug():
    return send_file('/home/ubuntu/codes/python/integracao_google_forms/log/flask_debug.log')

@app.route('/status')
def status():
    
    return 'Flask está ativo!'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_debugger=True, use_reloader=False)


