import os
import json

def get_list() -> dict:
    path = "alphabets/"
    
    abc_list = {}

    for abc in os.listdir(path):
        if not abc.startswith("_"): # ignoring examples
            abc_path = path + abc
            
            with open(abc_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            meta = data["meta"]
            abc_list.update({meta["name"]: {"description": meta["description"], "abc": data["abc"]}})
        
    return abc_list

def get_abc(name):
    abc_list = get_list()
    return abc_list[name]["abc"]

