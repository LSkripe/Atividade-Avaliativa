print("\n\tBem-vindo a Sorveteria do Leonardo Skripe da Silva")

print("-----------------------------------------Cardápio---------------------------------------------")
print("| Código |       Descrição      | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml)|")
print("|   TR   | Sabores Tradicionais |      R$ 6,00      |      R$ 10,00      |      R$ 18,00     |")
print("|   ES   | Sabores Especias     |      R$ 7,00      |      R$ 12,00      |      R$ 21,00     |")
print("|   PR   | Sabores Premium      |      R$ 8,00      |      R$ 14,00      |      R$ 24,00     |")
print("----------------------------------------------------------------------------------------------\n")

Valor_total = 0  # Declaração de váriavél.
x = 1  # Declaração de váriavel.

while x != 0:  # Váriavél de repetição;

    tamanho = input("Informe o codigo tamanho do pote desejada (P/M/G) : ")
    codigo = input("Informe o código do sabor desejado (TR/ES/PR) : ")

    if codigo.upper() == "TR":  # É usado o ".upper()" para deizar o texto em caixa alta, ex: tr -> TR.
        sabor = "Tradicional"
        if tamanho.upper() == "P":
            valor = 6.00
            tam = "Pequeno"  # Atribuição do tamanho a uma variavél
        elif tamanho.upper() == "M":
            valor = 10.00
            tam = "Médio"
        elif tamanho.upper() == "G":
            valor = 18.00
            tam = "Grande"
        else:  # Caso o código do tamanho for digitado erraddo, é mostrado está mensagem.
            print("\n!!!!!!!!! Codigo do Tamanho Incorreto !!!!!!!!!\n")
            continue  # Retorna para o começo da variavéç, onde irá perguntar novamente as opções.

    elif codigo.upper() == "ES":
        sabor = "Especial"
        if tamanho.upper() == "P":
            valor = 7.00
            tam = "Pequeno"
        elif tamanho.upper() == "M":
            valor = 12.00
            tamp = "Médio"
        elif tamanho.upper() == "G":
            valor = 18.00
            tam = "Grande"
        else:
            print("\n!!!!!!!!! Codigo do Tamanho Incorreto !!!!!!!!!\n")
            continue

    elif codigo.upper() == "PR":
        sabor = "Premium"
        if tamanho.upper() == "P":
            valor = 8.00
            tam = "Pequeno"
        elif tamanho.upper() == "M":
            valor = 14.00
            tam = "Médio"
        elif tamanho.upper() == "G":
            valor = 24.00
            tam = "Grande"

        else:
            print("\n!!!!!!!!! Codigo do Tamanho Incorreto !!!!!!!!!\n")
            continue

    else:  # Caso o codigo do produto for digitado erraddo, mostrado está mensagem.
        print("\n!!!!!!!!! Codigo do Produto Incorreto !!!!!!!!!\n")
        continue

    print("Você pediu um sorvete tamanho {} de sabor {} no valor de R$ {:.2f}".format(tam, sabor, valor))
    Valor_total = float(Valor_total + valor)  # Irá somar todos os pedidos feitos durante a execução;
    print("-------------------------------------------------------------")

    while True:  # usado para confirmar se deseja continuar ou não, também existe a verificação da opção informada.
        op = input("Deseja repetir a operação (S/N) ?  ")

        if op.upper() == "S":
            x = 1
            break
        elif op.upper() == "N":
            x = 0
            break
        else:
            print("opção invalida !")

print("Total a ser pago : R$ {:.2f}".format(Valor_total))
