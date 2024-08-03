import pickle


class MyPickler:

    def __init__(self, protocol=pickle.DEFAULT_PROTOCOL):
        # pickle.HIGHEST_PROTOCOL
        if protocol < 0 or protocol > 5:
            self.protocol = pickle.DEFAULT_PROTOCOL
        elif protocol == 0:
            self.protocol = pickle.HIGHEST_PROTOCOL
        else:
            self.protocol = protocol

    def pickle_data(self, data):
        pickled_data = pickle.dumps(data, self.protocol)
        return pickled_data

    def pickle_file(self, data, filename):
        with open(filename, 'wb') as file:
            pickle.dump(data, file, self.protocol)
        return "Произведен пиклинг в файл"


class MyUnPickler:

    @staticmethod
    def unpickle_data(pickled_data):
        unpickle_data = pickle.loads(pickled_data)
        return unpickle_data

    @staticmethod
    def unpickle_file(pickled_filename):
        with open(pickled_filename, 'rb') as file:
            unpickle_data = pickle.load(file)
        return unpickle_data
