import pd
import json
from instruments.Brass import *
from instruments.Keyboards import *
from instruments.Strings import *
from instruments.Winds import *


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


def py4pdLoadObjects():
    '''
    Load all the objects in pd.
    '''
    # Geral
    pd.addobject(orchideaConfig, "orchidea.config")

    # Keyboards
    pd.addobject(orchideaAccordion, "orchidea.accordion")

    # Winds
    pd.addobject(orchideaFlute, "orchidea.flute")

    # Strings
    pd.addobject(orchideaViolin, "orchidea.violin")

    # Brass
    pd.addobject(orchideaTrumpet, "orchidea.trumpet")
    pd.addobject(orchideaHorn, "orchidea.horn")
    pd.addobject(orchideaTrombone, "orchidea.trombone")
    pd.addobject(orchideaTuba, "orchidea.tuba")




