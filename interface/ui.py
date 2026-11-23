from database.dragon_dao import DAO
from services.dragon_service import Service
from database.connection import get_db_connection
from entities.dragon import Dragon

class Ui:

    def __init__(self):

        self.MENU_OPTIONS = [
            (1, "Dragão", self.menu_dragons),
        ]

    def show(self):
        while True:
            print("\n===== Reino dos Dragões =====")

            # Exibe as opções dinamicamente
            for number, description, action in self.MENU_OPTIONS:
                print(f"{number} - {description}")

            print("0 - Sair")

            option = input("Escolha uma opção: ")

            if option == "0":
                print("Encerrando...")
                break

            selected = False

            for item in self.MENU_OPTIONS:
                if str(item[0]) == option:
                    item[2]()
                    selected = True
                    break
            
            if not selected:
                print("Opção inválida. Tente novamente.")

    def menu_dragons(self):
        connection = get_db_connection()
        dao = DAO(connection)
        service = Service(dao)
        
        while True:
            print("\n===== Reino dos Dragões =====")
            print("= Dragão ==")
            print("1 - Cadastrar Dragão")
            print("0 - Sair")
            
            opcao = int(input("\nUsuário: ").strip())
            if opcao == 0:
                break
            
            elif opcao == 1:
                lore = ""
                idade = 0
                voa = False
                tipo = "Fogo"
                
                while True:
                    l = input("\nLore do dragão: ").strip()
                    if l == "":
                        print("\nA lore não pode estar vazia.")
                    else:
                        lore = l
                        break
                while True:
                    try:
                        i = int(input("\nIdade do dragão: ").strip())
                    except:
                        print("\nDigite um número, e que seja maior que zero.")
                        continue
                        
                    if i < 0:
                        print("\nDigite uma idade válida.")
                    else:
                        idade = i
                        break
                        
                while True:
                    print("\nO Dragão é capaz de voar? ")
                    v = input(" (s/n)").lower().strip()
                    
                    if v == "s" or v == "sim":
                        voa = True
                        break
                    elif v == "n" or v == "não" or v == "nao":
                        voa = False
                        break
                    else:
                        print("\nDigite uma opção válida.")
                
                while True:
                    t = input("\nO Dragão é de gelo, água ou ar? ").lower().strip()
                    
                    if t == "gelo" or t == "fogo" or t == "ar":
                        tipo = t
                        break
                    else:
                        print("\nDigite um tipo válido.")
                
                dragon = Dragon(lore, idade, voa, tipo)
                service.create(dragon)
                    
            else:
                print("\nSelecione uma opção válida.")
                
                