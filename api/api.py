from flask import Flask, request, make_response
from io import StringIO
import sys
import os
import csv

app = Flask(__name__, template_folder='templates')

# CONSULTA 1 --> REVISAR E TESTAR
# Número de publicações em uma determinada conferência de uma área
@app.route('/numeroPubsConferenciaDeUmaArea/<string:conferencia>/<string:area>')
def numeroPubsConferenciaDeUmaArea(conferencia, area):
    filename = "../data/" + area + "-out-confs.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data:
            if(row[0] == conferencia):
                DATA.append(row)  # return str(row[1])

    with open('Resultado_nPub_'+conferencia+'_'+area+'.csv', 'w') as csvfile:
        header = ['Conferencia da area ' +
                  area, 'Quantidade de publicacoes']
        writer = csv.DictWriter(
            csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames=header)
        writer.writeheader()
        for row in DATA:
            writer.writerow(
                {'Conferencia da area ' + area: row[0], 'Quantidade de publicacoes': row[1]})
    return 'ARQUIVO GERADO'

# CONSULTA 2 --> REVISAR E TESTAR
# Número de publicações no conjunto de conferências de uma área
@app.route('/numeroPubliNoConjuntoDeConferenciasDeUmaArea/<area>')
def numeroPubliNoConjuntoDeConferenciasDeUmaArea(area):
    contPublicacoes = 1

    filename = "../data/" + area + "-out-papers.csv"
    with open(filename, 'r') as file:
        data = csv.DictReader(file, delimiter=';', quotechar='|')
        for row in data:
            contPublicacoes = contPublicacoes + 1
    return str(contPublicacoes)


# CONSULTA 3 --> REVISAR E TESTAR
# Scores de todos os departamentos em uma área
@app.route('/scoresDepartamentosDaArea/<string:area>')
def scoresDepartamentosDaArea(area):
    filename = "../data/" + area + "-out-scores.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data:
            DATA.append(row)
    with open('scoresDepartamentos_'+area+'.csv', 'w') as csvfile:
        header = ['Departamento da area ' + area, 'Score']
        writer = csv.DictWriter(
            csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames=header)
        writer.writeheader()
        for row in DATA:
            writer.writerow({'Departamento da area ' +
                             area: row[0], 'Score': row[1]})
    return 'ARQUIVO GERADO'

# CONSULTA 4 --> REVISAR E TESTAR
# Score de um determinado departamento em uma área.
@app.route('/scoreDeUmDepartamentoEmUmaArea/<departamento>/<area>')
def scoreDeUmDepartamentoEmUmaArea(departamento, area):
    filename = "../data/" + area + "-out-scores.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data:
            if(row[0] == departamento):
                DATA.append(row[1])

    with open('score_' + departamento + '_' + area +'.csv', 'w') as csvfile:
        header = ['Departamento', 'Score']
        writer = csv.DictWriter(
            csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames=header)
        writer.writeheader()
        for row in DATA:
            writer.writerow(
                {'Departamento': departamento, 'Score': row})
    return 'ARQUIVO GERADO'

# CONSULTA 5 --> REVISAR E TESTAR
# Número de professores que publicam em uma determinada área (organizados por departamentos)
@app.route('/numeroProfsPorArea/<string:area>')
def numeroProfsPorArea(area):
    filename = "../data/" + area + "-out-profs.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data:
            DATA.append(row)

    with open('numeroProfsPorArea'+area+'.csv', 'w') as csvfile:
        header = ['Departamento da area ' + area, 'Numero de professores']
        writer = csv.DictWriter(
            csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames=header)
        writer.writeheader()
        for row in DATA:
            writer.writerow({'Departamento da area ' +
                             area: row[0], 'Numero de professores': row[1]})
    return 'ARQUIVO GERADO'

