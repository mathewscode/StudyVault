# Formas de conectar diversos conteúdos à uma impressão ou variável.
nome = "Ricardo"
idade = 18
status = "solteiro"

print("Método 1: o usuario se chama " + nome + " tem", idade, "anos e esta " + status + ".")
print("Método 2: o usuario se chama {} tem {} anos e esta {}.".format(nome, idade, status))
print(f"Método 3: o usuario se chama {nome} tem {idade} anos e esta {status}.")