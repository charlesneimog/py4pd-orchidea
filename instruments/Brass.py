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
        Args:
            note: string "C4"
            dyn: string "mf"
            orchideaNumber: int 1-15
        
        Techniques:

            Ordinary:

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
        

def orchideaHorn(note, dyn, orchideaNumber):
    '''
    Orchidea Horn:
    
        Args:
            note: string
            dyn: string
            orchideaNumber: int

        Techniques:

            Ordinary:

                1. brassy (dynamic: ff)
                2. flatterzunge (dynamic: pp, mf, ff)
                3. flatterzunge stopped (dynamic: mf)
                4. ordinario (dynamic: pp, mf, ff)
                5. sforzato (dynamic: f, fp)
                6. slap pitched (dynamic: p)
                7. sttoped (dynamic: mf)

            Sordina:
                8. flatterzunge (dynamic: mf)
                9. ordinario (dynamic: mf)
    '''

    if orchideaNumber == 1:
        # not important the final of the file name
        dynamics = ['ff']
        if dyn not in dynamics:
            pd.error("orchideaHorn: wrong dynamic for brassy, must be ff")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Horn/brassy/' + 'Hn-brassy-' + note + f'-{dyn}*')
        # get the files that match the pathname
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for brassy")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 2:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("orchideaHorn: wrong dynamic for flatterzunge, must be pp, mf or ff")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Horn/flatterzunge/' + 'Hn-flatt-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for flatterzunge")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 3:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaHorn: wrong dynamic for flatterzunge stopped, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Horn/flatterzunge_stopped/' + 'Hn-flatt_stopped-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for flatterzunge stopped")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 4:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("orchideaHorn: wrong dynamic for ordinario, must be pp, mf or ff")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Horn/ordinario/' + 'Hn-ord-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for ordinario")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 5:
        dynamics = ['f', 'fp']
        if dyn not in dynamics:
            pd.error("orchideaHorn: wrong dynamic for sforzato, must be f or fp")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Horn/sforzato/' + 'Hn-sfz-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sforzato")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 6:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaHorn: wrong dynamic for slap pitched, must be p")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Horn/slap_pitched/' + 'Hn-slap-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for slap pitched")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 7:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaHorn: wrong dynamic for stopped, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Horn/stopped/' + 'Hn-stopped-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for stopped")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 8:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaHorn: wrong dynamic for flatterzunge, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Horn+sordina/flatterzunge/' + 'Hn+S-flatt-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for flatterzunge")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 9:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaHorn: wrong dynamic for ordinario, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Horn+sordina/ordinario/' + 'Hn+S-ord-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for ordinario")
            return None
        pathname = random.choice(pathnames)
        return pathname


def orchideaTrombone(note, dyn, orchideaNumber):    
    '''

    Orchidea Trombone:
    
        Args:
            note: string
            dyn: string
            orchideaNumber: int

        Techniques:

            Ordinary:   

                1. brassy (dynamic: ff)
                2. flatterzunge (dynamic: pp, mf, ff)
                3. flatterzunge no mouthpiece (dynamic: p, f) | Just C#5, D5.
                4. ordinario (dynamic: pp, mf, ff)
                5. pedal tone (dynamic: p, f)
                6. sforzato (dynamic: f, fp)
                7. slap_pitched (dynamic: p)

            Sordina Cup:
                8. flatterzunge (dynamic: mf)
                9. ordinario (dynamic: mf)

            Sordina Harmon:
                10. flatterzunge (dynamic: mf)
                11. ordinario (dynamic: mf)

            Sordina Straight:
                12. flatterzunge (dynamic: mf)
                13. ordinario (dynamic: mf)

            Sordina Wah:
                14: flatterzunge closed (dynamic: mf)
                15: flattezunge open (dynamic: mf)
                16: ordinario closed (dynamic: mf)
                17: ordinario open (dynamic: mf)
    '''
    if orchideaNumber == 1:
        dynamics = ['ff']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for brassy, must be ff")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone/brassy/' + 'Tbn-brassy-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for brassy")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 2:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for flatterzunge, must be pp, mf or ff")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone/flatterzunge/' + 'Tbn-flatt-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for flatterzunge")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 3:
        dynamics = ['p', 'f']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for flatterzunge no mouthpiece, must be p or f")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone/flatterzunge_no_mouthpiece/' + 'Tbn-flatt-no-mouthpiece-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for flatterzunge no mouthpiece")
            return None
        pathname = random.choice(pathnames)
        return pathname

    elif orchideaNumber == 4:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for ordinario, must be pp, mf or ff")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone/ordinario/' + 'Tbn-ord-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for ordinario")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 5:
        dynamics = ['p', 'f']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for pedal tone, must be p or f")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone/pedal_tone/' + 'Tbn-pedal-tone-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for pedal tone")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 6:
        dynamics = ['f', 'fp']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for sforzato, must be f or fp")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone/sforzato/' + 'Tbn-sforzato-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sforzato")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 7:
        dynamics = ['p']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for slap_pitched, must be p")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone/slap_pitched/' + 'Tbn-slap-pitched-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for slap_pitched")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 8:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for sordina cup flatterzunge, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone/sordina_cup/flatterzunge/' + 'Tbn+SC-flatt-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sordina cup flatterzunge")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 9:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for sordina cup ordinario, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone+sordina_cup/ordinario/' + 'Tbn+SC-ord-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sordina cup ordinario")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 10:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for sordina cup pedal tone, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone+sordina_harmon/flatterzunge/' + 'Tbn+SH-flatt-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sordina cup pedal tone")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 11:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for sordina cup pedal tone, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone+sordina_harmon/ordinario/' + 'Tbn+SH-ord-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sordina harmon")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 12:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for sordina harmon pedal tone, must be mf")
            return None
        # Trombone+sordina_straight
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone+sordina_straight/flatterzunge/' + 'Tbn+SS-flatt-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sordina harmon pedal tone")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 13:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for sordina harmon pedal tone, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone+sordina_straight/ordinario/' + 'Tbn+SS-ord-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sordina straight")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 14:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for sordina straight pedal tone, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone+sordina_wah/flatterzunge_closed/' + 'Tbn+SW-flatt_closed-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sordina straight pedal tone")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 15:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone+sordina_wah/flatterzunge_open/' + 'Tbn+SW-flatt_open-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sordina straight pedal tone")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 16:
        # ordinario_closed
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for sordina straight pedal tone, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone+sordina_wah/ordinario_closed/' + 'Tbn+SW-ord_closed-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sordina straight pedal tone")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 17:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaTrombone: wrong dynamic for sordina straight pedal tone, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Trombone+sordina_wah/ordinario_open/' + 'Tbn+SW-ord_open-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sordina straight pedal tone")
            return None
        pathname = random.choice(pathnames)
        return pathname
    else:
        pd.error("orchideaTrombone: wrong orchidea number")
        return None


