class Aluno:
    def __init__(self, nome, matricula):
        self._nome = nome
        self._matricula = matricula
        self._nomeCurso = ''
        self._nomeDisciplinas = []
        self._notasDisciplinas = []
    
    @property
    def nome(self):
        return self._nome
    
    @nome.setter
    def nome(self, nome):
        self._nome = nome
    
    @property
    def matricula(self):
        return self._matricula
    
    @matricula.setter
    def matricula(self,matricula):
        self._matricula = matricula
    
    @property
    def nomeCurso(self):
        return self._nomeCurso
    
    @nomeCurso.setter
    def nomeCurso(self, nomeCurso):
        self._nomeCurso = nomeCurso
    
    @property
    def nomeDisciplinas(self):
        return self.nomeDisciplinas

    @nomeDisciplinas.setter
    def nomeDisciplina(self, valor):
        self._nomeDisciplinas = valor
    
    @property
    def notasDisciplinas(self):
        return self._notasDisciplinas

    @notasDisciplinas.setter
    def notasDisciplinas(self, valor):
        self._notasDisciplinas = valor
