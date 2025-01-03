import json, csv, os
import random

class Model:
    def __init__(self, name:str = "", race = None, gender = None, class_type = None, portrait = None,
                number:int = 0, seed:int = 0):
        self.__name = None
        self.__race = race
        self.__gender = gender
        self.__class_type = class_type
        self.__portait = portrait
        self.__number = number
        self.__seed = int(str(number) + str(seed))
        self.__model = {}
        self.__experience = 0

        random.seed(self.__seed)
        self.__name = self.update_name(name, True)


    def __repr__(self):
        out = {}
        for attr, value in self.__dict__.items():
            out[attr] = value
        return json.dumps(out)

    def import_model_type(self, model_file:str = None):
        while model_file is None:
            model_file = self.__request_file("Input path to useable JSON model template:")
            if model_file is None:
                print("No file path given.\n")
                continue
            if not model_file.lower().endswith(".json"):
                print(f"Invalid file type {model_file.split(".")[-1]} given.\n")
                continue
        self.__model["Template"] = model_file


    def __request_file(self, prompt:str = "File requested:"):
        print(prompt)
        cus_input = input(">>")
        cwd = os.getcwd()
        if os.path.exists(cus_input):
            return cus_input
        return None
    
    def __generate_name(self, name):
        if name is not None:
            return name
        first_names = []
        last_names = []
        with open("sources/names.csv") as names_file:
            names_lists = list(csv.reader(names_file,))
            first_names = names_lists[0][1:]
            last_names = names_lists[1][1:]
        first = str(random.choice(first_names))
        last = str(random.choice(last_names))
        return f"{first.title()} {last.title()}"
    
    def update_name(self, name:str = None, confirm:bool = False):
        if not confirm:
            choice = input("Confirm name change? Y/N: ")
            if choice.upper() == "Y":
                confirm = True
        
        if name is None and confirm:
                self.__name = self.__generate_name(None)
        elif confirm:
            self.__name = name
        print(f"Chacter name is {self.__name}.")
            
