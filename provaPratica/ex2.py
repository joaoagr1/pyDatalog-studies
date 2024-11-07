from pyDatalog import pyDatalog

pyDatalog.create_terms('Funcionarios', 'Projetos', 'Departamentos', 'Alocacoes','TrabalhaEm','PertenceAoDepartamento','Funcionario','Projeto','X','Z','Departamento')


with open('funcionarios.txt', 'r') as arquivo:
    for linha in arquivo:
        partes = linha.split(';')
        nome = partes[0].strip()
        departamento = partes[1].strip()
        anosExperiencia = partes[2].strip()
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



TrabalhaEm(Funcionario, Projeto) <= (Funcionarios(Funcionario, X, Z) & Projetos(Projeto, X)) #type: ignore

PertenceAoDepartamento(Funcionario, Departamento) <= (Funcionarios(Funcionario,X,Z) & Departamentos(Departamento,Z))

funcionariosProjetos = TrabalhaEm(Funcionario, Projeto)
funcionarioDepartamento = PertenceAoDepartamento(Funcionario, Departamento)

print(funcionariosProjetos)
print("=====================================================")
print(funcionarioDepartamento)

