# Importa a lista de contatos para relacionar os compromissos
from contatos import contatos

# Importa recursos para trabalhar com datas e horários
from datetime import datetime

# Lista que armazena os compromissos cadastrados
compromissos = []


def cadastrar_compromisso():
    print("\n--- CADASTRO DE COMPROMISSO ---")

    # Solicita os dados do compromisso
    titulo = input("Digite o título: ")
    data = input("Digite a data (DD/MM/AAAA): ")
    horario = input("Digite o horário (HH:MM): ")
    descricao = input("Digite a descrição: ")
    identificador = input("Digite o identificador do contato: ")

    # Verifica se o contato informado está cadastrado
    contato_encontrado = False

    for contato in contatos:
        if contato["identificador"] == identificador:
            contato_encontrado = True
            break

    # Impede o cadastro se o contato não existir
    if not contato_encontrado:
        print("Contato não encontrado!")
        return

    # Verifica se os campos obrigatórios estão vazios
    if titulo.strip() == "" or data.strip() == "" or horario.strip() == "" or identificador.strip() == "":
        print("Preencha todos os campos obrigatórios!")
        return


    # Guarda os dados do compromisso em um dicionário
    compromisso = {
        "titulo": titulo,
        "data": data,
        "horario": horario,
        "descricao": descricao,
        "identificador": identificador
    }

    # Adiciona o compromisso à lista
    compromissos.append(compromisso)
    print("Compromisso cadastrado com sucesso!")


def consultar_compromissos():
    print("\n--- LISTA DE COMPROMISSOS ---")

    # Verifica se existem compromissos cadastrados
    if len(compromissos) == 0:
        print("Nenhum compromisso cadastrado!")
        return

    # Exibe os dados dos compromissos
    for compromisso in compromissos:
        print("\nTítulo:", compromisso["titulo"])
        print("Data:", compromisso["data"])
        print("Horário:", compromisso["horario"])
        print("Descrição:", compromisso["descricao"])
        print("Identificador do contato:", compromisso["identificador"])


def pesquisar_compromisso():
    print("\n--- PESQUISAR COMPROMISSO ---")
    print("1 - Pesquisar por data")
    print("2 - Pesquisar por identificador do contato")

    # Solicita o tipo de pesquisa
    opcao = input("Escolha uma opção: ")

    # Define o campo que será pesquisado
    if opcao == "1":
        campo = "data"
    elif opcao == "2":
        campo = "identificador"
    else:
        print("Opção inválida!")
        return

    # Solicita o valor da pesquisa
    pesquisa = input("Digite o valor da pesquisa: ").strip()

    # Procura os compromissos correspondentes
    encontrado = False

    for compromisso in compromissos:
        if compromisso[campo] == pesquisa:
            print("\nTítulo:", compromisso["titulo"])
            print("Data:", compromisso["data"])
            print("Horário:", compromisso["horario"])
            print("Descrição:", compromisso["descricao"])
            print("Identificador do contato:", compromisso["identificador"])
            encontrado = True

    # Informa se nenhum compromisso foi encontrado
    if not encontrado:
        print("Nenhum compromisso encontrado!")


def editar_compromisso():
    print("\n--- EDITAR COMPROMISSO ---")

    # Solicita o título atual do compromisso
    titulo_atual = input("Digite o título do compromisso: ")

    # Procura o compromisso pelo título
    for compromisso in compromissos:
        if compromisso["titulo"] == titulo_atual:

            # Solicita o identificador do contato
            identificador = input("Digite o novo identificador do contato: ")

            # Verifica se o contato existe
            contato_encontrado = False

            for contato in contatos:
                if contato["identificador"] == identificador:
                    contato_encontrado = True
                    break

            # Impede a edição se o contato não existir
            if not contato_encontrado:
                print("Contato não encontrado!")
                return

            # Solicita os novos dados do compromisso
            titulo = input("Digite o novo título: ")
            data = input("Digite a nova data (DD/MM/AAAA): ")
            horario = input("Digite o novo horário (HH:MM): ")
            descricao = input("Digite a nova descrição: ")

           
            # Verifica os campos obrigatórios
            if titulo.strip() == "" or data.strip() == "" or horario.strip() == "":
                print("Preencha todos os campos obrigatórios!")
                return

            # Verifica se a data e o horário são válidos
            try:
                datetime.strptime(data + " " + horario, "%d/%m/%Y %H:%M")
            except ValueError:
                print("Data ou horário inválido! Use DD/MM/AAAA e HH:MM.")
                return


            # Atualiza os dados do compromisso
            compromisso["titulo"] = titulo
            compromisso["data"] = data
            compromisso["horario"] = horario
            compromisso["descricao"] = descricao
            compromisso["identificador"] = identificador

            print("Compromisso editado com sucesso!")
            return

    # Informa se o compromisso não existe
    print("Compromisso não encontrado!")


def cancelar_compromisso():
    print("\n--- CANCELAR COMPROMISSO ---")

    # Solicita o título do compromisso
    titulo = input("Digite o título do compromisso: ")

    # Procura o compromisso que será cancelado
    for compromisso in compromissos:
        if compromisso["titulo"] == titulo:

            # Remove o compromisso da lista
            compromissos.remove(compromisso)
            print("Compromisso cancelado com sucesso!")
            return

    # Informa se o compromisso não existe
    print("Compromisso não encontrado!")


def ordenar_compromissos():
    print("\n--- COMPROMISSOS ORDENADOS POR DATA E HORÁRIO ---")

    # Verifica se existem compromissos cadastrados
    if len(compromissos) == 0:
        print("Nenhum compromisso cadastrado!")
        return

    # Converte a data e o horário para permitir a ordenação
    compromissos_ordenados = sorted(
        compromissos,
        key=lambda compromisso: datetime.strptime(
            compromisso["data"] + " " + compromisso["horario"],
            "%d/%m/%Y %H:%M"
        )
    )

    # Exibe os compromissos em ordem cronológica
    for compromisso in compromissos_ordenados:
        print("\nTítulo:", compromisso["titulo"])
        print("Data:", compromisso["data"])
        print("Horário:", compromisso["horario"])
        print("Descrição:", compromisso["descricao"])
        print("Identificador do contato:", compromisso["identificador"])


def listar_proximos_compromissos():
    print("\n--- PRÓXIMOS COMPROMISSOS ---")

    # Obtém a data e o horário atuais
    agora = datetime.now()

    # Lista que armazenará os compromissos futuros
    proximos = []

    # Verifica quais compromissos ainda vão acontecer
    for compromisso in compromissos:
        data_horario = datetime.strptime(
            compromisso["data"] + " " + compromisso["horario"],
            "%d/%m/%Y %H:%M"
        )

        # Guarda apenas os compromissos futuros
        if data_horario > agora:
            proximos.append((data_horario, compromisso))

    # Ordena os próximos compromissos por data e horário
    proximos.sort(key=lambda item: item[0])

    # Exibe os compromissos futuros
    if len(proximos) == 0:
        print("Nenhum compromisso futuro encontrado!")
    else:
        for data_horario, compromisso in proximos:
            print("\nTítulo:", compromisso["titulo"])
            print("Data:", compromisso["data"])
            print("Horário:", compromisso["horario"])
            print("Descrição:", compromisso["descricao"])
            print("Identificador do contato:", compromisso["identificador"])


def contar_compromissos():
    # Retorna a quantidade de compromissos cadastrados
    return len(compromissos)