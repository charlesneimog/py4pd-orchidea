import pd
import json
from instruments.Brass import *
from instruments.Strings import *
from instruments.Woodwinds import *


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
    pd.addobject(orchideaConfig, "orchidea.config")
    pd.addobject(orchideaFlute, "orchidea.flute")
    pd.addobject(orchideaViolin, "orchidea.violin")
    pd.addobject(orchideaTrumpet, "orchidea.trumpet")