# CONSULTA 6 --> REVISAR E TESTAR
# Número de professores de um determinado departamento que publicam em uma área
@app.route('/numeroProfsDepartamentoPublicaramEmUmaArea/<departamento>/<area>')
def numeroProfsDepartamentoPublicaramEmUmaArea(departamento, area):
    filename = "../data/" + area + "-out-profs.csv"
    with open(filename, 'r') as file:
        profs = []
        data = csv.reader(file)
        for row in data:
            if(row[0] == departamento):
                profs.append(row[1])
    with open('profs_'+departamento+'.csv', 'w') as csvfile:
        header = ['Departamento', 'N de Professores']
        writer = csv.DictWriter(
            csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames=header)
        writer.writeheader()
        for row in profs:
            writer.writerow(
                {'Departamento': departamento, 'N de Professores': row})#sem mostrar a coluna de departamento
    return 'ARQUIVO GERADO'

# CONSULTA 7 --> REVISAR E TESTAR
# Todos os papers de uma área (ano, título, deptos e autores)
@app.route('/papersDeUmaArea/<string:area>')
def papersDeUmaArea(area):
    filename = "../data/" + area + "-out-papers.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data:
            DATA.append(row)

    with open('papers_'+area+'.csv', 'w') as csvfile:
        header = ['Ano', 'Titulo', 'Departamento', 'Autores']
        writer = csv.DictWriter(
            csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames=header)
        writer.writeheader()
        for row in DATA:
            writer.writerow(
                {'Ano': row[0], 'Titulo': row[2], 'Departamento': row[3], 'Autores': row[4]})#sem mostrar a coluna de departamento
    return 'ARQUIVO GERADO'

# CONSULTA 8 --> REVISAR E TESTAR
# Todos os papers de uma área em um determinado ano
@app.route('/papersDeUmaAreaDeterminadoAno/<ano>/<area>')
def papersDeUmaAreaDeterminadoAno(ano, area):
    filename = "../data/" + area + "-out-papers.csv"
    papers = []
    with open(filename, 'r') as file:
        data = csv.reader(file)
        for row in data:
            if(row[0] == ano):
                papers.append(row[2])
    si = StringIO()
    cw = csv.writer(si, quoting=csv.QUOTE_ALL)
    cw.writerow(papers)
    output = make_response(si.getvalue())
    return output

# CONSULTA 9 --> REVISAR E TESTAR
# Todos os papers de um departamento em uma área
@app.route('/papersDepartamentoEmUmaArea/<string:departamento>/<string:area>')
def papersDepartamentoEmUmaArea(departamento, area):
    filename = "../data/" + area + "-out-papers.csv"
    with open(filename, 'r') as file:
        DATA = []
        data = csv.reader(file)
        for row in data:
            if(row[1] == departamento):
                DATA.append(row)
    with open('papers_'+departamento+'_'+area+'.csv', 'w') as csvfile:
        header = ['Departamento da area ' + area, 'Paper']
        writer = csv.DictWriter(
            csvfile, delimiter=';', quotechar='|', quoting=csv.QUOTE_MINIMAL, fieldnames=header)
        writer.writeheader()
        for row in DATA:
            writer.writerow({'Departamento da area ' +
                             area: row[1], 'Paper': row[2]})
    return 'ARQUIVO GERADO'

# CONSULTA 10 --> REVISAR E TESTAR
# Todos os papers de um professor (dado o seu nome)
@app.route('/todosPapersDeUmProfessor/<string:nomeProfessor>')
def todosPapersDeUmProfessor(nomeProfessor):
    filename = "../data/profs/search/" + nomeProfessor + ".csv"
    papers = []
    with open(filename, 'r') as file:
        data = csv.reader(file)
        for row in data:
            papers.append(row[2])
    si = StringIO()
    cw = csv.writer(si, quoting=csv.QUOTE_ALL)
    cw.writerow(papers)
    output = make_response(si.getvalue())
    return output

# PRINCIPAL
if __name__ == '__main__':
    app.run(debug=True)
