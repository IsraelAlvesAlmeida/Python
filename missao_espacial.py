# missao_espacial.py
# Programa para calcular o tempo de viagem espacial
# Autor: Israel
# Data: 03/03/2026

def calcular_tempo_viagem(distancia_km, velocidade_kmh):
    """
    Calcula o tempo de viagem em horas e dias.
    """
    tempo_horas = distancia_km / velocidade_kmh
    tempo_dias = tempo_horas / 24
    return tempo_horas, tempo_dias


def calcular_consumo(distancia_km, consumo_km_por_litro, preco_combustivel):
    """
    Calcula o consumo de combustível e o custo total.
    """
    litros_necessarios = distancia_km / consumo_km_por_litro
    custo_combustivel = litros_necessarios * preco_combustivel
    return litros_necessarios, custo_combustivel


def calcular_custos_extras(valor_pedagios):
    """
    Retorna o valor de pedágios/portos espaciais.
    """
    return valor_pedagios


def exibir_resultado(nome_astronauta, distancia_km, velocidade_kmh, tempo_horas, tempo_dias, litros, custo_combustivel, custo_total):
    """
    Exibe o resultado formatado da simulação.
    """
    print(f"""
Astronauta {nome_astronauta}, bem-vindo à simulação!
A viagem terá uma distância de {distancia_km:.0f} km.
Com velocidade média de {velocidade_kmh:.0f} km/h, o tempo estimado é:
{tempo_horas:.2f} horas ({tempo_dias:.2f} dias).

Consumo estimado de combustível: {litros:.2f} litros
Custo total de combustível: R$ {custo_combustivel:.2f}
Custo total da missão (incluindo taxas): R$ {custo_total:.2f}

Boa sorte na missão!
    """)


def main():
    """
    Função principal que organiza o fluxo do programa.
    """
    # Entrada de dados com validações
    nome_astronauta = input("Digite seu nome completo: ")

    try:
        distancia_km = float(input("Digite a distância da viagem em km: "))
        if distancia_km <= 0:
            raise ValueError("A distância deve ser maior que zero.")

        velocidade_kmh = float(input("Digite a velocidade média da nave em km/h: "))
        if velocidade_kmh <= 0:
            raise ValueError("A velocidade deve ser maior que zero.")

        consumo_km_por_litro = float(input("Digite o consumo da nave (km por litro): "))
        if consumo_km_por_litro <= 0:
            raise ValueError("O consumo deve ser maior que zero.")

        preco_combustivel = float(input("Digite o preço do combustível por litro (R$): "))
        if preco_combustivel < 0:
            raise ValueError("O preço não pode ser negativo.")

        valor_pedagios = float(input("Digite o valor total de pedágios/portos espaciais (R$): "))
        if valor_pedagios < 0:
            raise ValueError("O valor não pode ser negativo.")

    except ValueError as e:
        print(f"Erro: {e}")
        input("Pressione Enter para encerrar...")
        return

    # Processamento
    tempo_horas, tempo_dias = calcular_tempo_viagem(distancia_km, velocidade_kmh)
    litros, custo_combustivel = calcular_consumo(distancia_km, consumo_km_por_litro, preco_combustivel)
    custos_extras = calcular_custos_extras(valor_pedagios)
    custo_total = custo_combustivel + custos_extras

    # Saída
    exibir_resultado(nome_astronauta, distancia_km, velocidade_kmh, tempo_horas, tempo_dias, litros, custo_combustivel, custo_total)

    # Pausa para evitar fechamento imediato
    input("Pressione Enter para encerrar...")


# Execução do programa
if __name__ == "__main__":
    main()
