import pd
import os
import glob
import json
import random

# find where is this script
scriptPath = os.path.dirname(os.path.realpath(__file__))

# go one folder up
scriptPath = os.path.dirname(scriptPath)


# check if there is config.json inside the script folder
configPath = os.path.join(scriptPath, "config.json")
if not os.path.exists(configPath):
    pd.error("config.json not found, use the object [orchidea.config] to set the path to orchidea samples")

else:
    ORCHIDEASOL_PATH = json.load(open(configPath))["orchideaSolPath"]


def orchideaAccordion(note, dyn, orchideaNumber):
    '''
    Orchidea Accordion: 
        Args:
            note: strin
            dyn: string "mf"
            orchideaNumber: int 1-15
        
        Techniques:
            Ordinary:
                1. breath (dynamic: mf)
                2. combination_of_registers (dynamic: mf)
                3. key_click (dynamic: mf)
                4. ordinary (dynamic: pp, mf, ff)
                5. sforzato (dynamic: fp)
    '''
    if orchideaNumber == 1:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for breath, must be mf")
            return None
        # Acc-breath-N-mf-1-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Keyboards/Accordion/breath/' + 'Acc-breath-N-' f'{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for breath")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 2:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for combination_of_registers, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Keyboards/Accordion/combination_of_registers/' + 'Acc-reg_combi-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for combination_of_registers")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 3:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for key_click, must be mf")
            return None
        #Acc-key_cl-N-mf-N-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Keyboards/Accordion/key_click/' + 'Acc-key_cl-N-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for key_click")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 4:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for ordinary, must be pp, mf, ff")
            return None
        # Acc-ord-A1-mf-alt1-N
        # Acc-ord-A1-mf-N-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Keyboards/Accordion/ordinario/' + 'Acc-ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for ordinary")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 5:
        dynamics = ['fp']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for sforzato, must be fp")
            return None
        # Acc-sfz-A2-fp-N-R100u
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Keyboards/Accordion/sforzato/' + 'Acc-sfz-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sforzato")
            return None
        pathname = random.choice(pathnames)
        return pathname




        








    

        
        
            



