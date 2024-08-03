class Document:
    def __init__(self, filename, data=None):
        self.filename = filename
        self.data = data

    def open_document(self):
        try:
            with open(self.filename, 'r') as file:
                self.data = file.read()
                return self.data
        except FileNotFoundError:
            return "Документ не найден!"

    def save_document(self, new_data, method):
        if method == 'rewrite':
            method = 'w'
        else:
            method = 'a'
        with open(self.filename, method) as file:
            file.write(new_data)


class ReadOnlyDocument(Document):
    def save_document(self, new_data, method):
        try:
            raise Exception
        except Exception:
            print("Только для чтения!")


document = Document('documents/NO_SOLID.txt')
print(document.open_document())
print()
document.save_document('new data', 'rewrite')
print(document.open_document())
print()
document.save_document('\nadded data', 'add data')
print(document.open_document())
print()
ro_document = ReadOnlyDocument('documents/NO_SOLID.txt')
ro_document.save_document('new document', 'rewrite')
