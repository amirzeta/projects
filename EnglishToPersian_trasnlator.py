from tabulate import tabulate   #for showing in tables
from googletrans import Translator  #usnig for translating the words or srntence

class Simple_Translator(object):
    def __init__(self, word, language):
        self.word = word
        self.language = language
        self.cursor = Translator(service_urls=["translate.google.com"])
    
    def __repr__(self):
        translated = self.cursor.translate(self.word, 
                            dest=self.language).text

        data = [["Language:", "Word or Sentence:"],
                ["English", self.word],
                ["Russian", str(translated)]]
        
        table = str(tabulate(data, headers="firstrow", tablefmt="grid"))#show in table
        return table

if __name__ == "__main__":
    translate = input(r"This is a simple EnglishToPersian trasnlator Enter word or Sentence In English: ")
    language = "ru"
    print(Simple_Translator(translate, language))
