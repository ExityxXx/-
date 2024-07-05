class Note:
    def __init__(self, content):
        self.content = content

class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self, content):
        self.notes.append(Note(content))

    def display_notes(self):
        for index, note in enumerate(self.notes):
            print(f"Заметка {index + 1}: {note.content}")

def main():
    notebook = Notebook()
    while True:
        action = input("Введите 'добавить' для добавления заметки или 'показать' для отображения заметок: ")
        if action.lower() == 'добавить':
            content = input("Введите текст заметки: ")
            notebook.add_note(content)
        elif action.lower() == 'показать':
            notebook.display_notes()
        else:
            print("Неизвестная команда. Попробуйте снова.")

if __name__ == "__main__":
    main()
