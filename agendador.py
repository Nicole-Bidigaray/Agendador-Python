def adicionar_contato(contatos, nome, telefone, email):
    contatos[nome] = {"telefone": telefone, "email": email, "favorito": False}

def listar_contatos(contatos):
    for nome, info in contatos.items():
        favorito = "✅" if info["favorito"] else " "
        print(f"{nome} - Tel: {info['telefone']}, Email: {info['email']} [{favorito}]")

def editar_contato(contatos, nome, novo_nome, novo_telefone, novo_email):
    if nome in contatos:
        contatos[novo_nome] = {"telefone": novo_telefone, "email": novo_email, "favorito": contatos[nome]["favorito"]}
        if novo_nome != nome:
            del contatos[nome]

def marcar_favorito(contatos, nome):
    if nome in contatos:
        contatos[nome]["favorito"] = not contatos[nome]["favorito"]

def listar_favoritos(contatos):
    for nome, info in contatos.items():
        if info["favorito"]:
            print(f"{nome} - Tel: {info['telefone']}, Email: {info['email']}")

def apagar_contato(contatos, nome):
    if nome in contatos:
        del contatos[nome]

contatos = {}

while True:
    print("\nGerenciador de Contatos")
    print("1. Adicionar Contato")
    print("2. Listar Contatos")
    print("3. Editar Contato")
    print("4. Marcar/Desmarcar Favorito")
    print("5. Listar Favoritos")
    print("6. Apagar Contato")
    print("7. Sair")
    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome = input("Nome: ")
        telefone = input("Telefone: ")
        email = input("Email: ")
        adicionar_contato(contatos, nome, telefone, email)
    elif escolha == "2":
        listar_contatos(contatos)
    elif escolha == "3":
        nome_atual = input("Nome do contato a editar: ")
        novo_nome = input("Novo nome: ")
        novo_telefone = input("Novo telefone: ")
        novo_email = input("Novo email: ")
        editar_contato(contatos, nome_atual, novo_nome, novo_telefone, novo_email)
    elif escolha == "4":
        nome = input("Nome do contato para marcar/desmarcar como favorito: ")
        marcar_favorito(contatos, nome)
    elif escolha == "5":
        listar_favoritos(contatos)
    elif escolha == "6":
        nome = input("Nome do contato a apagar: ")
        apagar_contato(contatos, nome)
    elif escolha == "7":
        break

print("Programa finalizado.")
