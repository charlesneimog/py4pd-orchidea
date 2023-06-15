import pd
import os
import glob
import random
import json

# find where is this script

scriptPath = os.path.dirname(os.path.realpath(__file__))


# check if there is config.json inside the script folder
configPath = os.path.join(scriptPath, "config.json")
if not os.path.exists(configPath):
    pd.error("config.json not found, use the object [orchidea.config] to set the path to orchidea samples")

else:
    ORCHIDEASOL_PATH = json.load(open(configPath))["orchideaSolPath"]


FAMILY_STRINGS = ["violin", "viola", "cello", "contrabass"]
FAMILY_BRASS = ["trumpet", 'horn', "trombone", "tuba"]
FAMILY_WINDS = ["flute", "oboe", "clarinet", "bassoon", "saxophone"]
FAMILY_PLUCKED = ["guitar", "harp"]
FAMILY_KEYBOARD = ["accordion"]


def orchideaConfig(path):
    '''
    args:
        path:: str

    Set the path to orchidea samples.
    '''
    global ORCHIDEASOL_PATH
    ORCHIDEASOL_PATH = path
    json.dump({"orchideaSolPath": path}, open(configPath, "w"))




def orchideaFlute(note, dyn, orchideaNumber):
    '''
    Get the pathname for orchidea samples.

1 = Aeolian                                 
2 = Aeolian-and-Ordinario                   
3 = Discolored_fingering                    
4 = Flatterzunge                            
5 = Harmonic_fingering                      
6  = Jet_whistle
7  = key_click
8  = ordinario
9  = sforzato
10 = whistle_tones
    '''
    if orchideaNumber == 1:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/aeolian/' + 'Fl-aeol-' + note + '-' + dyn + '-N-N.wav')
    elif orchideaNumber == 2:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/aeolian_and_ordinario/' + 'Fl-aeol_and_ord-' + note + '-' + dyn + '-N-N.wav')
    elif orchideaNumber == 3:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/discolored_fingering/' + 'Fl-dsclrd_fngr-' + note + '-' + dyn + '-N-N.wav')
    elif orchideaNumber == 4:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/flatterzunge/' + 'Fl-flatt-' + note + '-' + dyn + '-N-N.wav')
    elif orchideaNumber == 5:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/harmonic_fingering/' + 'Fl-harm_fngr-' + note + '-' + dyn + '-N-N.wav')
    elif orchideaNumber == 6:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/jet_whistle/' + 'Fl-jet_wh-N-N-N-N.wav')
    elif orchideaNumber == 7:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/key_click/' + 'Fl-key_cl-' + note + '-' + dyn + '-N-N.wav')
    elif orchideaNumber == 8:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/ordinario/' + 'Fl-ord-' + note + '-' + dyn + '-N-N.wav')
    elif orchideaNumber == 9:
        pd.error("not implemented")
        return None
    elif orchideaNumber == 10:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/whistle_tones/' + 'Fl-whst_tn-' + note + '-' + dyn + '-N-N.wav')
    else:
        pd.error("not implemented")
        return None
    if not os.path.exists(pathname):
        pd.error("path does not exist: " + pathname)
        return None
    return pathname
            

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
        


    
        


    




def py4pdLoadObjects():
    pd.addobject(orchideaConfig, "orchidea.config")


    pd.addobject(orchideaFlute, "orchidea.flute")
    pd.addobject(orchideaViolin, "orchidea.violin")
    pd.addobject(orchideaTrumpet, "orchidea.trumpet")



