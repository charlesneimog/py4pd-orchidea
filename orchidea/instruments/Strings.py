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


def orchideaViolin(note, dyn, orchideaNumber, **kwargs):
    """
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
    """

    string = kwargs.get("string", None)
    warning = kwargs.get("warning", False)

    if orchideaNumber == 1:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/artificial_harmonic/" + "Vn-art_harm-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 2:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Vn-art_harm_trem-G7-mf-2c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/harmonic_tremolo/" + "Vn-art_harm_trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 3:
        # Vn-behind_bridge-N-N-1c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/behind_the_bridge/" + "Vn-behind_bridge-N-N-*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 4:
        # behind_the_fingerboard
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/behind_the_fingerboard/" + "Vn-behind_fingerboard-N-N-*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 5:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/col_legno_battuto/" + "Vn-legno_batt-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 6:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/col_legno_tratto/" + "Vn-legno_tratto-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 7:
        # Vn-ord-A3-ff-4c-N
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/ordinario/" + "Vn-ord-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 8:
        # pizzicato_bartok Vn-pizz_bartok-A4-ff-3c-N
        dynamics = ["ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/pizzicato_bartok/" + "Vn-pizz_bartok-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 9:
        # Vn-pizz_lv-A3-ff-4c-N
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/pizzicato_l_vib" + "Vn-pizz_lv-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 10:
        # Vn-pizz_sec-A3-pp-4c-N
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/pizzicato_secco/" + "Vn-pizz_sec-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 11:
        # Vn-sfz-A4-f-3c-N
        dynamics = ["f", "fp"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be f or fp.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/sforzato/" + "Vn-sfz-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 12:
        # sul_ponticello
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Vn-pont-A4-mf-3c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/sul_ponticello/" + "Vn-pont-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 13:
        # sul_ponticello_tremolo
        # Vn-pont_trem-A5-mf-1c-N
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/sul_ponticello_tremolo/" + "Vn-pont_trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 14:
        # tremolo
        # Vn-trem-A4-ff-2c-N
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin/tremolo/" + "Vn-trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)

    # Violin+sordina
    elif orchideaNumber == 15:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        # Vn+S-ord-A3-ff-4c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin+sordina/ordinario/" + "Vn+S-ord-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)

    elif orchideaNumber == 16:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Vn+S-trem-G#6-ff-1c-R100d
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin+sordina/tremolo/" + "Vn+S-trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    # Violin+sordina_piombo
    elif orchideaNumber == 17:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Vn+SP-ord-A#3-mf-4c-T10u
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin+sordina_piombo/ordinario/" + "Vn+SP-ord-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    elif orchideaNumber == 18:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Vn+SP-trem-A#6-mf-4c-T10u
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violin+sordina_piombo/tremolo/" + "Vn+SP-trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1c, 2c, 3c, 4c] to select the string.",
            )
            pd.logpost(4, "send 'key string 1c' to select the string 1c")
        return random.choice(pathnames)
    else:
        if warning:
            pd.error("Wrong orchidea number, must be 1-18. Received: " + str(orchideaNumber))
        return None


