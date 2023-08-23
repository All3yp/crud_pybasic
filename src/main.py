class Main:
    def menu(argument):
        switcher = {
            0: "Create",
            1: "Read",
            2: "Update",
            3: "Delete"
        }
        return switcher.get(argument, "Invalid option")
