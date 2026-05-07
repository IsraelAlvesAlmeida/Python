# Importação da biblioteca
from colorama import Fore, Style, init

# Inicializa o colorama
init(autoreset=True)

# Lista com níveis e mensagens
niveis = [
    ("Nível 1", "Muito baixo (crítico)"),
    ("Nível 2", "Baixo"),
    ("Nível 3", "Médio"),
    ("Nível 4", "Alto"),
    ("Nível 5", "Muito alto (alerta)")
]

# Função para definir a cor com base no nível
def definir_cor(nivel):
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE

# Função para exibir o status do reservatório
def exibir_status():
    print("=== Monitoramento do Reservatório ===\n")
    
    for i, (nivel, mensagem) in enumerate(niveis, start=1):
        cor = definir_cor(i)
        print(cor + f"{nivel}: {mensagem}")

    print("\nSistema finalizado.")
    print(Style.RESET_ALL)  # Garante reset manual (segurança extra)

# Execução do sistema (simulação)
exibir_status()