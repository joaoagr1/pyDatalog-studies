from pyDatalog import pyDatalog

# Criando os predicados
pyDatalog.create_terms('colaborador, projeto, alocado, X, Y, Z')

# Lendo os arquivos e inserindo os fatos
with open('colaboradores.txt', 'r') as f:
    for line in f:
        line = line.strip().rstrip(';')
        try:
            nome, idade, setor = line.split(',')
            pyDatalog.assert_fact('colaborador', nome, int(idade), setor)
            print(f'Colaborador adicionado: {nome}, {idade}, {setor}')  # Linha de depuração
        except ValueError:
            print(f"Formato inválido na linha: {line}")

with open('projetos.txt', 'r') as f:
    for line in f:
        proj, setor = line.strip().split(',')
        pyDatalog.assert_fact('projeto', proj, setor)

with open('alocacoes.txt', 'r') as f:
    for line in f:
        colaborador_nome, projeto_nome = line.strip().split(',')
        pyDatalog.assert_fact('alocado', colaborador_nome, projeto_nome)

# Função para listar todos os colaboradores
def listar_colaboradores():
    q_colaboradores = pyDatalog.ask('colaborador(X, Y, Z)')  # Ajuste aqui
    if q_colaboradores:  # Verifica se a consulta retornou resultados
        return [sol[0] for sol in q_colaboradores.answers]
    return []  # Retorna lista vazia se não houver resultados

# Função para listar todos os projetos
def listar_projetos():
    q_projetos = pyDatalog.ask('projeto(X, _)')
    if q_projetos:  # Verifica se a consulta retornou resultados
        return [sol[0] for sol in q_projetos.answers]
    return []  # Retorna lista vazia se não houver resultados

# Função principal
def main():
    colaboradores = listar_colaboradores()
    projetos = listar_projetos()
    
    # Exibindo colaboradores
    print("Colaboradores:")
    if colaboradores:
        for col in colaboradores:
            print(col)
    else:
        print("Nenhum colaborador encontrado.")
    
    # Exibindo projetos
    print("\nProjetos:")
    for proj in projetos:
        print(proj)

if __name__ == "__main__":
    main()
