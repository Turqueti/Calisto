import datetime
from Aula import Aula
from Horario import Horario

diasDaSemana = {
    'seg': 0,
    'ter': 1,
    'qua': 2,
    'qui': 3,
    'sex': 4,
    'sab': 5,
    'dom': 6
}

def csvAula(Aula):

    nomeEvento = '\"' + Aula.codDisciplina + '-' + Aula.nomeDisciplina + '\"'
    infos = '\"' + 'Código da Turma:' + Aula.codTurma + '\nTipo da Turma:' + Aula.TipoDaTurma + '\nobservações: ' +  Aula.Observacoes

    for horario in Aula.horarios:
        datas = DatasHorario(horario,Aula.DiaInicio,Aula.DiaFim)
        for data in datas:
            print(nomeEvento + ',' + str(data) + ',' + horario.HrInicio + ',' + str(data) + ',' + horario.HrFim + ',' + infos + '\nProfessor: ' + horario.Prof + '\"' )

    pass

# retorna todos as datas que a aula acontece no horario passado como parametro
def DatasHorario(Horario,comecoAulas,FimAulas):
    datas = []
    data = PrimeiraOcorrenciaDiaDaSemana(comecoAulas,Horario.diaSemana)

    while data <= DateStrToDateObj(FimAulas):
        datas.append(data)
        data += datetime.timedelta(weeks=1)
    
    return datas

# retorna a data da primeira ocorrencia do dia da semana no periodo letivo
def PrimeiraOcorrenciaDiaDaSemana(dataInicio,DiaDaSemana):
    dataInicioDate = DateStrToDateObj(dataInicio)

    while dataInicioDate.weekday() != diasDaSemana[DiaDaSemana]:
        dataInicioDate += datetime.timedelta(days=1)
    


    return dataInicioDate

def DateStrToDateObj(data):
    data = data.split("/")
    day = data[0]
    month = data[1]
    year = data[2]
    

    retData = datetime.date(int(year),int(month),int(day))
    
    return retData
