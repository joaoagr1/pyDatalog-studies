# Questão 1: Listagem de Colaboradores e Projetos

# 1 - Defina os seguintes predicados:
# - Colaborador(Nome): lista todos os colaboradores.
# - Projeto(Nome): lista todos os projetos.
# 2 - Exiba o nome de todos os colaboradores e todos os projetos.

from pyDatalog import pyDatalog

pyDatalog.create_terms('Colaboradores', 'Projetos', 'Alocacoes', 'Colaborador', 'Projeto','NomeColaborador','X','Z','NomeProjeto')


with open('colaboradores.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split(',')
        nome = partes[0].strip()
        idade = partes[1].strip()
        departamento = partes[2].strip()
        +Colaboradores(nome, idade, departamento) #type: ignore criando fato


with open('projetos.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split(',')
        nome = partes[0].strip()
        departamento = partes[1].strip()
        +Projetos(nome, departamento) #type: ignore criando fato



with open('alocacoes.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split(',')
        nomeColaborador = partes[0].strip()
        projeto = partes[1].strip()
        +Alocacoes(nomeColaborador, projeto) #type: ignore criando fato


Colaborador(NomeColaborador) <= (Colaboradores(NomeColaborador,X,Z))
colaboradores = Colaborador(NomeColaborador)


print(colaboradores)

Projeto(NomeProjeto) <= (Projetos(NomeProjeto,X))
projetos = Projeto(NomeProjeto)

print(projetos)



