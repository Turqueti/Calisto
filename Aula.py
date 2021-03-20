class Aula():
    codDisciplina =  ''
    nomeDisciplina =  ''
    codTurma =  ''
    DiaInicio =  ''
    DiaFim =  ''
    TipoDaTurma =  ''
    Observacoes =  ''
    horarios =  []

    def print(self):
        print(self.codDisciplina,self.nomeDisciplina)
        print(self.codTurma,self.DiaInicio,self.DiaFim,self.TipoDaTurma,self.Observacoes,sep='\n')
        for horario in self.horarios:
            horario.print()
