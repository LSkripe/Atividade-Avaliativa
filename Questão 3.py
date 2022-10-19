print("\n\tBem-vindo ao programa de Serviços de limpesa do Leonardo Skripe da Silva\n".upper())
print("*" * 80)
print("---------------------  Menu 1 de 3 - Metragem Limpeza --------------------------")

while True:
    metragem_limpeza = float(input("Informe a metragem da casa : "))

    if metragem_limpeza < 30 or metragem_limpeza > 700:
        print("Não aceitamos metragem abaixo de 30m² ou maior que 700m² !")
    else:
        print("Será necessários(as) dois(duas) funcionários(as) para a limpeza")
        print("*" * 10)
        break

print("---------------------  Menu 2 de 3 - Tipo ded Limpeza --------------------------")

while True:
    print("B - Básica - Indicada para sujeiras semanais ou quinzenais")
    print("C - Completa (30% a mais) - Indicado para sujeiras antigas e/ou não rotineiras")
    tipo_limpeza = input("Informe o tipo de limpeza desejada : ")

    if tipo_limpeza.upper() == "B":
        valor_limpeza = 1.00
        print("*" * 80)
        break
    elif tipo_limpeza.upper() == "C":
        valor_limpeza = 1.30
        print("*" * 80)
        break
    else:
        print("Opção Invalida !")

print("---------------------  Menu 3 de 3 - Adicional de Limpeza ----------------------")
adicional_limpeza = 0

while True:
    print("0 - Não desejo mais nada (Enecerrar)\n"
          "1 - Passar 10 (dez) peças de roupas - R$ 10,00\n"
          "2 - Limpeza de 1 (um) Forno/Micro-ondas - R$ 12,00\n"
          "3 - Limpeza de 1 (um) Geladeira/Freezer - R$ 20,00")
    adicional_opcao = int(input("-> "))

    if adicional_opcao == 0:
        print("*" * 80)
        break
    elif adicional_opcao == 1:
        adicional_limpeza = adicional_limpeza + 10.00
    elif adicional_opcao == 2:
        adicional_limpeza = adicional_limpeza + 12.00
    elif adicional_opcao == 3:
        adicional_limpeza = adicional_limpeza + 20.00
    else:
        print("Opção invalida !")

Valor_final = (metragem_limpeza * valor_limpeza) + adicional_limpeza

print("Total : R$ {:.2f} (Metragem : {:.2f} * Tipo : {:.2f} + Adicional : {:.2f} )".format(Valor_final, metragem_limpeza, valor_limpeza, adicional_limpeza))
print("*" * 80)