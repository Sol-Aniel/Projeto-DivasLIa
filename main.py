from Classes import *
from hashlib import sha256
print("Biblioteca DivasLia")
while(2!=3):
    senhap = sha256((input("Digite sua senha: ")).encode()).hexdigest()
    if senhap == "b0a9deffef295c3e560a840305f81b4ff3ea595c8d6a73219988162e7048e43d": \\Senha do Chefe
        print("Bem vindo a Biblioteca DivasLia, Patrão!")
    if  senhaf=="7865c2c6a64de74ed6b3a40f40304a77a9def37cf73beac1705e1b4c67b03c70":  \\Senha Funcinario
        print("Bem vindo! Como funcionário, você só pode visualizar os intens e atualizar os dados de emprestimo. Deseja visualizar? Digite visualizar e o que deseja visualizar. Deseja atualizar? Digite atualizar.")
        realizar=input("O que deseja fazer?")
        if realizar==visualizar:
            item=input("O que deseja visualizar?")
             if item=="livros":
               print(lista_livros)
             if item=="revistas":
               print(lista_revistas)               \\Visualizar Itens
             if item=="jornais":
               print(lista_jornais)
             if item=="funcionarios":
               print(lista_funcionarios)
            if item=="emprestimo":
               print(lista_emprestimos)
  
        else realizar=="atualizar":
              novo_emprestimo=Emprestimos()
              new_emprestimo=input("Informações do Empréstimo")    \\Modificar Emprestimos
              novo_emprestimo=new_emprestimo
              lista_emprestimo.append('novo_emprestimo')
        break
\\Instruçoẽs
       print("Você pode digitar o que deseja visualizar, utilizando as palavras chaves, sendo elas:\n livros, para ver os livros, revistas para ver as revistas, jornais para ver os jornais e funcionarios para acessar os dados de seus funcionários e empréstimos para visualizar os emprestimos em andamento.\n Além disso, você pode editar os dados digitanto o nome do dado que quer alterar")
       alterar=input("O que deseja alterar?")
       fazer=input("O que deseja visualizar?")
\\Ver os docs
       if fazer=="livros":
           print(lista_livros)
       if fazer=="revistas":
           print(lista_revistas)
       if fazer=="jornais":
           print(lista_jornais)
       if fazer=="funcionarios":
           print(lista_funcionarios)
        if fazer=="emprestimo":
            print(lista_emprestimos)
       else 
           print(Entendido, não deseja visualizar nada.)
\\Alterar lista de livros
       if alterar=="livros":
           editar_livro=input("Quer remover ou adicionar livros a sua biblioteca?")
           if editar_livro=="remover":
               livroedit=input("Nome do livro")   \\Remover um livro da lista
               lista_livros.remove('livroedit')
            else 
               novo_livro1=Livros()
               lista_livros.append('novo_livro1')  \\Adicionar um livro na lista
         if alterar=="revistas":
           editar_revista=input("Quer remover ou adicionar revistas a sua biblioteca?")
           if editar_revista==remover:
               revistaedit=input("Nome da revista")
               lista_revistas.remove('revistaedit')
            else 
               novo_revista1=Revistas()
               lista_revistas.append('novo_revista1')
         if alterar=="jornal":
           editar_jornal=input("Quer remover ou adicionar revistas a sua biblioteca?")
           if editar_jornal=="remover":
               jornaledit=input("Nome do jornal")
               lista_jornal.remove('jornaledit')
            else 
               novo_jornal1=Jornal()
               lista_jornal.append('novo_jornal1')
         if alterar=="funcionários":
           editar_funcionarios=input("Quer remover ou adicionar funcionários?")
           if editar_funcioarios=="remover":
               funcionarioedit=input("Nome do funcionário:")
               lista_funcionarios.remove('funcionarioedit')
            else 
               novo_funcionario1=Funcionario()              
               lista_funcionarios.append('novo_funcionario1')   
        
    else:
        print("Senha incorreta, por favor tente novamente.")

\\Testar o código
\\Verificar variaveis e nome das classes e adcionar os atributos das revistas e jornais


