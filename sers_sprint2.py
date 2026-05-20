# =========================================
# Gestão Sustentável de Eletropostos
# Sprint 2 - Prova de Conceito Funcional
# =========================================

print("===================================")
print(" GESTÃO SUSTENTÁVEL DE ELETROPOSTOS ")
print("===================================")

while True:

    print("\nMENU")
    print("1 - Simular recarga")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    # =========================================
    # SIMULAÇÃO DE RECARGA
    # =========================================

    if opcao == "1":

        print("\n--- SIMULAÇÃO DE RECARGA ---")

        tempo = float(input("Digite o tempo de carregamento (em horas): "))
        potencia = float(input("Digite a potência do carregador (kW): "))

        # Cálculo do consumo
        consumo = tempo * potencia

        # Valor fictício por kWh
        valor_kwh = 0.85

        # Cálculo do custo
        custo = consumo * valor_kwh

        # Simulação de energia solar
        energia_solar = input(
            "A energia utilizada veio de fonte solar? (s/n): "
        ).lower()

        # =========================================
        # RESULTADOS
        # =========================================

        print("\n====== RESULTADO DA RECARGA ======")

        print(f"Tempo de carregamento: {tempo:.1f} horas")
        print(f"Potência do carregador: {potencia:.1f} kW")
        print(f"Consumo total: {consumo:.2f} kWh")
        print(f"Custo estimado: R$ {custo:.2f}")

        if energia_solar == "s":
            print("Fonte de energia: Sustentável ☀️")
            print("Menor impacto ambiental e maior eficiência energética.")
        else:
            print("Fonte de energia: Rede elétrica comum")
            print("Considere utilizar energia renovável.")

    # =========================================
    # SAIR
    # =========================================

    elif opcao == "2":
        print("\nEncerrando sistema...")
        print("Obrigado por utilizar o sistema!")
        break

    # =========================================
    # OPÇÃO INVÁLIDA
    # =========================================

    else:
        print("\nOpção inválida! Tente novamente.")