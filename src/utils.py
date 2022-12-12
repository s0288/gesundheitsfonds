"""
Utility functions
"""
from pathlib import Path
import json


def get_project_root() -> Path:
    return Path(__file__).parent.parent
BASE_PATH = get_project_root()

def load_okr_json():
    with open(BASE_PATH / "data" / "raw" / "okrs.json") as f:
        d = json.load(f)
    return d

def get_check_in_msg(okrs: list):
    check_in_msg = "Wie geht es dir mit deinen Zielen?\n"
    check_in_msg += "Schreibe deine Antwort, indem du auf diese E-Mail antwortest.\n\n"
    check_in_msg += "Folgende Ziele hast du dir gesetzt:\n"
    
    for okr in okrs:
        check_in_msg += '- ' + okr["objective"] + '\n'
        for key_result in okr["key_results"]:
            check_in_msg += '  -- ' + key_result + '\n'
        check_in_msg += '\n'

    return check_in_msg
