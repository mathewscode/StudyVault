# Operadores relacionais: ==, !=, <, > <= e >=

def scriptTesteIdade(idade):
    if idade >= 18:
        print("Você pode usar o sistema!")
    else:
        print("Você não pode usar o sistema!")
    
idade = int(input("Sua idade: "))
scriptTesteIdade(idade)