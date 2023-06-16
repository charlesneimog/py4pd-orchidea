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


def orchideaGuitar(note, dyn, orchideaNumber):
    '''
    Orchidea Guitar: 
        Args:
            note: strin
            dyn: string "mf"
            orchideaNumber: int 1-15
        
        Techniques:
            Ordinary:
                1. breathbehind_the_frog (dynamic: mf)
                2. harmonic_fingering (dynamic: p)
                3. ordinario (dynamic: pp, mf, ff)
                4. ordinario_high_register (dynamic: mf)
                5. pizzicato_bartok (dynamic: ff)
                6. sul_ponticello (dynamic: mf)
    '''
    if orchideaNumber == 1:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for breath, must be mf")
            return None
        # Acc-breath-N-mf-1-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Guitar/behind_the_frog/' + 'Gtr-behind_frog-N-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for breath")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 2:
        dynamics = ['p']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for harmonic, must be p")
            return None
        # Gtr-harm_fngr-A3-p-5c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Guitar/harmonic_fingering/' + 'Gtr-harm_fngr-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for harmonic")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 3:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for ordinario, must be pp, mf, ff")
            return None
        # Gtr-ord-A2-pp-5c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Guitar/ordinario/' + 'Gtr-ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for ordinario")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 4:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for ordinario_high_register, must be mf")
            return None
        # Gtr-ord_high_reg-A2-mf-5c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Guitar/ordinario_high_register/' + 'Gtr-ord_hi_reg-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for ordinario_high_register")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 5:
        dynamics = ['ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for pizzicato_bartok, must be ff")
            return None
        # Gtr-pizz_bartok-A#2-ff-5c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Guitar/pizzicato_bartok/' + 'Gtr-pizz_bartok-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for pizzicato_bartok")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 6:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for sul_ponticello, must be mf")
            return None
        # Gtr-sul_pont-A#2-mf-5c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Guitar/sul_ponticello/' + 'Gtr-pont-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sul_ponticello")
            return None
        pathname = random.choice(pathnames)
        return pathname
    else:
        pd.error("Wrong orchideaNumber, must be 1-6")
        return None











    

        
        
            