def orchideaViola(note, dyn, orchideaNumber, **kwargs):
    """
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
                9. pizzicato_l_vib
                10. pizzicato_secco
                11. sforzato
                12. sul_ponticello
                13. sul_ponticello_tremolo
                14. sul_tasto_tremolo
                15. tremolo

            Sordina:
                16. ordinario
                17. tremolo

            Sordina Piombo:
                18. ordinario
                19. tremolo

    """
    string = kwargs.get("string", None)
    warning = kwargs.get("warning", False)
    if orchideaNumber == 1:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-art_harm-G6-mf-2c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/artificial_harmonic/" + "Va-art_harm-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 2:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-art_harm_trem-G6-mf-2c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/artificial_harmonic_tremolo/" + "Va-art_harm_trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 3:
        pathname = os.path.join(ORCHIDEASOL_PATH, "Strings/Viola/behind_the_bridge/" + "Va-behind_bridge*")
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 4:
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/behind_the_fingerboard/" + "Va-behind_fngrbrd*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 5:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-legno_batt-G#3-mf-4c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/col_legno_battuto/" + "Va-legno_batt-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 6:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-legno_tratt-G#3-mf-4c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/col_legno_tratto/" + "Va-legno_tratto-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 7:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        # Va-ord-A4-ff-1c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/ordinario/" + "Va-ord-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 8:
        dynamics = ["ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be ff.")
            return None
        # Va-pizz-A4-mf-1c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/pizzicato_bartok/" + "Va-pizz_bartok-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 9:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        # Va-pizz-A4-mf-1c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/pizzicato_l_vib/" + "Va-pizz_lv-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 10:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        # Va-pizz-A4-mf-1c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/pizzicato_secco/" + "Va-pizz_sec-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 11:
        dynamics = ["f", "fp"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be f or fp.")
            return None
        # Va-sul_A4-fp-1c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/sforzato/" + "Va-sfz-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 12:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-sul_A4-mf-1c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/sul_ponticello/" + "Va-pont-" + note + f"-{dyn}*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 13:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-sul_A4-mf-1c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/sul_ponticello_tremolo/" + "Va-pont_trem-" + f"{note}-{dyn}*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 14:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-tasto_trem-A#4-mf-2c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/sul_tasto_tremolo/" + "Va-tasto_trem-" + note + f"-{dyn}*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 15:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        # Va-trem-A4-mf-1c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola/tremolo/" + "Va-trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 16:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        # Va-trem_A4-mf-1c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola+sordina/ordinario/" + "Va+S-ord-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 17:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-trem_A4-mf-1c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola+sordina/tremolo/" + "Va+S-trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 18:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-trem_A4-mf-1c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola+sordina_piombo/ordinario/" + "Va+SP-ord-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    elif orchideaNumber == 19:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Va-trem_A4-mf-1c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Viola+sordina_piombo/tremolo/" + "Va+SP-trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1a, 2a, 3a, 4a] to select the string.",
            )
            pd.logpost(4, "send 'key string 1a' to select the string 1a")
        return random.choice(pathnames)
    else:
        if warning:
            pd.error("Wrong orchidea number.")
        return None


