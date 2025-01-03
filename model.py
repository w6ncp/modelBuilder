import json

class Model:
    def __init__(self, name:str = None, race = None, gender = None, class_type = None, portrait = None,
                number:int = None, seed:int = None):
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

