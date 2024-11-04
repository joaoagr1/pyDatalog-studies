from pyDatalog import pyDatalog

# Criando os predicados
pyDatalog.create_terms('colaborador, projeto, alocado, X, I')

# Lendo os arquivos e inserindo os fatos
with open('colaboradores.txt', 'r') as f:
    for line in f:
        nome, idade, setor = line.strip().split(',')
        pyDatalog.assert_fact('colaborador', nome, int(idade), setor)

with open('projetos.txt', 'r') as f:
    for line in f:
        proj, setor = line.strip().split(',')
        pyDatalog.assert_fact('projeto', proj, setor)

with open('alocacoes.txt', 'r') as f:
    for line in f:
        colaborador_nome, projeto_nome = line.strip().split(',')
        pyDatalog.assert_fact('alocado', colaborador_nome, projeto_nome)

# Exemplos de consultas
# Quais colaboradores trabalham em Marketing?
q1 = pyDatalog.ask('colaborador(X, _, "Marketing")')
print("Colaboradores em Marketing:", [sol[0] for sol in q1.answers])

# Qual o projeto do Bruno?
q2 = pyDatalog.ask('alocado("Bruno", X)')
print("Projeto do Bruno:", [sol[0] for sol in q2.answers])

# Qual a idade média dos colaboradores de TI?
q3 = pyDatalog.ask('colaborador(X, I, "TI")')
idades_ti = [sol[1] for sol in q3.answers]  # Extrai as idades dos colaboradores de TI
idade_media = sum(idades_ti) / len(idades_ti) if idades_ti else 0
print("Idade média dos colaboradores de TI:", idade_media)
