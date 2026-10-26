# Lista que armazena os contatos cadastrados
contatos = []


# Procura um contato pelo identificador e retorna o resultado
def buscar_contato_por_identificador(identificador):
    # Percorre a lista de contatos
    for contato in contatos:
        if contato["identificador"] == identificador:
            return contato

    # Retorna None quando não encontra o contato
    return None

def cadastrar_contato():
    print("\n--- CADASTRO DE CONTATO ---")

    # Solicita os dados do contato
    identificador = input("Digite o identificador: ")
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    categoria = input("Digite a categoria: ")

    # Verifica se os campos obrigatórios estão vazios
    if identificador.strip() == "" or nome.strip() == "" or telefone.strip() == "" or categoria.strip() == "":
        print("Preencha todos os campos obrigatórios!")
        return

    # Impede o cadastro de identificadores repetidos
    for contato in contatos:
        if contato["identificador"] == identificador:
            print("Já existe um contato com esse identificador!")
            return

    # Guarda os dados em um dicionário
    contato = {
        "identificador": identificador,
        "nome": nome,
        "telefone": telefone,
        "email": email,
        "categoria": categoria
    }

    # Adiciona o contato à lista
    contatos.append(contato)
    print("\nContato cadastrado com sucesso!")


def consultar_contatos():
    print("\n--- LISTA DE CONTATOS ---")

    # Verifica se existem contatos cadastrados
    if len(contatos) == 0:
        print("Nenhum contato cadastrado!")
        return

    # Exibe os dados de cada contato
    for contato in contatos:
        print("\nIdentificador:", contato["identificador"])
        print("Nome:", contato["nome"])
        print("Telefone:", contato["telefone"])
        print("E-mail:", contato["email"])
        print("Categoria:", contato["categoria"])


def pesquisar_contato():
    print("\n--- PESQUISAR CONTATO ---")
    print("1 - Pesquisar por nome")
    print("2 - Pesquisar por telefone")
    print("3 - Pesquisar por e-mail")
    print("4 - Pesquisar por categoria")

    # Solicita o tipo de pesquisa
    opcao = input("Escolha uma opção: ")

    # Define qual campo será pesquisado
    if opcao == "1":
        campo = "nome"
    elif opcao == "2":
        campo = "telefone"
    elif opcao == "3":
        campo = "email"
    elif opcao == "4":
        campo = "categoria"
    else:
        print("Opção inválida!")
        return

    # Solicita o termo da pesquisa
    pesquisa = input("Digite o que deseja pesquisar: ").lower()

    # Procura contatos que correspondem à pesquisa
    encontrado = False

    for contato in contatos:
        if pesquisa in contato[campo].lower():
            print("\nIdentificador:", contato["identificador"])
            print("Nome:", contato["nome"])
            print("Telefone:", contato["telefone"])
            print("E-mail:", contato["email"])
            print("Categoria:", contato["categoria"])
            encontrado = True

    # Informa se nenhum contato foi encontrado
    if not encontrado:
        print("Nenhum contato encontrado!")



def editar_contato():
    print("\n--- EDITAR CONTATO ---")

    # Solicita o identificador do contato
    identificador = input("Digite o identificador do contato: ")

    # Busca o contato usando a função auxiliar
    contato = buscar_contato_por_identificador(identificador)

    # Verifica se o contato existe
    if contato is None:
        print("Contato não encontrado!")
        return

    # Solicita os novos dados
    nome = input("Digite o novo nome: ")
    telefone = input("Digite o novo telefone: ")
    email = input("Digite o novo e-mail: ")
    categoria = input("Digite a nova categoria: ")

    # Verifica os campos obrigatórios
    if nome.strip() == "" or telefone.strip() == "" or categoria.strip() == "":
        print("Preencha todos os campos obrigatórios!")
        return

    # Atualiza os dados do contato
    contato["nome"] = nome
    contato["telefone"] = telefone
    contato["email"] = email
    contato["categoria"] = categoria

    print("Contato editado com sucesso!")


def excluir_contato():
    print("\n--- EXCLUIR CONTATO ---")

    # Solicita o identificador do contato
    identificador = input("Digite o identificador do contato: ")

    # Busca o contato usando a função auxiliar
    contato = buscar_contato_por_identificador(identificador)

    # Verifica se o contato existe
    if contato is None:
        print("Contato não encontrado!")
        return

    # Remove o contato encontrado
    contatos.remove(contato)
    print("Contato excluído com sucesso!")


def ordenar_contatos():
    print("\n--- CONTATOS EM ORDEM ALFABÉTICA ---")

    # Ordena os contatos pelo nome
    contatos_ordenados = sorted(contatos, key=lambda contato: contato["nome"].lower())

    # Exibe os contatos ordenados
    for contato in contatos_ordenados:
        print(contato["nome"], "-", contato["telefone"])


def contar_contatos():
    # Retorna a quantidade de contatos cadastrados
    return len(contatos)

def listar_categorias():
    print("\n--- CATEGORIAS CADASTRADAS ---")

    # Cria uma lista para armazenar categorias sem repetição
    categorias = []

    # Adiciona cada categoria apenas uma vez
    for contato in contatos:
        categoria = contato["categoria"]

        if categoria.lower() not in [c.lower() for c in categorias]:
            categorias.append(categoria)

    # Exibe as categorias encontradas
    if len(categorias) == 0:
        print("Nenhuma categoria cadastrada!")
    else:
        for categoria in categorias:
            print(categoria)


def contatos_sem_email():
    print("\n--- CONTATOS SEM E-MAIL ---")

    # Verifica se existem contatos sem e-mail
    encontrado = False

    for contato in contatos:
        if contato["email"].strip() == "":
            print("\nIdentificador:", contato["identificador"])
            print("Nome:", contato["nome"])
            print("Telefone:", contato["telefone"])
            print("Categoria:", contato["categoria"])
            encontrado = True

    # Informa se todos os contatos possuem e-mail
    if not encontrado:
        print("Nenhum contato sem e-mail encontrado!")


def listar_contatos_por_categoria():
    print("\n--- CONTATOS POR CATEGORIA ---")

    # Solicita a categoria desejada
    categoria = input("Digite a categoria: ")

    # Lista que armazenará os nomes sem repetição
    nomes = []

    # Procura os contatos da categoria escolhida
    for contato in contatos:
        if contato["categoria"].lower() == categoria.lower():

            # Evita nomes repetidos, mesmo com letras diferentes
            if contato["nome"].lower() not in [n.lower() for n in nomes]:
                nomes.append(contato["nome"])

    # Exibe os nomes encontrados
    if len(nomes) == 0:
        print("Nenhum contato encontrado nessa categoria!")
    else:
        # Organiza os nomes em ordem alfabética
        nomes.sort(key=str.lower)

        for nome in nomes:
            print(nome)