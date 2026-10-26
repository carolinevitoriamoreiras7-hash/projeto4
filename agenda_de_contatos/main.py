from contatos import (cadastrar_contato, consultar_contatos, pesquisar_contato, editar_contato, excluir_contato, ordenar_contatos, contar_contatos, listar_categorias, contatos_sem_email, listar_contatos_por_categoria)
from compromissos import (cadastrar_compromisso, consultar_compromissos, pesquisar_compromisso, editar_compromisso, cancelar_compromisso, ordenar_compromissos, listar_proximos_compromissos, contar_compromissos)

# Menu
while True:
    print("\n=== AGENDA DE CONTATOS ===")
    print("1 - Cadastrar contato")
    print("2 - Consultar contatos")
    print("3 - Pesquisar contato")
    print("4 - Editar contato")
    print("5 - Excluir contato")
    print("6 - Ordenar contatos")
    print("7 - Contar contatos")
    print("8 - Listar categorias")
    print("9 - Listar contatos sem e-mail")
    print("10 - Cadastrar compromisso")
    print("11 - Consultar compromissos")
    print("12 - Pesquisar compromisso")
    print("13 - Editar compromisso")
    print("14 - Cancelar compromisso")
    print("15 - Ordenar compromissos por data e horário")
    print("16 - Listar próximos compromissos")
    print("17 - Contar compromissos")
    print("18 - Listar contatos por categoria")
    print("0 - Encerrar")

    # Recebe a opção escolhida pelo usuário
    opcao = input("Escolha uma opção: ")

    # Executa a função correspondente à opção escolhida
    if opcao == "1":
        cadastrar_contato()

    elif opcao == "2":
        consultar_contatos()

    elif opcao == "3":
        pesquisar_contato()

    elif opcao == "4":
        editar_contato()

    elif opcao == "5":
        excluir_contato()

    elif opcao == "6":
        ordenar_contatos()

    elif opcao == "7":
        total = contar_contatos()
        print("Quantidade de contatos cadastrados:", total)

    elif opcao == "8":
        listar_categorias()

    elif opcao == "9":
        contatos_sem_email()

    elif opcao == "10":
        cadastrar_compromisso()

    elif opcao == "11":
        consultar_compromissos()

    elif opcao == "12":
        pesquisar_compromisso()

    elif opcao == "13":
        editar_compromisso()

    elif opcao == "14":
        cancelar_compromisso()

    # Organiza todos os compromissos por data e horário
    elif opcao == "15":
        ordenar_compromissos()

    # Mostra somente os compromissos futuros, em ordem
    elif opcao == "16":
        listar_proximos_compromissos()

    # Mostra a quantidade total de compromissos
    elif opcao == "17":
        total = contar_compromissos()
        print("Quantidade de compromissos cadastrados:", total)
    
    # Lista os contatos de uma categoria, sem repetir nomes
    elif opcao == "18":
        listar_contatos_por_categoria()

    # Encerra o programa
    elif opcao == "0":
        print("Programa encerrado!")
        break

    # Trata opções que não existem no menu
    else:
        print("Opção inválida!")
