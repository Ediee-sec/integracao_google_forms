from datetime import datetime, timedelta

def cumprimento():

    hora_atual = datetime.today() - timedelta(hours=3)

    intervalos = [
        (datetime.strptime('00:00', '%H:%M').time(), datetime.strptime('04:59', '%H:%M').time(), "Boa madrugada"),
        (datetime.strptime('05:00', '%H:%M').time(), datetime.strptime('11:59', '%H:%M').time(), "Bom dia"),
        (datetime.strptime('12:00', '%H:%M').time(), datetime.strptime('17:59', '%H:%M').time(), "Boa tarde"),
        (datetime.strptime('18:00', '%H:%M').time(), datetime.strptime('23:59', '%H:%M').time(), "Boa noite")
    ]

    for inicio, fim, saudacao in intervalos:
        if inicio <= hora_atual.time() <= fim:
            return saudacao
        
def get_link_invite():
    with open("/home/ubuntu/codes/python/integracao_google_forms/documents/link_convite_discord.txt", 'r') as f:
        arquivo = f.read()
    
    return arquivo


def html(nome):
    html_content = f"""
        <html>
        <head>
            <title>Bem-vindo à Guild</title>
            <style>
                body {{
                    font-family: Arial, sans-serif;
                    background-color: #f0f0f0;
                    color: #333;
                }}
                h1 {{
                    color: #007BFF;
                }}
                p {{
                    font-size: 18px;
                }}
                a {{
                    color: #007BFF;
                    text-decoration: none;
                }}
                a:hover {{
                    text-decoration: underline;
                }}
                .banner {{
                    width: 50%;
                    height: auto;
                }}
            </style>
        </head>
        <body>
            <h1>{cumprimento()} {nome}</h1>
            <p>Estamos contentes em saber que você deseja fazer parte da nossa guild</p>
            <p>O próximo passo agora é um bate papo com um de nossos líderes no discord</p>
            <p>Assim que acessar o discord irá receber uma mensagem do nosso bot no privado para garantir o seu cargo</p>
            <p><a href="{get_link_invite()}">CLICK DISCORD</a></p>
            </br>
            <p>Atenciosamente</p>
            <p>Staff Guild Fury (SA)</p>
            <img src="https://media2.giphy.com/media/v1.Y2lkPTc5MGI3NjExenFxbWo2a3htbWIzeGh3dzNid3F5NHM0aWk0MjBnamNsdHRuNzNnNSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/7tJ4q1ZOT1YBuUrzxp/giphy.gif" alt="Banner" class="banner">
        </body>
        </html>
        """
    return html_content
