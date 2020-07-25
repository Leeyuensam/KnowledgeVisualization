import spacy


class findAllTitle:
    def __init__(self):
        self.nlp = spacy.load('en_core_web_sm')

    def find_similar_title(self, title, title_list):
        target = self.nlp(title)
        title_list.remove(title)
        tup_list = [(i, target.similarity(self.nlp(i))) for i in title_list]
        list2 = sorted(tup_list, key=lambda x: x[1], reverse=True)
        return [x[0] for x in list2[:10]]

