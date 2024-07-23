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
            
    def send_recruitment_message(self, name, discord_tag, weapon, user_id):
        def get_role_emoji(weapon):
            if  'healer' in weapon.lower():
                return '⚕️'
            elif 'tank' in weapon.lower():
                return '🛡️'
            elif 'dps' in weapon.lower():
                return '⚔️'
            elif 'assassino' in weapon.lower():
                return '🗡️'
            else:
                return ''

        role_emoji = get_role_emoji(weapon)
        
        embed = {
            "content": "",  # Mensagem de conteúdo em branco
            "embeds": [
                {
                    "title": f"{name} 🥸 preencheu o formulário",
                    "description": (
                        f"**Detalhes**: \n\n"
                        f"**Discord**: {discord_tag} \n"
                        f"**Classe**: {weapon} {role_emoji}\n"
                        f"**Experiência**: {user_id}"
                    ),
                    "color": 800000,  # Valor hexadecimal da cor do embed
                    "footer": {
                        "text": "Formulário de Recrutamento"
                    }
                }
            ]
        }

        self.send_message(embed)

        

        

