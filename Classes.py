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
    def __init__(self, Titulo, PubANO, Editora, Idioma, Disponibilidade):
        self.Titulo = str(Titulo)
        self.PubANO = int(PubANO)
        self.Editora = str(Editora)
        self.Idioma = str(Idioma)
        self.Disponibilidade = bool(Disponibilidade)

class Livros (Documentos):
    def __init__(self, Titulo, Autor, PubANO, Editora, Edição, Disponibilidade):
        super().__init__(Titulo, PubANO, Editora, Disponibilidade)
        self.Autor = str(Autor)
        self.Edição = int(Edição)
class Revistas (Documentos):
    def __init__(self, Titulo, PubANO, PubSEM, Editora, Idioma, Disponibilidade):
        super().__init__(Titulo, PubANO, Editora, Idioma, Disponibilidade)
        self.PubSEM = int(PubSEM)
class Jornais (Documentos):
    def __init__(self, Titulo, PubANO, PubDIA, Editora, Idioma, Disponibilidade):
        super().__init__(Titulo, PubANO, Editora, Idioma, Disponibilidade)
        self.PubDIA = int(PubDIA)

class Emprestimos:
    def __init__(self, Cliente, Documento, DataRet, DataDev):
        self.Cliente = str(Cliente)
        self.Documento = str(Documento)
        self.DataRet = str(DataRet)
        self.DataDev = str(DataDev)
