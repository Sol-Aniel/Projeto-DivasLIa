from hashlib import sha256
print("Biblioteca DivasLia")
while(2!=3):
    senha = sha256((input("Digite sua senha: ")).encode()).hexdigest()
    if senha == "b0a9deffef295c3e560a840305f81b4ff3ea595c8d6a73219988162e7048e43d":
        print("Bem vindo a Biblioteca DivasLia!")
        break
    else:
        print("Senha incorreta, por favor tente novamente.")
