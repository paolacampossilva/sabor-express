import os

restaurant_list = [{"name":"Subway", "category":"Lanche", "status":True}, 
                   {"name":"Bela Parmegiana", "category":"Prato feito", "status":False}]


def main():
    """Essa função limpa o console e exibi as informações presentes no menu principal, como: 
    
    - Nome do programa com a função show_program_name()
    - As opções de ações com a função show_options()
    - A escolha de opção com a função choose_option()

    """
    
    os.system("clear")
    show_program_name()
    show_options()
    choose_option()

if __name__ == "__main__":
    main()


def show_program_name():
    """Essa função exibi o nome do programa na tela"""

    print(""" 
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
""")


def show_options():
    """Essa função exibi as opções de ações para o usuário"""

    print("1. Cadastrar restaurante")
    print("2. Listar restaurantes")
    print("3. Alterar status do restaurante")
    print("4. Sair\n")


def choose_option():
    """Essa função recebe a opção escolhida pelo indivíduo com base na função show_options() e o redireciona para outra função correpondente a sua opção escolhida 
    
    Inputs:
    - A opção escolhida pelo usuário(chosen_option)

    Outputs:
    - Aciona outra função dependendo da opção escolhida

    """
    
    try:
        chosen_option = int(input("Escolha uma opção: "))

        if chosen_option == 1:
            register_new_restaurant()
        elif chosen_option == 2:
            show_restaurants()
        elif chosen_option == 3:
            change_restaurant_status()
        elif chosen_option ==4:
            end_app()
        else:
            invalid_option()
    except:
        invalid_option()

def register_new_restaurant():
    """Essa função é responsável por cadastrar um novo restaurante e é a opção 1 da função choose_option()
    
    Inputs:
    - Nome do resturante(restaurant_name)
    - Categoria(restaurant_category)

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    """
    
    show_title("Cadastro de novos restaurantes")
    
    restaurant_name = input("Digite o nome do restaurante que deseja cadastrar: ")
    restaurant_category = input(f"Digite o nome da categoria do restaurante {restaurant_name}: ")
    
    restaurant_data = {"name":restaurant_name, "category":restaurant_category, "status":False}
    
    restaurant_list.append(restaurant_data)
    print(f"O restaurante {restaurant_name} foi cadastrado com sucesso!")
    
    return_menu()

def show_restaurants():
    """Essa função exibi os restaurates presentes na lista de restaurantes e é a opção 2 da função choose_option()"""
    
    show_title("Listando os restaurantes")
    print(f"{"Nome do restaurante".ljust(22)} | {"Categoria".ljust(20)} | Status")
    
    for restaurant in restaurant_list:
        restaurant_name = restaurant["name"]
        restaurant_category = restaurant["category"]
        restaurant_status = "ativado" if restaurant["status"] else "desativado"
        print(f"- {restaurant_name.ljust(20)} | {restaurant_category.ljust(20)} | {restaurant_status}")

    return_menu()

def change_restaurant_status():
    """Essa função ativa ou desativa um restaurante selecionado e é a opção 3 da função choose_option()
    Inputs:
    - Nome do restaurante(restaurant_name)

    Outputs:
    - Inverte o valor booleano da categoria ["status"] do restaurante selecionado no dicionário {restaurant_list}

    """
    
    show_title("Alterando status do restaurante")
    
    restaurant_name = input("Digite o nome do restaurante que deseja alterar o status: ")
    restaurant_is_found = False

    for restaurant in restaurant_list:
        if restaurant_name == restaurant["name"]:
            restaurant_is_found = True
            restaurant["status"] = not restaurant["status"]
            message = f"O restaurante {restaurant_name} foi ativado com sucesso!" if restaurant["status"] else f"O restaurante {restaurant_name} foi desativado com sucesso!"
            print(message)
    
    if not restaurant_is_found:
        print("O restaurante não foi encontrado")

    return_menu()

def end_app():
    """Essa função realiza a opção 4 da função show_options(), que é sair do programa e encerra-lo"""

    show_title("Finalizando o app")

def invalid_option():
    """Essa função exibi uma mensagem de alerta e retorna para o menu principal caso o usuário não digite uma opção válida na função choose_option()"""

    print("\nOpção inválida!")
    return_menu()


def show_title(title):
    """Essa função limpa o console e exibi um título estilizado
    
    Parâmetros:
    - Título(title)

    """
    
    os.system("clear")
    line = "*" * len(title)
    print(line)
    print(title)
    print(line)
    print()

def return_menu():
    input("\nDigite enter para voltar para o menu principal ")
    main()
