# Pesquisa de opinião - TudoWeb
# Autor: Israel
# Objetivo: Coletar opiniões de clientes sobre atendimento usando FOR

# Inicialização dos contadores
excelente = 0
ruim = 0

# Lista para armazenar todos os entrevistados
entrevistados = []

# Teste com 10 entrevistados (pode alterar para 50)
total_entrevistados = 10

print("=== Pesquisa de Satisfação - TudoWeb ===")
print("Digite sua opinião sobre o atendimento:")
print("1 - EXCELENTE | 2 - BOM | 3 - RUIM\n")

for i in range(total_entrevistados):
    print(f"Entrevistado {i+1}/{total_entrevistados}")
    nome = input("Nome: ")
    idade = int(input("Idade: "))
    opiniao = int(input("Opinião (1-EXCELENTE, 2-BOM, 3-RUIM): "))

    # Estrutura de decisão para contar respostas
    if opiniao == 1:
        excelente += 1
    elif opiniao == 3:
        ruim += 1

    # Guardar dados do entrevistado
    entrevistados.append({
        "nome": nome,
        "idade": idade,
        "opiniao": opiniao
    })

    print("-" * 40)

# Exibir resultados finais
print("\n=== RESULTADO DA PESQUISA ===")
print(f"Quantidade de respostas EXCELENTE: {excelente}")
print(f"Quantidade de respostas RUIM: {ruim}")

# Mostrar resumo geral
print("\nResumo dos entrevistados:")
for e in entrevistados:
    opiniao_texto = "EXCELENTE" if e["opiniao"] == 1 else "BOM" if e["opiniao"] == 2 else "RUIM"
    print(f"{e['nome']} ({e['idade']} anos) - {opiniao_texto}")

# Trava final para visualizar resultados
input("\nPressione ENTER para sair...")
