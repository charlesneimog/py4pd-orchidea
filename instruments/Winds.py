import pd
import os
import json

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
            


