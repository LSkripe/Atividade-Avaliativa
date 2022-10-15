print("\n\tbem-vindo a loja do Leonardo Skripe da Silva\n")

Vproduto = float(input("Entre com o valor do produto : R$ "))
Qproduto = int(input("Entre com a quantidade de produtos : "))

VTproduto = Vproduto * Qproduto # Calculo da compra.

if Qproduto < 11:   # Verificação de quantidade de produto.
    Vfrete = 30     # Valor de incrimento em relação ao frete.
elif Qproduto < 101:
    Vfrete = 60
elif Qproduto < 1001:
    Vfrete = 120
else:
    Vfrete = 240

Vfinal = VTproduto + Vfrete # Calculo do pedido com o valor do frete.
print("Valor total sem o frete é : R$ {:.2f}".format(VTproduto))
print("Valor total com o frete é : R$ {:.2f}    (valor do frete R$ {:.2f})".format(Vfinal, Vfrete))