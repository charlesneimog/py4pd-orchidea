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


def orchideaTrumpet(note, dyn, orchideaNumber):
    '''

    Orchidea Trumpet: 
        args:
            note: string "C4"
            dyn: string "mf"
            orchideaNumber: int 1-15
        
        Techniques:

            No sordina:

                1. brassy (dynamic: ff)
                2. flatterzunge (dynamic: pp, mf, ff)
                3. ordinario (dynamic: pp, mf, ff)
                4. pedal tone (dynamic: mf)
                5. sforzato (dynamic: f, fp)
                6. slap pitched (dynamic: p)

            Sordina Cup:

                7. flatterzunge (dynamic: mf)
                8. ordinario (dynamic: mf)

            Sordina Harmon:

                9. flatterzunge (dynamic: mf)
                10. ordinario (dynamic: mf)

            Sordina Straight:

                11. flatterzunge (dynamic: mf)
                12. ordinario (dynamic: mf)

            Sordina wah:
                
                13. flatterzunge open (dynamic: mf)
                14. ordinario closed (dynamic: mf)
                15. ordinario open (dynamic: mf)


    '''
    if orchideaNumber == 1:
        # not important the final of the file name
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C/brassy/' + 'TpC-brassy-' + note + '-ff*.wav')
        # get the files that match the pathname
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for brassy")
            return None
        pathname = random.choice(pathnames)
        return pathname

    elif orchideaNumber == 2:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C/flatterzunge/' + 'TpC-flatt-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for flatterzunge")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 3:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C/ordinario/' + 'TpC-ord-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for ordinario")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 4:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C/pedal_tone/' + 'TpC-pdl_tone-' + note + f'-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for pedal tone")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 5:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C/sforzato/' + 'TpC-sfz-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sforzato")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 6:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C/slap_pitched/' + 'TpC-slap-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for slap pitched")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 7:
        # TpC+SC-flatt-A4-mf-N-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C+sordina_cup/flatterzunge/' + 'TpC+SC-flatt-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for flatterzunge")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 8:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C+sordina_cup/ordinario/' + 'TpC+SC-ord-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for ordinario")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 9:
        #TpC+SC-ord-B3-mf-N-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C+sordina_harmon/flatterzunge/' + 'TpC+SH-flatt-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for Trumpet_C+sordina_harmon, note: " + note + ", dyn: " + dyn)
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 10:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C+sordina_harmon/ordinario/' + 'TpC+SH-ord-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for Trumpet_C+sordina_harmon, note: " + note + ", dyn: " + dyn)
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 11:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C+sordina_straight/flatterzunge/' + 'TpC+SS-flatt-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for Trumpet_C+sordina_straight, note: " + note + ", dyn: " + dyn)
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 12:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C+sordina_straight/ordinario/' + 'TpC+SS-ord-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for Trumpet_C+sordina_straight, note: " + note + ", dyn: " + dyn)
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 13:
        # Trumpet_C+sordina_wah/flatterzunge_open/TpC+SW-flatt_open-A4-mf-N-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C+sordina_wah/flatterzunge_open/' + 'TpC+SW-flatt_open-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for Trumpet_C+sordina_wah, note: " + note + ", dyn: " + dyn)
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 14:
        # ordinario_closed
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C+sordina_wah/ordinario_closed/' + 'TpC+SW-ord_closed-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for Trumpet_C+sordina_wah, note: " + note + ", dyn: " + dyn)
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 15:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trumpet_C+sordina_wah/ordinario_open/' + 'TpC+SW-ord_open-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for Trumpet_C+sordina_wah, note: " + note + ", dyn: " + dyn)
            return None
        pathname = random.choice(pathnames)
        return pathname
    else:
        pd.error("orchideaTrumpet: wrong orchideaNumber must be between 1 and 15")
        return None
        
