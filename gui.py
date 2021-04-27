from functools import partial
import tkinter as tk
import generator

class MelodyGenerator(tk.Tk):
    def toggle_note(self, n):
        index = -1
        try:
            list_notes = self.note_selection.get(0, self.note_selection.size()-1)
            index = list_notes.index(n)
            self.note_selection.delete(index)
        except ValueError as e:
            # note isn't enabled
            self.note_selection.insert(0, n)

    def start_generation(self, n, list):
        if len(list) < 1:
            return
        else:
            generator.generate_melody(n, list)

    def __init__(self):
        super().__init__()
        self.geometry("400x300")
        self.all_notes = ["c","c#","d","d#","e","f","f#","g","g#","a","a#","b"]
        self.valid_notes = self.all_notes.copy()

        self.melody=[]

        self.title("Random Melody Generator")

        tk.Label(self, text="Notes to use").grid(row=0, column=0)

        self.note_selection = tk.Listbox(self)
        self.note_selection.grid(row=1, column=0)

        i = 0
        for note in self.all_notes:
            self.note_selection.insert(i, note)
            b = tk.Button(self, text=note, command=partial(self.toggle_note, note))
            b.grid(row=1, column=i+1)
            i += 1
    
        self.melody_length = tk.Entry(self)
        self.melody_length.grid(row=2,column=0)
        
        self.submit_button = tk.Button(self, 
            text="Start", 
            command=lambda: self.start_generation(
                int(self.melody_length.get()), 
                self.note_selection.get(0,self.note_selection.size()-1)
            )
        )
        self.submit_button.grid(row=3,column=0)
