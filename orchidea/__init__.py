import json
import platform
import os
import csv

import pd

from orchidea.instruments.Brass import *
from orchidea.instruments.Keyboards import *
from orchidea.instruments.PluckedStrings import *
from orchidea.instruments.Strings import *
from orchidea.instruments.Winds import *

print = pd.print

scriptPath = os.path.dirname(__file__)
configPath = os.path.join(scriptPath, "config.json")

ORCHIDEA_PATH = ""
if os.path.exists(configPath):
    ORCHIDEA_PATH = json.load(open(configPath))["orchideaSolPath"]


def orchideaget(values):
    """
    args:
        path:: str

    Set the path to orchidea samples.
    """
    if type(values) == list:
        method = values[0]
    else:
        method = values

    if method == "instruments":
        thisdir = os.path.dirname(__file__)
        metadata = os.path.join(thisdir, "OrchideaSOL_metadata.csv")
        instruments = {}
        with open(metadata, mode="r") as file:
            ORCHIDEA_METADATA = csv.DictReader(file)
            for row in ORCHIDEA_METADATA:
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
    else:
        pass


def orchideaset(values):
    """
    args:
        path:: str

    Set the path to orchidea samples.
    """
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


def orchidea_setup():
    """
    Load all the objects in pd.
    """
    # Geral
    orchidea_main = pd.new_object("orchidea")
    orchidea_main.addmethod("set", orchideaset)
    orchidea_main.addmethod("get", orchideaget)

    orchidea_main.addmethod("flute", orchideaFlute)
    orchidea_main.addmethod("oboe", orchideaOboe)
    orchidea_main.addmethod("clarinet", orchideaClarinet)
    orchidea_main.addmethod("bassoon", orchideaBassoon)
    orchidea_main.addmethod("violin", orchideaViolin)
    orchidea_main.addmethod("viola", orchideaViola)
    orchidea_main.addmethod("cello", orchideaCello)
    orchidea_main.addmethod("contrabass", orchideaContrabass)
    orchidea_main.addmethod("trumpet", orchideaTrumpet)
    orchidea_main.addmethod("horn", orchideaHorn)
    orchidea_main.addmethod("trombone", orchideaTrombone)
    orchidea_main.addmethod("tuba", orchideaTuba)
    orchidea_main.addmethod("accordion", orchideaAccordion)
    orchidea_main.addmethod("guitar", orchideaGuitar)
    orchidea_main.addmethod("harp", orchideaHarp)
    orchidea_main.addmethod("sax", orchideaSax)
    orchidea_main.add_object()

    if ORCHIDEA_PATH == "":
        pd.error("Orchidea path not found, define it using the object [orchidea] and the method [set path <ORCHIDEA_SOL_PATH>]")
