import json

dados = {
    "nome": "Carlos",
    "idade": 40
}

json_texto = json.dumps(dados)

print(json_texto)