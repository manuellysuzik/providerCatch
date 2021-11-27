## MONITORAMENTO DE INTERNET
---
## Instalando as libs
    pip install -r requirements.txt
## Rodando...
    python3 main_script.py
## Método que usei
 - Adicionei uma cron no meu WSL para rodar o script a cada 10 minutos. Esse intervalo você pode definir de acordo com sua necessidade.

## Para registrar uma cron em seu Linux
    crontab -e
## Escolha o seu editor de arquivos preferido no linux ( no meu caso foi o nano) adicione no fim do arquivo o comando abaixo:
    * * * * * cd /home/<usuario>/<providerCatch> && python3 main_script.py >> <nome do arquivo de log> 2>&1
