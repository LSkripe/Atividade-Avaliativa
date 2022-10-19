while True:
    op = input("Deseja repetir a operação (S/N) ?  ")

    if op.upper() == "S":
        x = 1
    elif op.upper() == "N":
        break
    else:
        print("opção invalida !")

        if metragem_limpeza < 300:
            valor_metragem = (metragem_limpeza * tipo) + adicional
        else:
            valor_metragem = (metragem_limpeza * tipo) + adicional