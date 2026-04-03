def calcular_consumo():
    print("=== Calculadora de Consumo de Energia ===")

    aparelho = input("Digite o nome do aparelho: ")
    potencia = float(input("Digite a potência do aparelho em watts (W): "))
    horas_dia = float(input("Digite o tempo médio de uso diário em horas: "))

    consumo_mensal = (potencia * horas_dia * 30) / 1000  # kWh
    custo_estimado = consumo_mensal * 0.75  # R$ 0,75 por kWh

    print("\n--- Resultado ---")
    print(f"Aparelho: {aparelho}")
    print(f"Consumo mensal: {consumo_mensal:.2f} kWh")
    print(f"Custo estimado: R$ {custo_estimado:.2f}")

    # Trava para não fechar imediatamente
    while True:
        sair = input("\nDeseja fechar o programa? (s/n): ").strip().lower()
        if sair == "s":
            print("Encerrando... Obrigado por usar a calculadora!")
            break
        else:
            print("Programa continuará aberto. Faça seu print da tela! 😉")


if __name__ == "__main__":
    calcular_consumo()
