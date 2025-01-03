import json, csv, os

class Model:
    def __init__(self, name:str = "", race = None, gender = None, class_type = None, portrait = None,
                number:int = 0, seed:int = 0):
        self.name = name
        self.race = race
        self.gender = gender
        self.class_type = class_type
        self.portait = portrait
        self.number = number
        self.seed = int(str(number) + str(seed))
        self.__model = {}
    
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
        if os.path.exists(cus_input):
            return cus_input
        else:
            return None