class PrinterQueue:
    def __init__(self, printer_queue: list = None):
        if printer_queue is None:
            self.__printer_queue = []
        else:
            self.__printer_queue = printer_queue

    def add_document(self, document_name):
        self.__printer_queue.append(document_name)
        return f"{document_name} помещен в очередь печати"

    # def print_document(self):
    #     if not self.__printer_queue:
    #         return "Очередь печати пуста"
    #     document = self.__printer_queue.pop(0)
    #     return f"Печать {document}...."

    def print_document(self):
        while self.__printer_queue:
            document = self.__printer_queue.pop(0)
            print(f"Печать {document}....")
        return "Очередь печати пуста"


hp_printer = PrinterQueue()
kyocera = PrinterQueue()

hp_printer.add_document("Отчет hp 1")
hp_printer.add_document("Отчет hp 2")
print(hp_printer.print_document())
print()

kyocera.add_document("Документ kyocera 1")
kyocera.add_document("Документ kyocera 2")
print(kyocera.print_document())

