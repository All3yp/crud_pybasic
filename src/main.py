class Main:
    def menu(argument):
        switcher = {
            0: "Create",
            1: "Read",
            2: "Update",
            3: "Delete"
        }
        return switcher.get(argument, "Invalid option")
    
    def main():
        print("Welcome to the CRUD application")
        try:
            while True:
                choice = int(input("0. Create\n1. Read\n2. Update\n3. Delete\n4. Exit\n"))
                result = menu(choice)
                if result != "Invalid option":
                    print("Redirecionar aqui pras funcoes do manager")
                else:
                     print("FODASE")
        except ValueError as e:
            print(f'Error: {e}')

