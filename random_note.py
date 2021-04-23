from constants import notes
import random
def randomNote():
    # Implement this
    note_name = notes[random.randint(0,len(notes))]
    rhythm = str(2 ** (random.randint(1,4)))
    return note_name + rhythm