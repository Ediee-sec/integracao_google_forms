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
    with open("documents/link_convite_discord.txt", 'r') as f:
        arquivo = f.read()
    
    return arquivo


def html(nome, classe):
    if 'healer' in classe.lower():
        classe = 'Healer'
    elif 'tank' in classe.lower():
        classe = 'Tank'
    elif 'dps' in classe.lower():
        classe = 'DPS'
    
    html_content = f"""
        <!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Bem-vindo à Fury</title>
                <style>
                    body {{
                        font-family: Arial, sans-serif;
                        background-color: #f4f4f4;
                        color: #333;
                        line-height: 1.6;
                        margin: 0;
                        padding: 0;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                    }}
                    .container {{
                        position: relative;
                        width: 80%;
                        max-width: 800px;
                        margin: auto;
                        background: rgba(255, 255, 255, 0.9);
                        padding: 20px;
                        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
                        text-align: center;
                        border-radius: 10px;
                    }}
                    h1 {{
                        color: #333;
                        font-size: 2.5em;
                        margin-bottom: 10px;
                    }}
                    p {{
                        margin: 10px 0;
                        font-size: 1.2em;
                    }}
                    .highlight {{
                        color: #E44D26;
                        font-weight: bold;
                    }}
                    .emoji {{
                        font-size: 1.5em;
                    }}
                    .btn-container {{
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        flex-wrap: wrap;
                        gap: 15px;
                        margin-top: 20px;
                    }}
                    .btn {{
                        display: inline-block;
                        padding: 10px 20px;
                        font-size: 18px;
                        color: #fff;
                        text-decoration: none;
                        border-radius: 5px;
                        transition: background-color 0.3s ease;
                    }}
                    .btn-discord {{
                        background-color: #7289DA;
                    }}
                    .btn-site {{
                        background-color: #1A73E8;
                    }}
                    .btn-guias {{
                        background-color: #F39C12;
                    }}
                    .btn:hover {{
                        background-color: #555;
                    }}
                    .img-container {{
                        width: 100%;
                        overflow: hidden;
                        border-radius: 10px;
                        margin-top: 20px;
                    }}
                    .img-container img {{
                        width: 100%;
                        height: auto;
                        border-radius: 10px;
                    }}
                </style>
            </head>
            <body>
                <div class="container">
                    <h1>{cumprimento()}, {nome}!</h1>
                    <p>Bem-vindo à <span class="highlight">Fury</span>.</p>
                    <p>Estamos contentes em ter um <span class="highlight">{classe}</span> como você em nossa guild <span class="emoji">😉</span></p>
                    <p>Somos uma comunidade de MMORPG competitiva, que valoriza as pessoas e a diversão sem perder a competitividade.</p>
                    <div class="btn-container">
                        <a href="https://discord.gg/furyteam" class="btn btn-discord">Junte-se ao nosso Discord</a>
                        <a href="http://guildfury.com.br" class="btn btn-site">Visite nosso Site</a>
                        <a href="https://tlacademy.mercadoonlinedigital.com/" class="btn btn-guias">Guias Throne And Liberty</a>
                    </div>
                    <div class="img-container">
                        <img src="https://media4.giphy.com/media/v1.Y2lkPTc5MGI3NjExajBxcWI3Z3YzcDJrcmFuOGtkbmx2a2pvaWl3d2t0ZHJlZGJ4eWprbCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/pzgdncQZ6Me0H4bQnU/giphy.gif" alt="Descrição da Imagem">
                    </div>
                </div>
            </body>
</html>
        """
    return html_content
