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


def orchideaViolin(note, dyn, orchideaNumber):
    '''
    Orchidea Violin: 
        Args:
            note: string "A4"
            dyn: string "mf"
            orchideaNumber: int 1-15

        Techniques:
            Ordinario:
                1. artificial_harmonic                   
                2. artificial_harmonic_tremolo
                3. behind_the_bridge                     
                4. behind_the_fingerboard
                5. col_legno_battuto                     
                6. col_legno_tratto
                7. ordinario                             
                8. pizzicato_bartok
                9. pizzicato_l_vib                       
                10. pizzicato_secco
                11. sforzato                              
                12. sul_ponticello
                13. sul_ponticello_tremolo                
                14. tremolo

            Sordina:
                15. ordinario+sordina                     
                16. tremolo+sordina

            Sordina+Piombo:
                17. ordinario+Violin+sordina_piombo       
                18. tremolo+sordina_piombo
    '''
    string = pd.getkey('string')
    if orchideaNumber == 1:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/artificial_harmonic/' + 'Vn-art_harm-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 2:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        # Vn-art_harm_trem-G7-mf-2c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/harmonic_tremolo/' + 'Vn-art_harm_trem-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 3:
        # Vn-behind_bridge-N-N-1c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/behind_the_bridge/' + 'Vn-behind_bridge-N-N-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 4:
        # behind_the_fingerboard
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/behind_the_fingerboard/' + 'Vn-behind_fingerboard-N-N-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 5:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/col_legno_battuto/' + 'Vn-legno_batt-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 6:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/col_legno_tratto/' + 'Vn-legno_tratto-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 7:
        # Vn-ord-A3-ff-4c-N
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/ordinario/' + 'Vn-ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 8:
        # pizzicato_bartok Vn-pizz_bartok-A4-ff-3c-N
        dynamics = ['ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/pizzicato_bartok/' + 'Vn-pizz_bartok-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 9:
        #Vn-pizz_lv-A3-ff-4c-N
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/pizzicato_l_vib' + 'Vn-pizz_lv-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 10:
        # Vn-pizz_sec-A3-pp-4c-N
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/pizzicato_secco/' + 'Vn-pizz_sec-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 11:
        # Vn-sfz-A4-f-3c-N
        dynamics = ['f', 'fp']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be f or fp.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/sforzato/' + 'Vn-sfz-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 12:
        # sul_ponticello
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        # Vn-pont-A4-mf-3c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/sul_ponticello/' + 'Vn-pont-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 13:
        # sul_ponticello_tremolo
        # Vn-pont_trem-A5-mf-1c-N
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/sul_ponticello_tremolo/' + 'Vn-pont_trem-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 14:
        # tremolo
        # Vn-trem-A4-ff-2c-N
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/tremolo/' + 'Vn-trem-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    
    # Violin+sordina
    elif orchideaNumber == 15:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        # Vn+S-ord-A3-ff-4c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin+sordina/ordinario/' + 'Vn+S-ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)

    elif orchideaNumber == 16:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        # Vn+S-trem-G#6-ff-1c-R100d
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin+sordina/tremolo/' + 'Vn+S-trem-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    # Violin+sordina_piombo
    elif orchideaNumber == 17:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        # Vn+SP-ord-A#3-mf-4c-T10u
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin+sordina_piombo/ordinario/' + 'Vn+SP-ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 18:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        # Vn+SP-trem-A#6-mf-4c-T10u
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin+sordina_piombo/tremolo/' + 'Vn+SP-trem-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.")
            pd.logpost(3, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    else:
        pd.error("Wrong orchidea number.")
        return None


def orchideaViola(note, dyn, orchideaNumber):
    '''
    Orchidea Viola: 
        Args:
            note: string "A4"
            dyn: string "mf"
            orchideaNumber: int 1-15

        Techniques:
            Ordinario:
                1. artificial_harmonic
                2. artificial_harmonic_tremolo
                3. behind_the_bridge
                4. behind_the_fingerboard
                5. col_legno_battuto
                6. col_legno_tratto
                7. ordinario
                8. pizzicato_bartok
                9. pizzicato_secco
                10. sforzato
                11. sul_ponticello
                12. sul_ponticello_tremolo
                13. sul_tasto_tremolo
                14. tremolo

            Sordina:
                15. ordinario
                16. tremolo

            Sordina Piombo:
                17. ordinario
                18. tremolo

    '''
    string = pd.getkey('string')
    if orchideaNumber == 1:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-art_harm-G6-mf-2c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Viola/artificial_harmonic/' + 'Va-art_harm-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None: 
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.")
            pd.logpost(3, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 2:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-art_harm_trem-G6-mf-2c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Viola/artificial_harmonic_tremolo/' + 'Va-art_harm_trem-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
        if string is not None: 
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.")
            pd.logpost(3, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 3:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Viola/behind_the_bridge/' + 'Va-behind_bridge*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None: 
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.")
            pd.logpost(3, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 4:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Viola/behind_the_fingerboard/' + 'Va-behind_fingerboard*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None: 
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.")
            pd.logpost(3, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 5:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-legno_batt-G#3-mf-4c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Viola/col_legno_battuto/' + 'Va-legno_batt-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.")
            pd.logpost(3, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 6:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-legno_tratt-G#3-mf-4c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Viola/col_legno_tratto/' + 'Va-legno_tratt-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(3, "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.")
            pd.logpost(3, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 7:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        # Va-col_legno-G#3-pp-4c-N


        
