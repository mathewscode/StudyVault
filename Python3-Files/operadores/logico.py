# Operadores Lógicos: AND, OR e NOT.

username = "maria4590"
password = "maria0000"

def loginTeste(inputname, inputPass):
    if (inputname and inputPass) == (username and password):
        print("Bem-vindo(a)! Username e Password corretos.")
    else:
        print("Nome de usuário ou senha incorreto!")
        
loginTeste("maria4590", "maria0000")
