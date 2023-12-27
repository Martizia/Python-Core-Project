class Note:
    def __init__(self, note_title, note_text, note_tags=''):
        self.note_title = note_title
        self.note_text = note_text
        self.note_tags = note_tags.split(' ')


