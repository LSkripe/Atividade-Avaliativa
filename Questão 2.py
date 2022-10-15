print("\n\tBem-vindo a Sorveteria do Leonardo Skripe da Silva")

print("-----------------------------------------Cardápio---------------------------------------------")
print("| Código |       Descrição      | Tamanho P (500ml) | Tamanho M (1000ml) | Tamanho G (2000ml |")
print("|   TR   | Sabores Tradicionais |      R$ 6,00      |      R$ 10,00      |      R$ 18,00     |")
print("|   ES   | Sabores Especias     |      R$ 7,00      |      R$ 12,00      |      R$ 21,00     |")
print("|   PR   | Sabores Premium      |      R$ 8,00      |      R$ 14,00      |      R$ 24,00     |")
print("----------------------------------------------------------------------------------------------")

tamanho = input("\nInforme o codigo tamanho do pote desejada (P/M/G) : ")
codigo = input("Informe o código do sabor desejado (TR/ES/PR) : ")

if codigo.upper() == "TR": # É usado o ".upper()" para deizar o texto em caixa alta, ex: tr -> TR.
    sabor = "Tradicional"
    if tamanho.upper() == "P":
        valor = 6.00
    elif tamanho.upper() == "M":
        valor = 10.00
    elif tamanho.upper() == "G":
        valor = 18.00
    else: # Caso o código do tamanho for digitado erraddo, é mostrado está mensagem.
        print("!!!!!!!!! Codigo do Tamanho Incorreto !!!!!!!!!")

elif codigo.upper() == "ES":
    sabor = "Especial"
    if tamanho.upper() == "P":
        valor = 7.00
    elif tamanho.upper() == "M":
        valor = 12.00
    elif tamanho.upper() == "G":
        valor = 18.00
    else:
        print("!!!!!!!!! Codigo do Tamanho Incorreto !!!!!!!!!")

elif codigo.upper() == "PR":
    sabor = "Premium"
    if tamanho.upper() == "P":
        valor = 8.00
    elif tamanho.upper() == "M":
        valor = 14.00
    elif tamanho.upper() == "G":
        valor = 24.00
    else:
        print("!!!!!!!!! Codigo do Tamanho Incorreto !!!!!!!!!")

else: # Caso o codigo do produto for digitado erraddo, mostrado está mensagem.
    print("!!!!!!!!! Codigo do Produto Incorreto !!!!!!!!!")

print("-------------------------------------------------------------")

print("R${:.2f}".format(valor))
print(codigo)
print(tamanho)