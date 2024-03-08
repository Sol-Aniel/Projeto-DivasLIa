class Funcionários:
    def __init__(self, Nome, CPF, Tel, Email, Endereço, Salário, CH, Código):
        self.Nome = str(Nome)
        self.CPF = str(CPF)
        self.Tel = int(Tel)
        self.Email = str(Email)
        self.Endereço = str(Endereço)
        self.Salário = float(Salário)
        self.CH = float(CH)
        self.Código = int(Código)

class Cliente:
    def __init__(self, Nome, CPF, Tel, Email, Endereço):
        self.Nome = str(Nome)
        self.CPF = str(CPF)
        self.Tel = int(Tel)
        self.Email = str(Email)
        self.Endereço = str(Endereço)

class Documentos:
    def __init__(self, Título, PubANO, Editora, Idioma, Disponibilidade):
        self.Título = str(Título)
        self.PubANO = int(PubANO)
        self.Editora = str(Editora)
        self.Idioma = str(Idioma)
        self.Disponibilidade = bool(Disponibilidade)

class Livros (Documentos):
    def __init__(self, Título, Autor, PubANO, Editora, Edição, Disponibilidade):
        super().__init__(Título, PubANO, Editora, Disponibilidade)
        self.Autor = str(Autor)
        self.Edição = int(Edição)
class Revistas (Documentos):
    def __init__(self, Título, PubANO, Editora, Idioma, Disponibilidade):
        super().__init__(Título, PubANO, Editora, Idioma, Disponibilidade)
class Jornais (Documentos):
    def __init__(self, Título, PubANO, Editora, Idioma, Disponibilidade):
        super().__init__(Título, PubANO, Editora, Idioma, Disponibilidade)
