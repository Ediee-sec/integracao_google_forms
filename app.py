from flask import Flask, send_file, request, jsonify
import json
import logging
import main
import create_pdf

app = Flask(__name__)
app.config['TIMEOUT'] = 60


@app.route('/webhook', methods=['POST'])
def webhook():

    try:
        data = request.json

        with open('json/dados_recebidos.json', 'w') as f:
            json.dump(data, f, indent=4)

        create_pdf.instance_pdf(data, data['Nickname'])
        #main.insert_db()
        main.mail(data['Endereço de e-mail'],data['Nickname'],data['Função'])

        return 'OK', 200
    except Exception as e:
        response = {
            "error": str(e),
            "message": "An error occurred"
        }
        return jsonify(response), 500
    
    
@app.route('/debug')
def debug():
    return send_file('log/flask_debug.log')

@app.route('/status')
def status():
    
    return 'Flask está ativo!'
    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True, use_debugger=True, use_reloader=False)


