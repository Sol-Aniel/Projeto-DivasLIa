class Funcionários:
    def __init__(self, Nome, CPF, Tel, Email, Endereço, Salário, CH):
        self.Nome = str(Nome)
        self.CPF = str(CPF)
        self.Tel = int(Tel)
        self.Email = str(Email)
        self.Endereço = str(Endereço)
        self.Salário = float(Salário)
        self.CH = float(CH)
