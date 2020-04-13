"""
:Simple word dictionary. All resources will be created by user.
:Using sqlite for storing the data
:User can add words with their meaning and example
:Later user will be able to practise
"""
import sqlite3
import random


class Word:

    """
    :this class is the basic structure for the words.
    """
    def __init__(self, word, meaning, example1, example2, syn, ant):
        self.word = word
        self.meaning = meaning
        self.example1 = example1
        self.example2 = example2
        self.syn = syn
        self.ant = ant

    def show_current_word(self):
        print("word: {}\nmeaning: {}\nexp -> {}\n      -> {}\nsyn : {}\nant : {}".format(self.word,
                                                                                         self.meaning,
                                                                                         self.example1,
                                                                                         self.example2,
                                                                                         self.syn,
                                                                                         self.ant))

    def __repr__(self):
        return "..Word object.. this word is : {}".format(self.word)

    def __str__(self):
        return "{}\n{}".format(self.word, self.meaning)


def add_new_word():
    while True:
        word = input("The word is : ")
        meaning = input("Meaning : ")
        exm1 = input("Give a example: ")
        exm2 = input("Please give another one: ")
        syn = input("Synonyms : ")
        ant = input("Antonyms : ")

        new_word = Word(word, meaning, exm1, exm2, syn, ant)
        return new_word



                
def adding_word_in_db():
    word = add_new_word()

    conn = sqlite3.connect(':memory:')
    c = conn.cursor()

    c.execute('''CREATE TABLE words
                 (id integer primary key autoincrement, 
                  word text, 
                  meaning text, 
                  exm1 text, 
                  exm2 text, 
                  syn text, 
                  ant text)''')

    c.execute("INSERT INTO words VALUES"
              "(?,?,?,?,?,?,?)",
              (None,
               word.word,
               word.meaning,
               word.example1,
               word.example2,
               word.syn,
               word.ant))

    conn.commit()
    c.execute("SELECT * FROM words")
    print(c.fetchall())
    conn.close()


adding_word_in_db()
