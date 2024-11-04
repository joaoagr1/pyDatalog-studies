# Questão 2: Relações entre Colaboradores e Projetos

# 1 - Defina o predicado ParticipaDe(NomeColaborador, NomeProjeto) que indica quais colaboradores estão alocados em quais projetos.
# 2 - Defina o predicado DepartamentoColaborador(NomeColaborador, NomeDepartamento) que associa cada colaborador ao seu respectivo departamento.
# 3 - Liste todos os colaboradores, seus projetos e departamentos.

from pyDatalog import pyDatalog

pyDatalog.create_terms('Colaboradores', 'Projetos', 'Alocacoes', 'ParticipaDe', 'DepartamentoColaborador', 'X', 'Z', 'Y', 'NomeColaborador', 'NomeProjeto', 'NomeDepartamento')

with open('colaboradores.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split(',')
        nome = partes[0].strip()
        idade = partes[1].strip()
        departamento = partes[2].strip()
        +Colaboradores(nome, idade, departamento) #type: ignore
        
with open('projetos.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split(',')
        projeto = partes[0].strip()
        departamento = partes[1].strip()
        +Projetos(projeto, departamento) #type: ignore
        
with open('alocacoes.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split(',')
        teste = partes[0].strip()
        projeto = partes[1].strip()
        +Alocacoes(teste, projeto) #type: ignore
        

ParticipaDe(NomeColaborador, NomeProjeto) <= (Colaboradores(NomeColaborador, X, Z) & Projetos(NomeProjeto, Z)) #type: ignore
DepartamentoColaborador(NomeColaborador, NomeDepartamento) <= (Colaboradores(NomeColaborador, X, NomeDepartamento))  #type: ignore

participantes = ParticipaDe(NomeColaborador, NomeProjeto) #type: ignore
departamentos = DepartamentoColaborador(NomeColaborador, NomeDepartamento) #type: ignore

print(participantes)
print(departamentos)