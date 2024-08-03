class Article:

    def __init__(self, title, author, content_length, publication, description):
        self.article_data = {
            'title': title,
            'author': author,
            'content_length': content_length,
            'publication': publication,
            'description': description,
        }

    def get_data(self):
        return self.article_data

    def change_data(self, type_of_data, data):
        if type_of_data not in self.article_data.keys():
            return "Ошибочное поле"
        else:
            self.article_data[type_of_data] = data
