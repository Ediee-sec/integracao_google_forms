import requests
import json


class DiscordWebhook:
    def __init__(self):
        self.webhook_url = 'https://discordapp.com/api/webhooks/1256713225836429312/g40vOjqMT_kUPXoZBubGRQ2tqVBXdN8hfbwSc_ptFyCnSVaIeVtQ8w0tUkXnsRe3TPNR'

    def send_message(self, embed):
        print("Payload enviado:", json.dumps(embed, indent=4))  # Adiciona essa linha para ver o payload
        response = requests.post(self.webhook_url, data=json.dumps(embed), headers={'Content-Type': 'application/json'})
        if response.status_code == 204:
            print('Mensagem enviada com sucesso!')
        else:
            print(f'Erro ao enviar mensagem: {response.status_code}')
            print(response.json())
            
    def send_recruitment_message(self, name, discord_tag, weapon, role, user_id):
        def get_role_emoji(role):
            if role.lower() == 'healer':
                return '⚕️'
            elif role.lower() == 'tank':
                return '🛡️'
            elif role.lower() == 'dps':
                return '⚔️'
            elif role.lower() == 'assassino':
                return '🗡️'
            else:
                return ''

        role_emoji = get_role_emoji(role)
        
        embed = {
            "content": "",  # Mensagem de conteúdo em branco
            "embeds": [
                {
                    "title": f"{name} 🥸 preencheu o formulário",
                    "description": (
                        f"**Detalhes**: \n\n"
                        f"**Discord**: {discord_tag} \n"
                        f"**Armas**: {weapon} \n"
                        f"**Função**: {role} {role_emoji} \n"
                        f"**ID**: {user_id}"
                    ),
                    "color": 800000,  # Valor hexadecimal da cor do embed
                    "footer": {
                        "text": "Formulário de Recrutamento"
                    }
                }
            ]
        }

        self.send_message(embed)

        

        