def orchideaTuba(note, dyn, orchideaNumber):    
    '''
    Orchidea Tuba:
        Args:
            note: string
            dyn: string
            orchideaNumber: int

        Techniques:
            Ordinary:   
                1. bisbigliando (dynamic: mf)
                2. blow (dynamic: p) - unpitched
                3. brazzy (dynamic: ff) - C#4, D4, D#4
                4. breath (dynamic: pp) - unpitched
                5. discolored_fingering (dynamic: p - pp)
                6. flatterzunge (dynamic: pp, mf)
                7. growl (dynamic: mf, ff) - unpitched
                8. kiss (dynamic: f) - unpitched
                9. ordinario (dynamic: pp, mf, ff)
                10. ordinario_high_register (dynamic: p, mf, ff)
                11. pedal_tone (dynamic: pp, mf, ff)
                12. sforzato (dynamic: fp)
                13. single_tonguing (dynamic: mf)
                14. slap_pitched (dynamic: mf, f, ff)
                15. slap_unpitched (dynamic: mf, f)

            Sordina:
                16. ordinario (dynamic: p, f)
    '''
    if orchideaNumber == 1:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for bisbigliando, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/bisbigliando/' + 'BTb-bisb-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for bisbigliando")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 2:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/blow/' + 'BTb-blow*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for blow")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 3:
        if note not in ['C#4', 'D4', 'D#4']:
            pd.error("orchideaTuba: wrong note for brazzy, must be C#4, D4 or D#4")
            return None
        dynamics = ['ff']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for brazzy, must be ff")
            return None
        # BTb-brassy-C#4-ff-N-T23u
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/brazzy/' + 'BTb-brassy-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for brazzy")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 4:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/breath/' + 'BTb-breath*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for blow")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 5:
        dynamics = ['p', 'pp']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for discolored_fingering, must be p or pp")
            return None
        # BTb-dsclrd_fngr-A#3-p-N-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/discolored_fingering/' + 'BTb-dsclrd_fngr-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for discolored_fingering")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 6:
        dynamics = ['pp', 'mf']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for flatterzunge, must be pp or mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/flatterzunge/' + 'BTb-flatt-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for flatterzunge")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 7:
        dynamics = ['mf', 'ff']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for growl, must be mf or ff")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/growl/' + 'BTb-growl-N-' + f'{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for growl")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 8:
        dynamics = ['f']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for kiss, must be f")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/kiss/' + 'BTb-kiss-N-' + f'{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for kiss")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 9:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for ordinario, must be pp, mf or ff")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/ordinario/' + 'BTb-ord-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for ordinario")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 10:
        dynamics = ['p', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for ordinario_high_register, must be p, mf or ff")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/ordinario_high_register/' + 'BTb-ord_hi_reg-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for ordinario_high_register")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 11:
        dynamics = ['p', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for pedal_tone, must be p, mf or ff")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/pedal_tone/BTb-pdl_tone-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for pedal_tone")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 12:
        dynamics = ['fp']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for sforzato, must be fp")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/sforzato/' + 'BTb-sfz-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for sforzato")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 13:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for single tonguing, must be mf")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/single_tonguing/' + 'BTb-sngl_tng-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for single tonguing")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 14:
        dynamics = ['mf', 'f', 'ff']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for slap_pitched, must be mf or ff")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/slap_pitched/' + 'BTb-slap-' + note + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for slap_pitched")
            return None
        # check if there is the dynamic in the pathname
        pathnames = [path for path in pathnames if dyn in path]
        if pathnames == []:
            pd.error("No pathnames found for slap_pitched with the right dynamic")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 15:
        dynamics = ['mf', 'f']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for slap_unpitched, must be mf or ff")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba/slap_unpitched/' + 'BTb-slap_unp-N-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for slap_unpitched")
            return None
        pathnames = [path for path in pathnames if dyn in path]
        if pathnames == []:
            pd.error("No pathnames found for slap_unpitched with the right dynamic")
            return None
        pathname = random.choice(pathnames)
        return pathname
    elif orchideaNumber == 16:
        dynamics = ['p', 'f']
        if dyn not in dynamics:
            pd.error("orchideaTuba: wrong dynamic for tongue_stop, must be p or f")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Brass/Bass_Tuba+sordina/ordinario/' + 'BTb+S-ord-' + note + f'-{dyn}*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("No pathnames found for tongue_stop")
            return None
        pathname = random.choice(pathnames)
        return pathname
    else:
        pd.error("orchideaTuba: wrong orchideaNumber, must be between 1 and 16")
        return None













    

        
        
            



