import pd
import json
from src.Brass import *
from src.Keyboards import *
from src.Strings import *
from src.Winds import *
from src.PluckedStrings import *


def orchideaConfig(path):
    '''
    args:
        path:: str

    Set the path to orchidea samples.
    '''
    scriptPath = os.path.dirname(os.path.realpath(__file__))
    # check if there is config.json inside the script folder
    configPath = os.path.join(scriptPath, "config.json")
    json.dump({"orchideaSolPath": path}, open(configPath, "w"))


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



def py4pdLoadObjects():
    '''
    Load all the objects in pd.
    '''
    # Geral
    pd.addobject(orchidea, "orchidea")
    pd.addobject(orchideaConfig, "orchidea.config")

    # Keyboards
    pd.addobject(orchideaAccordion, "orchidea.accordion")

    # PluckedStrings
    pd.addobject(orchideaGuitar, "orchidea.guitar")
    pd.addobject(orchideaHarp, "orchidea.harp")

    # Winds
    pd.addobject(orchideaFlute, "orchidea.flute")
    pd.addobject(orchideaOboe, "orchidea.oboe")
    pd.addobject(orchideaClarinet, "orchidea.clarinet")
    pd.addobject(orchideaBassoon, "orchidea.bassoon")
    pd.addobject(orchideaSax, "orchidea.sax")

    # Strings
    pd.addobject(orchideaViolin, "orchidea.violin")
    pd.addobject(orchideaViola, "orchidea.viola")
    pd.addobject(orchideaCello, "orchidea.cello")
    pd.addobject(orchideaContrabass, "orchidea.contrabass")

    # Brass
    pd.addobject(orchideaTrumpet, "orchidea.trumpet")
    pd.addobject(orchideaHorn, "orchidea.horn")
    pd.addobject(orchideaTrombone, "orchidea.trombone")
    pd.addobject(orchideaTuba, "orchidea.tuba")




