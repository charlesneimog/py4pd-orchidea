import glob
import json
import os
import random

import pd

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


def orchideaFlute(note, dyn, orchideaNumber):
    '''
    Get the pathname for orchidea samples.

    Orchidea Flute: 
        Args:
            note: string "A4"
            dyn: string "mf"
            orchideaNumber: int 1-10

        Techniques:
            Ordinario:
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
        dynamics = ['p']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be p.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/aeolian/' + 'Fl-aeol-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 2:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/aeolian_and_ordinario/' + 'Fl-aeol_and_ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 3:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/discolored_fingering/' + 'Fl-dsclrd_fngr-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 4:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/flatterzunge/' + 'Fl-flatt-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 5:
        dynamics = ['p', 'f']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be p or f.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/harmonic_fingering/' + 'Fl-harm_fngr-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 6:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/jet_whistle/' + 'Fl-jet_wh-N-N*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 7:        
        dynamics = ['f']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be f.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/key_click/' + 'Fl-key_cl-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 8:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/ordinario/' + 'Fl-ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 9:
        dynamics = ['f', 'fp']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be f or fp.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/sforzato/' + 'Fl-sfz-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)

    elif orchideaNumber == 10:
        dynamics = ['pp']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Flute/whistle_tones/' + 'Fl-whst_tn-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    else:
        pd.error("Wrong orchidea number, must be between 1 and 10.")
        return None
            

def orchideaOboe(note, dyn, orchideaNumber):    
    '''
    Get the pathname for orchidea samples.

    Orchidea Oboe: 
        Args:
            note: string "A4"
            dyn: string "mf"
            orchideaNumber: int 1-10

        Techniques:
            Ordinario:
                1. Blow without reed
                2. discolored_fingering
                3. flatterzunge
                4. harmonic_fingering
                5. key_click
                6. kiss
                7. ordinario
                8. sforzato
                9. vibrato

            Sordina:
                10. ordinario
    '''
    if orchideaNumber == 1:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Oboe/blow_without_reed/' + 'Ob-blow_no_reed-' + note + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 2:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Oboe/discolored_fingering/' + 'Ob-dsclrd_fngr-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
    elif orchideaNumber == 3:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Oboe/flatterzunge/' + 'Ob-flatt-' + note + '-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 4:
        dynamics = ['p', 'f']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be p or f.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Oboe/harmonic_fingering/' + 'Ob-harm_fngr-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 5:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Oboe/key_click/' + 'Ob-key_cl-' + note + '-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 6:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Oboe/kiss/' + 'Ob-kiss-' + note + '-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 7:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Oboe/ordinario/' + 'Ob-ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 8:
        dynamics = ['f', 'fp']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be f or fp.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Oboe/sforzato/' + 'Ob-sfz-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 9:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Oboe/vibrato/' + 'Ob-vib-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 10:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Oboe+sordina/ordinario/' + 'Ob+S-ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
        return random.choice(pathnames)
    else:
        pd.error("Wrong orchidea number, must be between 1 and 10.")
        return None


def orchideaClarinet(note, dyn, orchideaNumber):    
    '''
    Get the pathname for orchidea samples.

    Orchidea Clarinet: 
        Args:
            note: string "A4"
            dyn: string "mf"
            orchideaNumber: int 1-10

        Techniques:
                1. Aeolian and Ordinario
                2. Flatterzunge
                3. Flatterzunge High Register
                5. Key Click
                6. Ordinario
                8. Ordinario High Register
                9. Sforzato
    '''
    if orchideaNumber == 1:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Clarinet_Bb/aeolian_and_ordinario/' + 'ClBb-aeol_and_ord-' + note + '-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
        return random.choice(pathnames)
    elif orchideaNumber == 2:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Clarinet_Bb/flatterzunge/' + 'ClBb-flatt-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 3:
        dynamics = ['mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Clarinet_Bb/flatterzunge_high_register/' + 'ClBb-flatt_hi_reg-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 4:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Clarinet_Bb/key_click/' + 'ClBb-key_cl-' + note + '-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 5:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Clarinet_Bb/ordinario/' + 'ClBb-ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 6:
        dynamics = ['pp', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Clarinet_Bb/ordinario_high_register/' + 'ClBb-ord_hi_reg-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 7:
        dynamics = ['f', 'fp']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be f or fp.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Clarinet_Bb/sforzato/' + 'ClBb-sfz-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
        return random.choice(pathnames)
    else:
        pd.error("Wrong orchidea number, must be between 1 and 7.")
        return None
    

def orchideaBassoon(note, dyn, orchideaNumber):    
    '''
    Get the pathname for orchidea samples.

    Orchidea Bassoon: 
        Args:
            note: string "A4"
            dyn: string "mf"
            orchideaNumber: int 1-10

        Techniques:
            Ordinario:
                1. Blow Without Reed
                2. Flatterzunge
                3. Harmonic Fingering
                4. Key click
                5. Ordinario
                6. Sforzato
                7. Vibrato

            Sordina:
                8. Ordinario
    '''
    if orchideaNumber == 1:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Bassoon/blow_without_reed/' + 'Bn-blow_no_reed-' + note + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 2:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Bassoon/flatterzunge/' + 'Bn-flatt-' + note + '-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 3:
        dynamics = ['p', 'f']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be p or f.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Bassoon/harmonic_fingering/' + 'Bn-harm_fngr-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 4:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Bassoon/key_click/' + 'Bn-key_cl-' + note + '-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 5:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Bassoon/ordinario/' + 'Bn-ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 6:
        dynamics = ['f', 'fp']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be f or fp.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Bassoon/sforzato/' + 'Bn-sfz-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 7:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Bassoon/vibrato/' + 'Bn-vib-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 8:
        dynamics = ['mf']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Bassoon+sordina/ordinario/' + 'Bn+S-ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
        return random.choice(pathnames)
    else:
        pd.error("Wrong orchidea number, must be between 1 and 8.")
        return None


def orchideaSax(note, dyn, orchideaNumber):   
    '''
    Get the pathname for orchidea samples.

    Orchidea Bassoon: 
        Args:
            note: string "A4"
            dyn: string "mf"
            orchideaNumber: int 1-10

        Techniques:
            Ordinario:
                1. Aeolian
                2. bisbigliando
                3. blow_without_reed
                4. discolored_fingering
                5. double_tonguing
                6. flatterzunge
                7. harmonic_fingering
                8. key_click
                9. kiss
                10. ordinario
                11. ordinario high register
                12. sforzato
                13. slap pitched
                14. slap unpitched
    '''
    if orchideaNumber == 1:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/aeolian/' + 'ASax-aeol-' + note + '-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 2:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/bisbigliando/' + 'ASax-bisb-' + note + '-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 3:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/blow_without_reed/' + 'ASax-blow_no_reed*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return pathnames[0]
    elif orchideaNumber == 4:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/discolored_fingering/' + 'ASax-dsclrd_fngr-' + note + '-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 5:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/double_tonguing/' + 'ASax-dbl_tng-' + note + '-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 6:
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/flatterzunge/' + 'ASax-flatt-' + note + '-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 7:
        pd.logpost(3, "The note input is the harmonic with C#3")
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/harmonic_fingering/' + 'ASax-harm_fngr-C#3_' + note + '-*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 8:
        pathnames = glob.glob(os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/key_click/' + 'ASax-key_cl-' + note + '-*'))
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 9:
        pathnames = glob.glob(os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/kiss/' + 'ASax-kiss-*'))
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 10:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/ordinario/' + 'ASax-ord-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 11:
        dynamics = ['pp', 'mf', 'ff']
        if dyn not in dynamics:
            pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/ordinario_high_register/' + 'ASax-ord_hi_reg-' + note + '-' + dyn + '*')
        pathnames = glob.glob(pathname)
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 12:
        pathnames = glob.glob(os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/sforzato/' + 'ASax-sfz-' + note + '-*'))
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 13:
        dynamics = ['mf', 'f']
        pathnames = glob.glob(os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/slap_pitched/' + 'ASax-slap-' + note + '-' + dyn + '*'))
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 14:
        pathnames = glob.glob(os.path.join(ORCHIDEASOL_PATH, 'Winds/Sax_Alto/slap_unpitched/' + 'ASax-slap_unp-' + note + '-*'))
        if pathnames == []:
            pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    else:
        pd.error("Wrong orchidea number, must be between 1 and 14.")
        return None
    











