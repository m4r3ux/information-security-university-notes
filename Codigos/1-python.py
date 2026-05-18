import os

if os.path.exists("dados.txt"):
    print("Arquivo existe")
else:
    print("Arquivo não encontrado")