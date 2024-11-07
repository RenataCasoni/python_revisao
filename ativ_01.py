'''
 Como a função importar_dados() organiza os dados dos 
 arquivos colaboradores.txt, projetos.txt e alocacoes.txt?
 Explique os dicionários resultantes
'''


def importar_dados():
    # Dicionário para armazenar colaboradores com seu departamento
    colaboradores = {}
    # Dicionário para armazenar a idade dos colaboradores
    idades = {}
    
    # Abrindo e lendo o arquivo de colaboradores
    with open("colaboradores.txt", "r") as file:
        for line in file:
            nome, idade, departamento = line.strip().split(',')
            colaboradores[nome] = departamento   # Armazena o departamento do colaborador
            idades[nome] = int(idade)            # Armazena a idade do colaborador
    
    # Dicionário para armazenar projetos com seus respectivos departamentos
    projetos = {}
    with open("projetos.txt", "r") as file:
        for line in file:
            nome_projeto, departamento = line.strip().split(',')
            projetos[nome_projeto] = departamento
    
    # Dicionário para armazenar as alocações dos colaboradores em projetos
    alocacoes = {}
    with open("alocacoes.txt", "r") as file:
        for line in file:
            nome_colaborador, nome_projeto = line.strip().split(',')
            if nome_colaborador in alocacoes:
                alocacoes[nome_colaborador].append(nome_projeto)  # Adiciona projeto à lista
            else:
                alocacoes[nome_colaborador] = [nome_projeto]       # Cria lista com o primeiro projeto

    # Retorna os dicionários de dados
    return colaboradores, projetos, alocacoes, idades

# Chamada da função para importar dados
colaboradores, projetos, alocacoes, idades = importar_dados()

# Print para verificar se os dados foram importados corretamente
print("Colaboradores:", colaboradores)
print("Projetos:", projetos)
print("Alocações:", alocacoes)
print("Idades:", idades)

def ParticipaDe(nome_colaborador, nome_projeto):
    # Verifica se o projeto está na lista de alocações do colaborador
    return nome_projeto in alocacoes.get(nome_colaborador, [])

def DepartamentoColaborador(nome_colaborador, nome_departamento):
    # Compara o departamento do colaborador com o fornecido
    return colaboradores.get(nome_colaborador) == nome_departamento

def Senior(nome_colaborador):
    # Verifica se a idade do colaborador é maior que 30
    return idades.get(nome_colaborador, 0) > 30

def listar_colaboradores_projetos_departamentos():
    for colaborador, departamento in colaboradores.items():
        projetos_alocados = alocacoes.get(colaborador, [])
        print(f"Colaborador: {colaborador}")
        print(f"Departamento: {departamento}")
        print(f"Projetos: {', '.join(projetos_alocados) if projetos_alocados else 'Nenhum projeto alocado'}\n")


def listar_seniores_e_departamentos():
    for colaborador, idade in idades.items():
        if Senior(colaborador):
            departamento = colaboradores.get(colaborador, "Departamento não especificado")
            print(f"Nome: {colaborador}, Departamento: {departamento}")


def contar_seniores_por_departamento():
    contagem_por_departamento = {}
    for colaborador, idade in idades.items():
        if Senior(colaborador):
            departamento = colaboradores.get(colaborador, "Departamento não especificado")
            contagem_por_departamento[departamento] = contagem_por_departamento.get(departamento, 0) + 1
    for departamento, contagem in contagem_por_departamento.items():
        print(f"Departamento: {departamento}, Colaboradores Sêniores: {contagem}")

listar_colaboradores_projetos_departamentos()
listar_seniores_e_departamentos()
contar_seniores_por_departamento()


"""
colaboradores: Dicionário onde as chaves são nomes dos colaboradores e os valores são os departamentos.
projetos: Dicionário onde as chaves são nomes dos projetos e os valores são os departamentos aos quais pertencem.
alocacoes: Dicionário onde cada chave é o nome de um colaborador, e o valor é uma lista de projetos nos quais ele está alocado.
idades: Dicionário onde as chaves são os nomes dos colaboradores, e os valores são suas idades.

Usa alocacoes.get(nome_colaborador, []), que retorna a lista de projetos de um colaborador ou uma lista vazia caso o colaborador 
não exista no dicionário. A função retorna True se o projeto estiver na lista.

 Usa colaboradores.get(nome_colaborador), que retorna o departamento do colaborador. Compara com o valor de nome_departamento.

Usa idades.get(nome_colaborador, 0), que retorna a idade do colaborador ou 0 se não encontrado. Retorna True se a idade for maior que 30.
 
"""