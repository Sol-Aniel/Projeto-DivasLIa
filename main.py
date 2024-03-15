from hashlib import sha256
from Classes import *
print("Biblioteca DivasLia")
while(2!=3):
    senha = sha256((input("Digite sua senha: ")).encode()).hexdigest()
    if senha == "0559329ef95a60080163a64be4f8867cc297ba64187c7e061f724da5dc793480":
        print("Bem vindo Matusálem!")
        break
    else:
        print("Senha incorreta, por favor tente novamente.")
