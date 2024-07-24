from flask import Flask, send_file, request, jsonify
import json
import logging
import main
import create_pdf
from msg_to_staff import DiscordWebhook
import discord
from discord.ext import commands
import threading
import os

app = Flask(__name__)
app.config['TIMEOUT'] = 60

intents = discord.Intents.default()
intents.members = True
bot = commands.Bot(command_prefix="!", intents=intents)

GUILD_ID = '1033501541115637860'
ROLE_NAME = 'Form preenchido'
DISCORD_TOKEN = os.getenv('TOKEN')

async def assign_role(discord_username):
    guild = bot.get_guild(int(GUILD_ID))
    role = discord.utils.get(guild.roles, name=ROLE_NAME)
    member = guild.get_member_named(discord_username)
    
    if member and role not in member.roles:
        await member.add_roles(role)
        print(f'Cargo {ROLE_NAME} atribuído a {discord_username}')


@app.route('/webhook', methods=['POST'])
def webhook():

    try:
        data = request.json

        with open('json/dados_recebidos.json', 'w') as f:
            json.dump(data, f, indent=4)

        create_pdf.instance_pdf(data, data['Nickname que você costuma usar in-game'])
        main.insert_db()
        main.mail(data['Endereço de e-mail'],data['Nickname que você costuma usar in-game'],data['Qual sua classe principal'])
        
        executor = DiscordWebhook()
        executor.send_recruitment_message(data['Nickname que você costuma usar in-game'], data['Nome de usuário Discord'], data['Qual sua classe principal'], data['Experiência no jogo'])

        discord_username = data['Nome de usuário Discord']
        bot.loop.create_task(assign_role(discord_username))
        
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
    

def run_flask():
    app.run(host='0.0.0.0', port=5000, debug=True, use_debugger=True, use_reloader=False)

if __name__ == '__main__':
    # Executar o Flask em uma thread separada
    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()
    
    # Executar o bot do Discord
    bot.run(DISCORD_TOKEN)


