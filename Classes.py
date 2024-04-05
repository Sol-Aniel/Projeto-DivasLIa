lista_pessoa=[]
lista_funcionario=[]
lista_livros=[]
lista_revistas=[]
lista_jornais=[]
lista_emprestimos=[]

class Pessoa:
    def __init__(self, Nome, CPF, Tel, Email, Endereco):
        self.Nome = str(Nome)
        self.CPF = str(CPF)
        self.Tel = int(Tel)
        self.Email = str(Email)
        self.Endereco = str(Endereco)

class Funcionarios (Pessoa):
    def __init__(self, Nome, CPF, Tel, Email, Endereco, Salario, CH, Codigo):
        super().__init__(self, Nome, CPF, Tel, Email, Endereco)
        self.Salario = float(Salario)
        self.CH = float(CH)
        self.Codigo = int(Codigo)

class Documentos:
    def __init__(self, Titulo, PubANO, Editora, Idioma, Disponibilidade, quantidade):
        self.Titulo = str(Titulo)
        self.PubANO = int(PubANO)
        self.Editora = str(Editora)
        self.Idioma = str(Idioma)
        self.Disponibilidade = bool(Disponibilidade)
        self.quantidade=int(quantidade)

class Livros (Documentos):
    def __init__(self, Titulo, PubANO, Editora, Idioma, Disponibilidade, quantidade):
        super().__init__(self, Titulo, PubANO, Editora, Idioma, Disponibilidade, quantidade)
        self.Autor = str(Autor)
        self.Edição = int(Edição)
class Revistas (Documentos):
    def __init__(self, Titulo, PubANO, Editora, Idioma, Disponibilidade, quantidade):
        super().__init__(self, Titulo, PubANO, Editora, Idioma, Disponibilidade, quantidade)
        self.PubSEM = int(PubSEM)
class Jornais (Documentos):
    (self, Titulo, PubANO, Editora, Idioma, Disponibilidade):
        super().__init__(self, Titulo, PubANO, Editora, Idioma, Disponibilidade, quantidade):
        self.PubDIA = int(PubDIA)

class Emprestimos:
    def __init__(self, Cliente, Documento, DataRet, DataDev):
        self.Cliente = str(Cliente)
        self.Documento = str(Documento)
        self.DataRet = str(DataRet)
        self.DataDev = str(DataDev)

livro1=Livro("Dom Quixote", 1605, "Editorial Clássicos","Miguel de Cervantes", " 1ª edição", 3)
livro2=Livro("1984", 1949, "Penguin Books","George Orwell", " 1ª edição", 6)
livro3=Livro("Orgulho e Preconceito", 1813," Penguin Classics","Jane Austen", "1ª edição", 2)
livro4=Livro("Cem Anos de Solidão", 1967, "HarperCollins","Gabriel García Márquez", "1ª edição", 1)
livro5=Livro(""Harry Potter e a Pedra Filosofal", 1997, "Bloomsbury Publishing","J.K Rolling", "1ª edição", 9)
livro6=Livro("O Senhor dos Anéis: A Sociedade do Anel", 1954, "Houghton Mifflin","J.R.R. Tolkien", "1ª edição", 8)
livro7=Livro("Crime e Castigo", 1866, "Editora 34","Fiódor Dostoiévski", "1ª edição", 5)
livro8=Livro("A revolução dos Bixos", 1945, "Companhia das Letras","George Orwell", "1ª edição", 15)
livro9=Livro("O Pequeno Príncipe", 1943, "Agir","Antoine de Saint-Exupéry", "1ª edição", 25)
livro10=Livro("O Apanhador no Campo de Centeio", 1951, "Little, Brown and Company","J.D. Salinger", "1ª edição", 11)

revista1=Revistas("Nactional Geographic",'National Geographic Society' 2022, 1)
revista2=Revistas("Time", "Time USA LLC", 2024, 9)
revista3=Revistas("Scientific American" ,"Springer Nature", 2024, 16)
revista4=Revistas("The Economist" ,"The Economist Group" ,2023, 7)
revista5=Revistas("Vogue","Condé Nast", 2022, 13)

jornal1=Jornais("The New York Times", "The New York Times Company", 2024, 25)
jornal2=Jornais("The Guardian", "Guardian Media Group", 2024, 37)
jornal3=Jornais("Le Monde", "Groupe Le Monde", 2024, 28)
jornal4=Jornais("The Times", "News UK", 2024, 53)
jornal5=Jornais("El País", "PRISA", 2024, 13)
jornal6=Jornais("Der Spiegel", "Spiegel-Verlag", 2024, 17)
jornal7=Jornais("Yomiuri Shimbun", "The Yomiuri Shimbun Holdings", 2024, 43)

lista_livros.append('livro1','livro2', 'livro3', 'livro4', 'livro5', 'livro6','livro7','livro8', 'livro9','livro10')
lista_revistas.append('revista1','revista2','revista3','revista4','revista5')
lista_jornais.append('jornal1','jornal2','jornal3','jornal4','jornal5','jornal6','jornal7')
