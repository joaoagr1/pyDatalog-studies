from pyDatalog import pyDatalog

pyDatalog.create_terms('Funcionarios', 'Projetos', 'Departamentos', 'Alocacoes', 'Funcionario', 'Projeto',
                       'Departamento', 'X', 'Z', 'Y', 'Experiente', 'ExperienteDepartamento', 'TrabalhaEm',
                       'PertenceAoDepartamento', 'AAA')


with open('funcionarios.txt', 'r') as arquivo:
    for linha in arquivo:
        if linha.startswith("Nome"):
            continue;
        partes = linha.split(';')
        nome = partes[0].strip()
        departamento = partes[1].strip()
        anosExperiencia = int(partes[2].strip())
        +Funcionarios(nome, departamento, anosExperiencia)

with open('projetos.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split(';')
        nome = partes[0].strip()
        departamentoResponsavel = partes[1].strip()
        +Projetos(nome, departamentoResponsavel)


with open('departamentos.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split(';')
        nome = partes[0].strip()
        qtdFuncionarios = partes[1].strip()
        +Departamentos(nome, qtdFuncionarios)

with open('alocacoes.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split(';')
        nomeFuncionario = partes[0].strip()
        nomeProjeto = partes[1].strip()
        +Alocacoes(nomeFuncionario, nomeProjeto)

# ---------------------------------------------------------- Atividade 1
Funcionario(X) <= (Funcionarios(X, Y, Z))
funcionarios = Funcionario(X)

print("")
print("")
print('Nome dos Funcionários da questão 1')
print(funcionarios)

Projeto(Y) <= (Projetos(Y, Z))
projetos = Projeto(Y)

print("")
print("")
print('Nome dos Projetos da questão 1')
print(projetos)

Departamento(Z) <= (Departamentos(Z, Y))
departamentos = Departamento(Z)

print("")
print("")
print('Nome dos Departamentos da questão 1')
print(departamentos)

# ---------------------------------------------------------- Atividade 2
TrabalhaEm(Funcionario, Projeto) <= (Funcionarios(Funcionario, X, Z) & Projetos(Projeto, X)) #type: ignore

PertenceAoDepartamento(Funcionario, Departamento) <= (Funcionarios(Funcionario,X,Z) & Departamentos(Departamento,Z))

funcionariosProjetos = TrabalhaEm(Funcionario, Projeto)
funcionarioDepartamento = PertenceAoDepartamento(Funcionario, Departamento)


print("")
print("")

print("Relação Funcionário-Projeto questão 2 parte 1")
print(funcionariosProjetos)
print("")
print("")
print("")
print("Relação Funcionário-Departamento questão 2 parte 2")
print(funcionarioDepartamento)

# ---------------------------------------------------------- Atividade 3
 
print()
print()
print()
print()
Experiente(Funcionario) <= (Funcionarios(Funcionario, Y, Z) & (Z > 5))
ExperienteDepartamento(Funcionario, Departamento) <= (Funcionarios(Funcionario, Departamento, Z) & (Z > 5))

for n, d, a in Funcionarios(Funcionario, Departamento, Z):
    +AAA(d, len(ExperienteDepartamento(Y, d)))

print()
print("Atividade 3 - Funcionáerios experientes e seus departamentos:")
print(ExperienteDepartamento(X, Y))
print()
print()

print("Atividade 3 - Quantidade de funcionários experientes por departamento:")

print(AAA(X, Y))