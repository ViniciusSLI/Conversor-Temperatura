def celsius_para_fahrenheit(celsius):
    # Converte a temperatura de Celsius para Fahrenheit
    return (celsius * 9/5) + 32

def fahrenheit_para_celsius(fahrenheit):
    # Converte a temperatura de Fahrenheit para Celsius
    return (fahrenheit - 32) * 5/9

def main():
    # Loop principal para executar o conversor de temperatura
    while True:
        # Exibe o menu de opções para o usuário
        print("Você deseja converter para qual unidade de temperatura?")
        print("[C] Celsius")
        print("[F] Fahrenheit")
        # Captura a escolha do usuário
        escolha = input("Escolha [C/F]: ").strip().upper()

        # Verifica a escolha do usuário e realiza a conversão correspondente
        if escolha == 'C':
            fahrenheit = float(input("Informe a temperatura em Fahrenheit: "))
            celsius = fahrenheit_para_celsius(fahrenheit)
            print(f"{fahrenheit} Fahrenheit é igual a {celsius:.2f} Celsius.")
        elif escolha == 'F':
            celsius = float(input("Informe a temperatura em Celsius: "))
            fahrenheit = celsius_para_fahrenheit(celsius)
            print(f"{celsius} Celsius é igual a {fahrenheit:.2f} Fahrenheit.")
        else:
            # Informa o usuário sobre uma escolha inválida e repete o loop
            print("Escolha inválida. Tente novamente.")
            continue

        # Pergunta ao usuário se deseja continuar ou encerrar o programa
        continuar = input("Deseja encerrar as conversões? (sim/não): ").strip().lower()
        if continuar == 'sim':
            # Se o usuário escolher encerrar, exibe uma mensagem e sai do loop
            print("Atividades finalizadas, volte sempre.")
            break

# Executa a função main() somente se o script for executado diretamente
if __name__ == "__main__":
    main()
