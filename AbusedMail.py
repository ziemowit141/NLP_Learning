class Mail:
    def __init__(self, filename):
        self.file = open("./books/{}".format(filename), "r")

    def get_string(self):
        text = ''
        for line in self.file:
            text += line

        return text
