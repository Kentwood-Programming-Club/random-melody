from music21 import *
# Before you copy this for filling out the constants.py file, 
# consider if you really want to use EVERY note in the chromatic scale.
notes=[ 
    "c",
    "c#",
    "d",
    "d#",
    "e",
    "f",
    "f#",
    "g",
    "g#",
    "a",
    "a#",
    "b"
]

# number of semitones
major_steps = [2,2,1,2,2,2,1]
minor_steps = [2,1,2,2,1,3,1]

def scaleFromTonic(note, steps, note_type):
    i = notes.index(note)
    scale = []
    count = 0
    for s in steps:
        scale.append(notes[(i+count)%12] + str(note_type))
        count += s
    return scale

if __name__=="__main__":
    converter.parse("tinynotation: 4/4 " + " ".join(scaleFromTonic("c", major_steps, 4))).show()