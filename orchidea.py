import json
import platform

import pd

from src.Brass import *
from src.Keyboards import *
from src.PluckedStrings import *
from src.Strings import *
from src.Winds import *


def orchideaConfig(path):
    '''
    args:
        path:: str

    Set the path to orchidea samples.
    '''
    # check if last char of the path is / for linux and mac or \\ for windows
    if platform.system() == "Windows":
        if path[-1] != "\\":
            path += "\\"
    elif platform.system() == "Linux" or platform.system() == "Darwin":
        if path[-1] != "/":
            path += "/"

    scriptPath = os.path.dirname(os.path.realpath(__file__))
    # check if there is config.json inside the script folder
    configPath = os.path.join(scriptPath, "config.json")
    json.dump({"orchideaSolPath": path}, open(configPath, "w"))
    pd.print("Path added!")


def orchidea(note, dyn, orchideaNumber, orchideaString):
    '''
    args:
        note:: float
        dyn:: float
        orchideaString:: str

    Orchidea strings.
        Winds:
            flute
            oboe
            clarinet
            bassoon
            sax

        Strings:
            violin
            viola
            cello
            contrabass

        Brass:
            trumpet
            horn
            trombone
            tuba

        Keyboards:
            accordion

        PluckedStrings:
            guitar
            harp
    '''
    if orchideaString == "flute":
        return orchideaFlute(note, dyn, orchideaNumber)
    elif orchideaString == "oboe":
        return orchideaOboe(note, dyn, orchideaNumber)
    elif orchideaString == "clarinet":
        return orchideaClarinet(note, dyn, orchideaNumber)
    elif orchideaString == "bassoon":
        return orchideaBassoon(note, dyn, orchideaNumber)
    elif orchideaString == "violin":
        return orchideaViolin(note, dyn, orchideaNumber)
    elif orchideaString == "viola":
        return orchideaViola(note, dyn, orchideaNumber)
    elif orchideaString == "cello":
        return orchideaCello(note, dyn, orchideaNumber)
    elif orchideaString == "contrabass":
        return orchideaContrabass(note, dyn, orchideaNumber)
    elif orchideaString == "trumpet":
        return orchideaTrumpet(note, dyn, orchideaNumber)
    elif orchideaString == "horn":
        return orchideaHorn(note, dyn, orchideaNumber)
    elif orchideaString == "trombone":
        return orchideaTrombone(note, dyn, orchideaNumber)
    elif orchideaString == "tuba":
        return orchideaTuba(note, dyn, orchideaNumber)
    elif orchideaString == "accordion":
        return orchideaAccordion(note, dyn, orchideaNumber)
    elif orchideaString == "guitar":
        return orchideaGuitar(note, dyn, orchideaNumber)
    elif orchideaString == "harp":
        return orchideaHarp(note, dyn, orchideaNumber)
    elif orchideaString == "sax":
        return orchideaSax(note, dyn, orchideaNumber)
    else:
        pd.print("orchideaString not found")
        return None



def orchidea_setup():
    '''
    Load all the objects in pd.
    '''
    # Geral
    pd.add_object(orchidea, "orchidea")
    pd.add_object(orchideaConfig, "orchidea.config")

    # Keyboards
    pd.add_object(orchideaAccordion, "orchidea.accordion")

    # PluckedStrings
    pd.add_object(orchideaGuitar, "orchidea.guitar")
    pd.add_object(orchideaHarp, "orchidea.harp")

    # Winds
    pd.add_object(orchideaFlute, "orchidea.flute")
    pd.add_object(orchideaOboe, "orchidea.oboe")
    pd.add_object(orchideaClarinet, "orchidea.clarinet")
    pd.add_object(orchideaBassoon, "orchidea.bassoon")
    pd.add_object(orchideaSax, "orchidea.sax")

    # Strings
    pd.add_object(orchideaViolin, "orchidea.violin")
    pd.add_object(orchideaViola, "orchidea.viola")
    pd.add_object(orchideaCello, "orchidea.cello")
    pd.add_object(orchideaContrabass, "orchidea.contrabass")

    # Brass
    pd.add_object(orchideaTrumpet, "orchidea.trumpet")
    pd.add_object(orchideaHorn, "orchidea.horn")
    pd.add_object(orchideaTrombone, "orchidea.trombone")
    pd.add_object(orchideaTuba, "orchidea.tuba")




