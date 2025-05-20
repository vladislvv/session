
import os

RECORD_FILE = "record.txt"

def load_record():
    if os.path.exists(RECORD_FILE):
        with open(RECORD_FILE, "r") as f:
            try:
                return int(f.read())
            except ValueError:
                return 0
    return 0

def save_record(score):
    with open(RECORD_FILE, "w") as f:
        f.write(str(score))
