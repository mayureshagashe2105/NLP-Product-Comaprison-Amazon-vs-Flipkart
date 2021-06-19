class TextFormatting:
    def __init__(self, text):
        self.text = text
        self.unique_dict = {}

    def RemoveStopWords(self, stopwords=None, omit=None):
        stop_words = ['the', 'a', 'and', 'is', 'be', 'will', 'was', 'etc', 'an', 'https']
        if stopwords is not None:
            for i in stopwords:
                stop_words.append(i)

        if omit is not None:
            for i in omit:
                stop_words.remove(i)

        #print(f'Removing following stop words: {stop_words}')
        words = self.text.split(" ")
        doc1 = ""
        for i in words:
            if i not in stop_words:
                doc1 = doc1 + " " + i

        self.text = doc1
        self.TextTruncate()

    def RemoveTagsAndPunctuations(self, punctuation=None, omit=None):
        punctuations = r'''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        if punctuation is not None:
            for i in punctuation:
                punctuations += i

        if omit is not None:
            for i in omit:
                punctuations = punctuations.replace(i, "")

        #print(f'Removing following Punctuations: {punctuations}')
        for i in self.text:
            if i in punctuations:
                self.text = self.text.replace(i, "")

    def ToLower(self):
        self.text = self.text.lower()

    def CreateUniqueid(self):
        self.ToLower()
        unique_dict = {}
        li = list(set(self.text.split(" ")))
        li.sort()
        for i, word in enumerate(li):
            self.unique_dict.update({word: i})

    def TextTruncate(self):
        for i in self.text:
            if i == " ":
                self.text = self.text.replace(i, "", 1)
            else:
                break