def orchideaCello(note, dyn, orchideaNumber, **kwargs):
    """
    Orchidea Cello:
        Args:
            note: string "A4"
            dyn: string "mf"
            orchideaNumber: int 1-15

        Techniques:
            Ordinario:
                1. artificial_harmonic
                2. artificial_harmonic_tremolo
                3. behind_the_bridge
                4. col_legno_battuno
                5. col_legno_tratto
                6. ordinario
                7. pizzicato_bartok
                8. pizzicato_l_vib
                9. pizzacto_secco
                10. sforzato
                11. sul_ponticello
                12. sul_ponticello_tremolo
                13. sul_tasto_tremolo
                14. tremolo

            Violoncello+sordina
                15. ordinario
                16. tremolo
    """
    string = pd.getkey("string")
    warning = kwargs.get("warning", False)
    if orchideaNumber == 1:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Vc-art_harm-G4-mf-3c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/artificial_harmonic/" + "Vc-art_harm-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1, 2, 3, 4] to select the string.",
            )
            pd.logpost(4, "send 'key string 1' to select the string 1")
        return random.choice(pathnames)
    elif orchideaNumber == 2:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Vc-art_harm_trem-G4-mf-3c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/artificial_harmonic_tremolo/" + "Vc-art_harm_trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1, 2, 3, 4] to select the string.",
            )
            pd.logpost(4, "send 'key string 1' to select the string 1")
        return random.choice(pathnames)
    elif orchideaNumber == 3:
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/behind_the_bridge/" + "Vc-behind_bridge-N-N*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 4:
        dynamics = ["mf"]
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/col_legno_battuto/" + "Vc-legno_batt-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 5:
        dynamics = ["mf"]
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/col_legno_tratto/" + "Vc-legno_tratto-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 6:
        dynamics = ["pp", "mf", "ff"]
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/ordinario/" + "Vc-ord-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 7:
        dynamics = ["ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/pizzicato_bartok/" + "Vc-pizz_bartok-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 8:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/pizzicato_l_vib/" + "Vc-pizz_lv-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 9:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/pizzicato_secco/" + "Vc-pizz_sec-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 10:
        dynamics = ["fp", "f"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be fp or f.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/sforzato/" + "Vc-sfz-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 11:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/sul_ponticello/" + "Vc-pont-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    elif orchideaNumber == 12:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/sul_ponticello_tremolo/" + "Vc-pont_trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    elif orchideaNumber == 13:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/sul_tasto_tremolo/" + "Vc-tasto_trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    elif orchideaNumber == 14:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello/tremolo/" + "Vc-trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    elif orchideaNumber == 15:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello+sordina/ordinario/" + "Vc+S-ord-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    elif orchideaNumber == 16:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello+sordina/tremolo/" + "Vc+S-trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    elif orchideaNumber == 17:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello+sordina_piombo/ordinario/" + "Vc+SP-ord-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    elif orchideaNumber == 18:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Violoncello+sordina_piombo/tremolo/" + "Vc+SP-trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    else:
        if warning:
            pd.error("Wrong orchidea number, must be between 1 and 18.")
        return None


def orchideaContrabass(note, dyn, orchideaNumber, **kwargs):
    """
    Orchidea Contrabass:
        Args:
            note: string "A4"
            dyn: string "mf"
            orchideaNumber: int 1-16

        Techniques:
            Ordinario:
                1. artificial_harmonic
                2. artificial_harmonic_tremolo
                3. behind_the_bridge
                4. col_legno_battuno
                5. col_legno_tratto
                6. ordinario
                7. pizzicato_bartok
                8. pizzicato_l_vib
                9. pizzacto_secco
                10. sforzato
                11. sul_ponticello
                12. sul_ponticello_tremolo
                13. sul_tasto_tremolo
                14. tremolo

            Contrabass+sordina
                15. ordinario
                16. tremolo
    """
    string = kwargs.get("string", None)
    warning = kwargs.get("warning", False)
    if orchideaNumber == 1:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Cb-art_harm-G4-mf-3c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/artificial_harmonic/" + "Cb-art_harm-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1, 2, 3, 4] to select the string.",
            )
            pd.logpost(4, "send 'key string 1' to select the string 1")
        return random.choice(pathnames)
    elif orchideaNumber == 2:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        # Cb-art_harm_trem-G4-mf-3c-N
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/artificial_harmonic_tremolo/" + "Cb-art_harm_trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        else:
            pd.logpost(
                4,
                "I recommend to send one message with string [1, 2, 3, 4] to select the string.",
            )
            pd.logpost(4, "send 'key string 1' to select the string 1")
        return random.choice(pathnames)
    elif orchideaNumber == 3:
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/behind_the_bridge/" + "Cb-behind_bridge-N-N*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 4:
        dynamics = ["mf"]
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/col_legno_battuto/" + "Cb-legno_batt-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 5:
        dynamics = ["mf"]
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/col_legno_tratto/" + "Cb-legno_tratto-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 6:
        dynamics = ["pp", "mf", "ff"]
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/ordinario/" + "Cb-ord-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 7:
        dynamics = ["ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/pizzicato_bartok/" + "Cb-pizz_bartok-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        return random.choice(pathnames)
    elif orchideaNumber == 8:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/pizzicato_l_vib/" + "Cb-pizz_lv-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 9:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/pizzicato_secco/" + "Cb-pizz_sec-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 10:
        dynamics = ["fp", "f"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be fp or f.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/sforzato/" + "Cb-sfz-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
        return random.choice(pathnames)
    elif orchideaNumber == 11:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/sul_ponticello/" + "Cb-pont-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    elif orchideaNumber == 12:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/sul_ponticello_tremolo/" + "Cb-pont_trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    elif orchideaNumber == 13:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/sul_tasto_tremolo/" + "Cb-tasto_trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    elif orchideaNumber == 14:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass/tremolo/" + "Cb-trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    elif orchideaNumber == 15:
        dynamics = ["pp", "mf", "ff"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be pp, mf or ff.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass+sordina/ordinario/" + "Cb+S-ord-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    elif orchideaNumber == 16:
        dynamics = ["mf"]
        if dyn not in dynamics:
            if warning:
                pd.error("Wrong dynamic, must be mf.")
            return None
        pathname = os.path.join(
            ORCHIDEASOL_PATH,
            "Strings/Contrabass+sordina/tremolo/" + "Cb+S-trem-" + note + "-" + dyn + "*",
        )
        pathnames = glob.glob(pathname)
        if pathnames == []:
            if warning:
                pd.error("Sample not found.")
            return None
        if string is not None:
            pathnames = [path for path in pathnames if string in path]
            if pathnames == []:
                if warning:
                    pd.error("This note not exist with string" + string + ".")
        return random.choice(pathnames)
    else:
        if warning:
            pd.error("Wrong orchidea number, must be between 1 and 16.")
        return None
