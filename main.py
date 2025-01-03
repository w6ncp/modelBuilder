# generic imports
import json

# file imports
from model import Model

def main():
    testing = Model(seed=1234,number=0)
    print(testing)
    testing.update_name("Test Character")
    print(testing)
    testing.update_name()
    testing.import_model_type("source/scdwic_template.json")
    print(testing)

main()
