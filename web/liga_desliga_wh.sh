#!/bin/zsh

echo "Ligar ou Desligar: "
read -r option 

option="${option:l}"

if [ "$option" = "ligar" ]; then
    # Inicia o processo webhook.py em segundo plano usando nohup
    nohup python /home/ubuntu/codes/python/integracao_google_forms/webhook.py &
    echo "Processo webhook.py iniciado."
elif [ "$option" = "desligar" ]; then
    # Busca o PID do processo webhook.py em execução
    pid=$(ps aux | grep 'webhook.py' | grep -v 'grep' | awk '{print $2}')
    
    # Verifica se o PID foi encontrado
    if [ -n "$option" ]; then
        # Encerra o processo com o PID encontrado
        kill $pid
        echo "Processo webhook.py com PID $pid encerrado com sucesso."
    else
        echo "Nenhum processo webhook.py em execução."
    fi
else
    echo "Uso: $0 [ligar|desligar]"
fi
