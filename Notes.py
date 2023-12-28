class Note:
    def __init__(self, note_title, note_text, note_tags=''):
        self.note_title = note_title
        self.note_text = note_text
        self.note_tags = note_tags.split(' ')

    def add_tag(self, new_tag):
        self.note_tags.append(new_tag)

    def edit_tag(self, old_tag, new_tag):
        for i, p in enumerate(self.note_tags):
            if p == old_tag:
                self.note_tags[i] = new_tag

    def delete_tag(self, tag_to_delete):
        for tag in self.note_tags:
            if tag == tag_to_delete:
                self.note_tags.remove(tag_to_delete)
