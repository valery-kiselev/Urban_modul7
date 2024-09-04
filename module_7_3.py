class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punc = [',', '.', '=', '!', '?', ';', ':', ' - ']
        for i in self.file_names:
            with open(i, 'r', encoding='utf-8') as file:
                text_file = file.read().lower()
                for el in text_file:
                    if el in punc:
                        text_file = text_file.replace(el, '')
                    words = (text_file.split())
                    all_words[i] = words
                return all_words

    def find(self, word):
        dictionary = {}
        for key, words in self.get_all_words().items():
            if word.lower() in words:
                dictionary[key] = words.index(word.lower()) + 1
        return dictionary

    def count(self, word):
        dictionary = {}
        for key, words in self.get_all_words().items():
            dictionary[key] = words.count(word.lower())
        return dictionary


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего





