class Note(object):
    def __init__(self, content):
        self.content = content

    def add_content(self, stuff: str):
        self.content += stuff

    def remove_content(self):
        self.content= None
    
    def __add__(self, other):
        return self.content + other.content

    def __str__(self):
        return self.content

class NoteBook():
    def __init__(self, title: str):
        self.title = title
        self.pg = 0
        self.notes = {}

    def __str__(self):
        return self.title

    def add_note(self, note: Note):
        if self.pg < 300:
            self.pg+=1
            self.notes[self.pg] = note
        else:
            return "Notebook reached 300 pages max."

    def remove_note(self, pg):
        if pg in self.notes.keys():
            return self.notes.pop(pg)
        else:
            return "{0} doesn't have pg.{1}".format(self.title, self.pg)

    def view_all_notes(self):
        for page, note in self.notes.items():
            print ("pg.{}: {}".format(page,note))
         

    def count_page(self):
        return "<{}> is {} pages long".format(self.title, self.pg)


my_journal = NoteBook("Happy Day")

note_1 = Note('first note!!')
note_2 = Note('second day')

half_1 = Note("I'm half")
half_2 = Note("I'm half")
one = half_1 + half_2

my_journal.add_note(note_1)
my_journal.add_note(note_2)
my_journal.add_note(one)

my_journal.view_all_notes()
print(my_journal.count_page())
