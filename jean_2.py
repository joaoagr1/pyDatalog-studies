# Questão 3: Identificação de Colaboradores Sêniores

# 1 - Defina o predicado Senior(Nome) para identificar colaboradores com idade maior que 30 anos.
# 2 - Liste todos os colaboradores sêniores e o departamento ao qual pertencem.
# 3 - Conte quantos colaboradores sêniores há em cada departamento e exiba essa informação.

from pyDatalog import pyDatalog

pyDatalog.create_terms('AAA, Colaboradores', 'Projetos', 'Alocacoes', 'ParticipaDe', 'SeniorDepartamento', 'X', 'Z', 'Y', 'NomeColaborador', 'NomeProjeto', 'NomeDepartamento', 'Senior')

with open('colaboradores.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split(',')
        nome = partes[0].strip()
        idade = int(partes[1].strip())
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
        

Senior(NomeColaborador) <= (Colaboradores(NomeColaborador, X, Z) & (X > 30)) #type: ignore
SeniorDepartamento(NomeColaborador, NomeDepartamento) <= (Colaboradores(NomeColaborador, X, NomeDepartamento) & (X > 30))

participantes = Senior(NomeColaborador) #type: ignore
departamentos = SeniorDepartamento(NomeColaborador, NomeDepartamento)

for c, i, d in Colaboradores(NomeColaborador, X, NomeDepartamento):
    +AAA(d, len(SeniorDepartamento(Y, d)))    

print(Colaboradores(X,Y,Z))
print(AAA(X, Y))