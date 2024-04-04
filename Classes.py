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

livro1.livros=("Dom Quixote", 1605, "Editorial Clássicos","Miguel de Cervantes", " 1ª edição", 3)
livro2.livros=("1984", 1949, "Penguin Books","George Orwell", " 1ª edição", 6)
livro3.livros=("Orgulho e Preconceito", 1813," Penguin Classics","Jane Austen", "1ª edição", 2)
livro4.livros=("Cem Anos de Solidão", 1967, "HarperCollins","Gabriel García Márquez", "1ª edição", 1)
livro5.livros=(""Harry Potter e a Pedra Filosofal", 1997, "Bloomsbury Publishing","J.K Rolling", "1ª edição", 9)
livro6.livros=("O Senhor dos Anéis: A Sociedade do Anel", 1954, "Houghton Mifflin","J.R.R. Tolkien", "1ª edição", 8)
livro7.livros=("Crime e Castigo", 1866, "Editora 34","Fiódor Dostoiévski", "1ª edição", 5)
livro8.livros=("A revolução dos Bixos", 1945, "Companhia das Letras","George Orwell", "1ª edição", 15)
livro9.livros=("O Pequeno Príncipe", 1943, "Agir","Antoine de Saint-Exupéry", "1ª edição", 25)
livro10.livros=("O Apanhador no Campo de Centeio", 1951, "Little, Brown and Company","J.D. Salinger", "1ª edição", 11)
