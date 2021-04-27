import constants
import random
def randomNote():
    # Implement this
    note_name = constants.notes[random.randint(0,len(constants.notes)-1)]
    rhythm = str(2 ** (random.randint(1,4)))
    return note_name + rhythm

def randomNote(array):
    return array[random.randint(0,len(array)-1)] + str(2 ** random.randint(1,4))