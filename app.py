def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
  contato = {"nome": nome_contato, "telefone": telefone_contato, "email": email_contato, "favorito": False}
  contatos.append(contato)
  print(f"Contato {nome_contato} foi adicionado com sucesso!")
  return

def ver_contatos(contatos):
  print("Lista de contatos:")
  for indice, contato in enumerate(contatos, start=1):
    favorito = " ★ " if contato["favorito"] else "   "
    nome_contato = contato["nome"]
    telefone_contato = contato["telefone"]
    email_contato = contato["email"]
    print(f"{indice}. [{favorito}] {nome_contato} | Telefone: {telefone_contato} | Email: {email_contato}")
  return

def editar_contato(contatos, indice_contato, chave, novo_dado):
  indice_contato_ajustado = int(indice_contato) - 1
  contatos[indice_contato_ajustado][chave] = novo_dado
  print(f"Contato {contatos[indice_contato_ajustado]['nome']} atualizado com sucesso!")
  return

def favoritar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  contatos[indice_contato_ajustado]["favorito"] = not contatos[indice_contato_ajustado]["favorito"]
  print(f"Contato {contatos[indice_contato_ajustado]['nome']} foi atualizado!")
  return

def ver_contatos_favoritos(contatos):
  lista_favoritos = []
  for contato in contatos:
    if contato["favorito"]:
      lista_favoritos.append(contato)  
  ver_contatos(lista_favoritos)
  return

def apagar_contato(contatos, indice_contato):
  indice_contato_ajustado = int(indice_contato) - 1
  print(f"O contato {contatos[indice_contato_ajustado]['nome']} foi deletado com sucesso!")
  contatos.remove(contatos[indice_contato_ajustado])
  return

contatos = []

while True: 
  print("\n************* Agenda *************")
  print("1. Adicionar um contato")
  print("2. Visualizar os contatos")
  print("3. Editar um contato")
  print("4. Adicionar ou remover contato como favorito")
  print("5. Ver lista de contatos favoritos")
  print("6. Apagar um contato")
  print("7. Sair")

  escolha = input("Digite a sua escolha: ")

  if(escolha == "1"):
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o email: ")
    adicionar_contato(contatos, nome, telefone, email)

  if(escolha == "2"):
    ver_contatos(contatos)

  if(escolha == "3"):
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja atualizar: ")
    chave = input("Digite a informação que deseja atualizar (nome, telefone, email): ")
    novo_dado = input("Digite o novo dado: ")
    editar_contato(contatos, indice_contato, chave, novo_dado)

  if(escolha == "4"):
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja favoritar/desfavoritar: ")
    favoritar_contato(contatos, indice_contato)

  if(escolha == "5"):
    ver_contatos_favoritos(contatos)

  if(escolha == "6"):
    ver_contatos(contatos)
    indice_contato = input("Digite o número do contato que deseja apagar: ")
    apagar_contato(contatos, indice_contato)

  if(escolha == "7"):
    break

print("Programa finalizado")