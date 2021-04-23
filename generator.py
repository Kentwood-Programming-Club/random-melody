from random_note import randomNote
from music21 import *
note_list = []
for i in range(10):
    note_list.append(randomNote())
    converter.parse("tinynotation: 4/4 " + " ".join(note_list)).show()
    print(note_list)