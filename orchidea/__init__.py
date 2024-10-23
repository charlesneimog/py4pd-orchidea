import json
import platform
import os

import pd
import pandas


print = pd.print

scriptPath = os.path.dirname(__file__)
configPath = os.path.join(scriptPath, "config.json")

ORCHIDEA_PATH = ""
if os.path.exists(configPath):
    ORCHIDEA_PATH = json.load(open(configPath))["orchideaSolPath"]


ORCHIDEA_DATA = pandas.read_csv(os.path.join(scriptPath, "OrchideaSOL_metadata.csv"))


def getsample():
    keys = {
        "family": "Family (abbr.)",
        "inst": "Instrument (abbr.)",
        "tech": "Technique (abbr.)",
        "midi": "Pitch ID (if applicable)",
        "pitch": "Pitch Name",
        "dyn": "Dynamics",
        "mute": "Mute (abbr.)",
        "string": "String ID (if applicable)",
    }

    user_input = pd.get_obj_var("keys", initial_value={})
    if ORCHIDEA_DATA is None:
        raise ValueError("Orchidea data not found. Please check the path to the Orchidea samples.")

    conditions = []
    for key, column in keys.items():
        if user_input.get(key) is not None:  # If the user has set a value for this key
            conditions.append(ORCHIDEA_DATA[column] == user_input[key])
    if conditions:
        combined_condition = conditions[0]
        for condition in conditions[1:]:
            combined_condition &= condition
    else:
        combined_condition = pandas.Series([True] * len(ORCHIDEA_DATA))

    matching_rows = ORCHIDEA_DATA[combined_condition]
    if not matching_rows.empty:
        len = matching_rows.shape[0]
        if len == 1:
            return ORCHIDEA_PATH + "/" + matching_rows["Path"].values[0]
        else:
            samples_complete = []
            samples = matching_rows["Path"].values
            for sample in samples:
                samples_complete.append(ORCHIDEA_PATH + "/" + sample)
            return samples_complete
    else:
        pd.error("No matching rows found.")


def orchideaget(values):
    """
    args:
        path:: str

    Set the path to orchidea samples.
    """
    keys = {
        "family": "Family (abbr.)",
        "inst": "Instrument (abbr.)",
        "tech": "Technique (abbr.)",
        "midi": "Pitch ID (if applicable)",
        "pitch": "Pitch Name",
        "dyn": "Dynamics",
        "mute": "Mute (abbr.)",
        "string": "String ID (if applicable)",
    }

    if type(values) == list:
        method = values[0]
    else:
        method = values

    if method == "instruments":
        instruments = {}
        for row in ORCHIDEA_DATA:
            inst = row["Instrument (in full)"]
            tech = row["Technique (abbr.)"]
            if inst not in instruments:
                instruments[inst] = []
            if tech not in instruments[inst]:
                instruments[inst].append(tech)
        for inst in instruments:
            mystr = "[" + inst + "]:\n\t" + ",\n\t".join(instruments[inst])
            pd.print(mystr, show_prefix=False)
            pd.print("", show_prefix=False)
    elif method == "keys":
        for key in keys:
            print(key + ": " + keys[key], show_prefix=False)

    elif method in keys.keys():
        print(f"Valid {method}:", show_prefix=False)
        for family in ORCHIDEA_DATA[keys[method]].unique():
            print("\t" + family, show_prefix=False)

    else:
        pass


def orchideaset(values):
    """
    args:
        path:: str

    Set the path to orchidea samples.
    """
    keys = {
        "family": "Family (abbr.)",
        "inst": "Instrument (abbr.)",
        "tech": "Technique (abbr.)",
        "midi": "Midi value(if applicable)",
        "pitch": "Pitch Name",
        "dyn": "Dynamics",
        "mute": "Mute (abbr.)",
        "string": "String ID (if applicable)",
    }

    method = values[0]
    if method == "path":
        path = values[1]
        if platform.system() == "Windows":
            if path[-1] != "\\":
                path += "\\"
        elif platform.system() == "Linux" or platform.system() == "Darwin":
            if path[-1] != "/":
                path += "/"
        scriptPath = os.path.dirname(__file__)
        configPath = os.path.join(scriptPath, "config.json")
        json.dump({"orchideaSolPath": path}, open(configPath, "w"))
        pd.print("Path added!")
    elif method in keys.keys():
        keys = pd.get_obj_var("keys", initial_value={})
        keys[method] = values[1]
        pd.set_obj_var("keys", keys)


def clear():
    pd.set_obj_var("keys", {})


def py4pdLoadObjects():
    """
    Load all the objects in pd.
    """
    # Geral
    orchidea_main = pd.new_object("orchidea")
    orchidea_main.addmethod("set", orchideaset)
    orchidea_main.addmethod("get", orchideaget)
    orchidea_main.addmethod("sample", getsample)
    orchidea_main.addmethod("clear", clear)

    orchidea_main.add_object()

    if ORCHIDEA_PATH == "":
        pd.error("Orchidea path not found, define it using the object [orchidea] and the method [set path <ORCHIDEA_SOL_PATH>]")
