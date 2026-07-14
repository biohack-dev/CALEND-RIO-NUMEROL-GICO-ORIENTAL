import calendar
from datetime import datetime
from colorama import init, Fore, Style

init(autoreset=True)

def soma_cabalistica(dia, mes, ano):
    """Reduz a soma a um único dígito (1-9) estilo numerologia"""
    soma = dia + mes + ano
    while soma > 9:
        soma = sum(int(d) for d in str(soma))
    return soma

# Obtém data atual
hoje = datetime.now()
ano = hoje.year
mes = hoje.month

# Gera calendário
cal = calendar.monthcalendar(ano, mes)

# Nomes dos meses
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
         "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

# Cabeçalho
print(f"\n{meses[mes-1]} {ano}")
print("Dom Seg Ter Qua Qui Sex Sáb")

# Exibe calendário
for semana in cal:
    linha = ""
    for dia in semana:
        if dia == 0:
            linha += "    "
        else:
            resultado = soma_cabalistica(dia, mes, ano)
            if resultado == 4:
                linha += f"{Fore.RED}{dia:2d}{Style.RESET_ALL}  "
            elif resultado == 7:
                linha += f"{Fore.GREEN}{dia:2d}{Style.RESET_ALL}  "
            else:
                linha += f"{dia:2d}  "
    print(linha)