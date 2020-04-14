"""
:Simple word dictionary. All resources will be created by user.
:Using sqlite for storing the data
:User can add words with their meaning and example
:Later user will be able to practise
"""
import sqlite3
import random
import os


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
        print("word: {}\nmeaning: {}\nexample -> {}\n        -> {}\nsyn : {}\nant : {}".format(self.word,
                                                                                               self.meaning,
                                                                                               self.example1,
                                                                                               self.example2,
                                                                                               self.syn,
                                                                                               self.ant))

    def __repr__(self):
        return "..Word object.. this word is : {}".format(self.word)

    def __str__(self):
        return "{}\n{}".format(self.word, self.meaning)


def add_new_word(connector, cursor):
    while True:
        os.system('cls')
        word = input("The word is : ").lower()
        meaning = input("Meaning : ")
        exm1 = input("Give a example: ")
        exm2 = input("Please give another one: ")
        syn = input("Synonyms : ")
        ant = input("Antonyms : ")

        new_word = Word(word, meaning, exm1, exm2, syn, ant)
        print("You have just added the following word to the database: ")
        new_word.show_current_word()

        adding_word_in_db(connector, cursor, new_word)

        more = input("Do you want to add more word?")
        if more == "n":
            break
        elif more == "y":
            continue


def adding_word_in_db(connector, cursor, word):

    with connector:
        cursor.execute('''CREATE TABLE IF NOT EXISTS words
                         (id integer primary key autoincrement, 
                          word text, 
                          meaning text, 
                          exm1 text, 
                          exm2 text, 
                          syn text, 
                          ant text)''')

    with connector:
        cursor.execute("INSERT INTO words VALUES" 
                       "(?,?,?,?,?,?,?)",
                       (None,
                        word.word,
                        word.meaning,
                        word.example1,
                        word.example2,
                        word.syn,
                        word.ant))


def show_word(tup_word):
    print("word : {}\nmeaning : {}\nexample : \n{}\n{}\nsynonym : {}\nantonym : {}"
          .format(tup_word[1], tup_word[2], tup_word[3], tup_word[4], tup_word[5], tup_word[6]))


def delete_word(connector, cursor):
    del_word = input("Type in the word you want to delete: ").lower()
    with connector:
        cursor.execute("SELECT word FROM words WHERE word = ?", (del_word,))
        if cursor.fetchone() is None:
            print("The word \'{}\' is not in the wordbook!".format(del_word))
        else:
            cursor.execute("DELETE FROM words WHERE word = ?", (del_word,))
            print("The word \'{}\' has been deleted".format(del_word))


def find_word(connector, cursor):
    while True:
        find = input("Type in the word fo find: ").lower()
        with connector:
            cursor.execute("SELECT word FROM words WHERE word = ?", (find,))
            if cursor.fetchone() is None:
                print("The word \'{}\' is not in the wordbook!".format(find))
            else:
                cursor.execute("SELECT * FROM words WHERE word = ?", (find,))
                list_rows = cursor.fetchall()
                tup = list_rows[0]
                show_word(tup)
        more = input("Need to find more?")
        if more == "y":
            continue
        elif more == "n":
            os.system('cls')
            break


def practise():
    pass


def check_duplicate():
    pass


if __name__ == '__main__':
    os.system('cls')
    print(10 * " ", end="")
    print(10 * "#")
    print(10 * " ", end="")
    print(" WordBook")
    print(10 * " ", end="")
    print(10 * "#")

    conn = sqlite3.connect("wordbook.db")
    c = conn.cursor()

    while True:
        option = input("##Press 1, to Add new word\n"
                       "##Press 2, for Practice\n"
                       "##Press 3 for Delete a word\n"
                       "##Press 4 for Find a word\n"
                       "(e for exit) ")

        if option == "1":
            add_new_word(conn, c)
            os.system('cls')
        elif option == "2":
            practise()
            os.system('cls')
        elif option == "3":
            delete_word(conn, c)

        elif option == "4":
            os.system('cls')
            find_word(conn, c)

        elif option == "e":
            break

    c.close()
