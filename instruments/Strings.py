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
    args:
        orchideaNumber:: int
        note:: str
        dyn:: str

    Get the pathname for orchidea samples.

1 = artificial_harmonic                   
2 = harmonic_tremolo
3 = behind_the_bridge                     
4 = behind_the_fingerboard
5 = col_legno_battuto                     
6 = col_legno_tratto
7 = ordinario                             
8 = pizzicato_bartok
9 = pizzicato_l_vib                       
10 = pizzicato_secco
11 = sforzato                              
12 = sul_ponticello
13 = sul_ponticello_tremolo                
14 = tremolo
15 = ordinario+sordina                     
16 = tremolo+sordina
17 = ordinario+Violin+sordina_piombo       
18 = tremolo+sordina_piombo


    '''
    if orchideaNumber == 1:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/artificial_harmonic/' + 'Vn-art_harm-' + note + '-' + dyn + '-N-N.wav')
    elif orchideaNumber == 2:
        # Vn-art_harm_trem-A5-mf-4c-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/artificial_harmonic_tremolo/' + 'Vn-art_harm_trem-' + note + '-' + dyn + '-N-N.wav')
    elif orchideaNumber == 3:
        allNotes = os.listdir(os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/behind_the_bridge/'))
        randomNote = random.choice(allNotes)
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/behind_the_bridge/' + randomNote)
    elif orchideaNumber == 4:
        # Vn-behind_fngrbrd-N-N-N-N
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/behind_the_fingerboard/' + 'Vn-behind_fngrbrd-N-N-N-N.wav')
    elif orchideaNumber == 5:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/col_legno_battuto/' + 'Vn-legno_batt-' + note + '-' + dyn + '-N-N.wav')
    elif orchideaNumber == 6:
        # Vn-legno_tratto-A4-mf-3c-N.wav
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/col_legno_tratto/' + 'Vn-legno_tratto-' + note + '-' + dyn + '-N-N.wav')
    elif orchideaNumber == 7:
        # Vn-ord-A4-ff-4c-N.wav
        strings = ['4c', '3c', '2c', '1c']
        pathnames = []
        for str in strings:
            pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/ordinario/' + 'Vn-ord-' + note + '-' + dyn + '-' + str + '-N.wav')
            pathnames.append(pathname)
        pathname = random.choice(pathnames)
    elif orchideaNumber == 8:
        strings = ['4c', '3c', '2c', '1c']
        pathnames = []
        for str in strings:
            pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/pizzicato_bartok/' + 'Vn-pizz_bartok-' + note + '-' + dyn + '-' + str + '-N.wav')
            pathnames.append(pathname)
        pathname = random.choice(pathnames)
    elif orchideaNumber == 9:
        strings = ['4c', '3c', '2c', '1c']
        pathnames = []
        for str in strings:
            pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/pizzicato_l_vib/' + 'Vn-pizz_lv-' + note + '-' + dyn + '-' + str + '-N.wav')
            if os.path.exists(pathname):
                pathnames.append(pathname)
        if pathnames == []:
            pd.error("No pathnames found for pizzicato_secco")
            return None
        pathname = random.choice(pathnames)
    elif orchideaNumber == 10:
        strings = ['4c', '3c', '2c', '1c']
        pathnames = []
        for str in strings:
            pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/pizzicato_secco/' + 'Vn-pizz_sec-' + note + '-' + dyn + '-' + str + '-N.wav')
            if os.path.exists(pathname):
                pathnames.append(pathname)
        if pathnames == []:
            pd.error("No pathnames found for pizzicato_secco")
            return None
        pathname = random.choice(pathnames)
    elif orchideaNumber == 11:
        strings = ['4c', '3c', '2c', '1c']
        pathnames = []
        for str in strings:
            # Vn-pizz_sec-A4-mf-3c-N
            pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/pizzicato_secco/' + 'Vn-pizz_sec-' + note + '-' + dyn + '-' + str + '-N.wav')
            if os.path.exists(pathname):
                pathnames.append(pathname)
        pathname = random.choice(pathnames)
    elif orchideaNumber == 12:
        strings = ['4c', '3c', '2c', '1c']
        pathnames = []
        for str in strings:
            pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/ponticello/' + 'Vn-pont-' + note + '-' + dyn + '-' + str + '-N.wav')
            if os.path.exists(pathname):
                pathnames.append(pathname)
        pathname = random.choice(pathnames)
    elif orchideaNumber == 13:
        strings = ['4c', '3c', '2c', '1c']
        pathnames = []
        for str in strings:
            pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/ponticello_tremolo/' + 'Vn-pont_trem-' + note + '-' + dyn + '-' + str + '-N.wav')
            if os.path.exists(pathname):
                pathnames.append(pathname)
        pathname = random.choice(pathnames)
    elif orchideaNumber == 14:
        strings = ['4c', '3c', '2c', '1c']
        pathnames = []
        for str in strings:
            pathname = os.path.join(ORCHIDEASOL_PATH, 'Strings/Violin/tremolo/' + 'Vn-trem-' + note + '-' + dyn + '-' + str + '-N.wav')
            if os.path.exists(pathname):
                pathnames.append(pathname)
        pathname = random.choice(pathnames)
    else:
        pd.error("orchideaViolin: orchideaNumber not in range")
        return None
            
    if not os.path.exists(pathname):
        pd.error("path does not exist: " + pathname)
        return None
    pd.out("next open " + pathname)
