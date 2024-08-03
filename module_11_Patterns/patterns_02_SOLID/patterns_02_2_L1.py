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


class WritableDocument(Document):
    def save_document(self, new_data, method):
        if method == 'rewrite':
            method = 'w'
        else:
            method = 'a'
        with open(self.filename, method) as file:
            file.write(new_data)


document = Document('documents/SOLID.txt')
print(document.open_document())
print()

wr_document = WritableDocument('documents/SOLID.txt')
print(wr_document.open_document())
print()
wr_document.save_document('new data', 'rewrite')
print(wr_document.open_document())
print()
wr_document.save_document('\nadded data', 'add data')
print(wr_document.open_document())
