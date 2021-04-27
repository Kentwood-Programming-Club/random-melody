from typing import no_type_check
from random_note import randomNote
from music21 import *

def generate_melody(num, note_list):
    m = []
    for i in range(num):
        m.append(randomNote(note_list))
    converter.parse("tinynotation: 4/4 " + " ".join(m)).show()