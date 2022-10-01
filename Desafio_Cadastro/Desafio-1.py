#TESTAR COM LISTA DENTRO DO WHILE, AO SAIR OS IDS VÃO VOLTAR AO NORMAL, SOMENTE PARA TESTES.

# while selec != 6: ##IRÁ SAIR SOMENTE SE DIGITAR 6, QUALQUER OUTRO NÚMERO FORA DO RANGE NÃO IMPRIMIRIA ERRO. EX: 7

users = [[0,True,["Ivisson César", "9898181-8181", "Av. 1 - São Luís" ] ], [1, True,["Davi Nascimento", "9898485-8586", "Est. 10 - Pará"]], 
            [2, True,["Kátia Fonseca", "9898145-4545", "Av. 0 - Turu"]], [3, True,["Barbosa Matos", "9894545-7845", "Quadra 12 - Paço"]], 
              [4, True,["Marcos Castro", "9898586-7866", "Travessa 20 - Açailândia"]]]
while True:
  
  selec = int(input("""Boas vindas ao nosso sistema:
  1 - Inserir usuário
  2 - Excluir usuário
  3 - Atualizar usuário
  4 - Informações de um usuário
  5 - Informações de todos os usuários
  6 - Sair\n"""))
  
  if selec == 1:
    nome = input("Digite seu nome: ")
    telefone = input("Digite seu telefone no formato (00)90000-0000: ")
    while len(telefone) != 11:
      print("Número inválido digite novamente.")
      telefone = input("Digite seu telefone no formato (00)90000-0000: ")
    endereco = input("Digite seu endereço: ")
    alocar = len(users) + 1
    users.append([alocar, True,[nome,telefone,endereco]])
                    ##PRINTA OS DADOS DO ID QUE FOI ADICIONADO
    print("*"*20)
    print("\nUsuário: ", nome,"\nID: ", len(users), "\nTelefone: ",telefone ,
    "\nEndereço: ", endereco, "\nFoi adicionado com sucesso!")
    print()
    print("*"*20)
    selec == 0 ##DEVOLVE O 0 PARA SELEC 

  elif selec == 2:
    exclui_id = int(input("Digite um ID: "))
    while (exclui_id > len(users)):
      print("Usuário não encontrado!")
      exclui_id = int(input("Digite um ID: "))
    users[exclui_id][1] = False
                    ##PRINTA OS DADOS DO ID QUE FOI EXCLUÍDO
    print("*"*20)
    print("O Usuário: ", users[exclui_id][2][0], "\nID: ", exclui_id,
                 "\nTelefone: ",users[exclui_id][2][1] ,
                        "\nEndereço: ", users[exclui_id][2][2], 
                                "\nFoi excluído com sucesso!")
    print()
    print("*"*20)
    print()
    print(users) #Para verificar 
     
    selec == 0

  elif selec == 3:
    atualiza_id = int(input("Digite o ID do usuário que deseja atualizar: "))
    while atualiza_id > len(users):
      print("Usuário não encontrado!")
      atualiza_id = int(input("Digite o ID do usuário que deseja atualizar: "))
    alterador = int(input("Qual informação deseja alterar? \n1 - Nome \n2 - Telefone \n3 - Endereço"))
    if alterador == 1:
      users[atualiza_id][2][0] = input("Insira o nome:")
        ##JOGA O NOME PARA A LISTA NA POSIÇÃO ATUALIZA_ID INFORMADA
    elif alterador == 2:
      users[atualiza_id][2][1] = input("Insira o telefone nesse formato (00)99999-9999: ")
      while len(users[atualiza_id][2][1]) != 11:
        print("Número inválido digite novamente.")
        users[atualiza_id][2][1] = input("Insira o telefone nesse formato (00)99999-9999: ")
    elif alterador == 3:
      users[atualiza_id][2][2] = input("Insira o endereço: ")
    print(users)  
    selec == 0

  elif selec == 4:
    info_user = int(input("Insira o ID do usuário: "))
    while info_user > len(users):
      print("Usuário não encontrado!")
      info_user = int(input("Insira o ID do usuário: "))
    print()
    print("*"*20)
    print("Usuário:", users[info_user][2][0], "\nID:", users[info_user][0], "\nTelefone:", users[info_user][2][1] ,"\nEndereço:", users[info_user][2][2])
    print("*"*20)
    selec == 0

  elif selec == 5: 
    #NÃO FOI ESPECÍFICADO SE SERIAM APENAS OS USUÁRIOS ATIVOS, INCLUI TODOS.
    for i in range (len(users)):
      for j in range(len(users[i][2])):
        if j == 0:
            print()
            print("*"*20)
            print(f"Dados do usuário ID: {i}")
            print("Nome: ", users[i][2][j])
        if j == 1:
            print("Telefone: ", users[i][2][j])
        if j == 2:
            print("Endereço: ", users[i][2][j])
            print("*"*20)
            print()
    selec == 0

  elif selec == 6:
    break
  else:
    print("Alternativa inválida, digite novamente.")
    continue
