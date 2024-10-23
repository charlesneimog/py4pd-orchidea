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


def orchideaHarp(note, dyn, orchideaNumber):
    '''
    Orchidea Harp: 
        Args:
            note: strin
            dyn: string "mf"
            orchideaNumber: int 1-15
        
        Techniques:
            Ordinary:
                1. bisbigliando (dynamic: p, mf)
                2. bisbigliando_with_stick (dynamic: mf)
                3. cluster (dynamic: pp, mf, ff)
                4. cluster_with_nail (dynamic: p, f)
                5. damped (dynamic: mf)
                6. harmonic_fingering (dynamic: p, f)
                7. ordinario (dynamic: pp, mf, ff)
                8. pizzicato_bartok (dynamic: ff)
                9. tremolo_with_fingertips (dynamic: p) 
    '''
    if orchideaNumber == 1:
        dynamics = ['pp', 'p', 'mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for bisbigliando, must be pp, p, mf")
            return None
        # Hp-bisb-A#1-mf-N-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Harp/bisbigliando/' + 'Hp-bisb-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for bisbigliando")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 2:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for bisbigliando_with_stick, must be mf")
            return None
        # Hp-bisb_and_stick-C6-mf-N-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Harp/bisbigliando_with_stick/' + 'Hp-bisb_and_stick-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for bisbigliando_with_stick")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 3:
        dynamics = ['pp', 'mf', 'ff']
        # Hp-cluster_hi-N-pp-N-N
        if dyn not in dynamics:
            pd.error("Wrong dynamic for cluster, must be pp, mf, ff")
            return None
        # if there is [0, 1 or 2] in note, then 
        register = ''
        if any(num in note for num in ['0', '1', '2']):
            register = 'lo'
        elif any(num in note for num in ['3', '4', '5']):
            register = 'mid'
        elif any(num in note for num in ['6', '7', '8']):
            register = 'hi'
        else:
            pd.error("Wrong register for cluster, must be 0-8")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Harp/cluster/' + f'Hp-cluster_{register}-N-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for cluster")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 4:
        dynamics = ['p', 'f']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for cluster_with_nail, must be p, f")
            return None
        # Hp-cluster_and_nail_lo-N-f-N-N
        register = ''
        if any(num in note for num in ['0', '1', '2']):
            register = 'lo'
        elif any(num in note for num in ['3', '4', '5']):
            register = 'mid'
        elif any(num in note for num in ['6', '7', '8']):
            register = 'hi'
        else:
            pd.error("Wrong register for cluster_with_nail, must be 0-8")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Harp/cluster_with_nail/' + f'Hp-cluster_and_nail_{register}-N-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for cluster_with_nail")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 5:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for damped, must be mf")
            return None
        # Hp-damp-A2-mf-N-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Harp/damped/' + 'Hp-damp-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for damped")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 6:
        dynamics = ['p', 'f']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for harmonic_fingering, must be p, f")
            return None
        # Hp-harm_fngr-A5-f-N-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Harp/harmonic_fingering/' + 'Hp-harm_fngr-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for harmonic_fingering")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 7:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for ordinario, must be pp, mf, ff")
            return None
        #Hp-ord-A2-ff-N-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Harp/ordinario/' + 'Hp-ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for ordinario")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 8:
        dynamics = ['ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for pizzicato_bartok, must be ff")
            return None
        # Hp-pizz_bartok-A4-ff-N-R100d
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Harp/pizzicato_bartok/' + 'Hp-pizz_bartok-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for pizzicato_bartok")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 9:
        dynamics = ['p']
        if dyn not in dynamics:
            pd.error("Wrong dynamic for tremolo_with_fingertips, must be p")
            return None
        # Hp-trem_and_fngrtip-N-p-N-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'PluckedStrings/Harp/tremolo_with_fingertips/' + 'Hp-trem_and_fngrtip-N-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for tremolo_with_fingertips")
            return None
        pathname = random.choice(pathnames)
        return pathname



