
def verifica_impar_par(valor):
    
    status = int(valor) % 2

    if status == 0:
        return "par"
    else:
        return "impar"
    
valor_usuario = input("Digite o número que deseja saber se é impar ou par: \n")

status = verifica_impar_par(valor_usuario)

print(f"{valor_usuario} é {status}")