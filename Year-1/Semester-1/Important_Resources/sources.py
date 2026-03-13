import json
import os

class ResourcesManager:
    def __init__(self, file_name):
        self.file_name = file_name
        self.resources = []
        self.load_resources()

    def load_resources(self):
        try:
            with open(self.file_name, "r") as f:
                self.resources = json.load(f)

        except FileNotFoundError:
            print("HEHE NO FILE!")

    def save_resources(self):
        with open(self.file_name, "w") as f:
            json.dump(self.resources, f, indent=4)

    def clear_screen(self):
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')    

    def check_resources(self):
        print("\nHERE ALL OF YOUR IMPORTANT RESOURCES!")

        for i, t in enumerate(self.resources, 1):
            print(f"{i}. {t['name']}")
            print(f"{t['url']}")
            print(f"{t['type']}")



    def add_resources(self):
        self.clear_screen()
        print("OKay let's add!")
        name_resources = input("What is the name? ") 
        url_resources = input("What is the url? ") 
        type_resources = input("What is the type? ")
        print("SUCCESSFULLY ADDED!")

        self.resources.append(
            {
                "name": name_resources,
                "url": url_resources,
                "type": type_resources
            }
        )
        self.save_resources()
        print("okay na, na add kona lods!")


    def remove_resources(self):
        self.clear_screen()
        print("Okay let's remove some resources!")
        num = int(input("INPUT THE NUMBER U WANT TO REMOVE: "))
        print("SUCCESSFULLY REMOVED!")

        if 0 < num <=len(self.resources):
            self.resources.pop()
            self.save_resources()
    
    def exit():
        global ran
        print("THANK YOU SO MUCH!")
        ran = False


FILE_RESOURCES = "resources.json"
resources_manager = ResourcesManager(FILE_RESOURCES)
ran = True
while ran:
    print("\nCHOOSE ONE 1")
    print("[1] Check Resources")
    print("[2] Add Resources")
    print("[3] Remove Resources")
    print("[4] EXIT")

    choice = input("HERE: ")

    if choice == "1":
        resources_manager.check_resources()
    if choice == "2":
        resources_manager.add_resources()
    if choice == "3":
        resources_manager.remove_resources()
    if choice == "4":
        exit()


