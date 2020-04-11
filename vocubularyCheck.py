"""
This will be a simple program in which I can save the words I learned
Then whenever I need to practise this will randomly through words,
There will be examples and meanings saved with the words
"""
import json
import random
import os


class Words:

    def __init__(self, word, meaning, example1, example2=None, example3=None):
        self.word = word
        self.meaning = meaning
        self.example1 = example1
        self.example2 = example2
        self.example3 = example3

    def new_word_dic(self):
        """
        :This method constructs a dictionary for every word and returns
        """
        return {
            "word": self.word,
            "meaning": self.meaning,
            "example": [self.example1, self.example2, self.example3]
        }

    def show_word(self):
        """
        :just a show method to show the word you just added
        """
        print(10*" ", end='')
        print("\nWord: {}\nMeaning: {}\nexm:\n{} \n{}\n{}".format(self.word, self.meaning, self.example1, self.example2, self.example3))

    def __repr__(self):
        return "Word Object... This word is {}".format(self.word)

    def __str__(self):
        return "{} : {}".format(self.word, self.meaning)


def new_word():
    """
    :this function is used for adding new word to your word list
    """
    while True:
        os.system('cls')
        word = input("The word is : ")
        meaning = input("Meaning : ")
        example1 = input("example 1: ")
        example2 = input("example 2: ")
        example3 = input("example 3: ")

        w = Words(word, meaning, example1, example2, example3)
        word_dic = w.new_word_dic()    # calling the new_word_dic() method for creating the dic for this word
        add_new_word_jason_file(word_dic)  # sending the word dic to the json file
        os.system('cls')
        print("\nYou have just added the following word: \n")
        w.show_word()

        x = input("\nDo you want to add more words? y or n\n")
        if x == "y":
            continue
        else:
            break


def add_new_word_jason_file(word_dic):
    """
    :adding the newly added words to the json file
    :first I'm opening the json file and loading it's data to a variable. It is saved as a python list.
    Then appending the new word dictionary to the python list. Then again dumping the list to the json file
    """

    with open('wordbook.json') as f:
        py_dic = json.load(f)
    py_dic.append(word_dic)

    with open('wordbook.json', 'w') as f:
        json.dump(py_dic, f)


def reading_from_json_file():
    """
    :This is simple, just opening the json file, loading it's data and returning the data
    """
    with open('wordbook.json') as f:
        data = json.load(f)
    return data


def practise():
    """
    :here I'm using random module to give user a random word from the list using the random number as the index.
        Then While loops to continuously running the process of practicing until user breaks the loop
    """
    data = reading_from_json_file()
    print(type(data))
    print(len(data))
    print("\n***Type 'exit' whenever you want to exit practicing***\n")
    while True:
        os.system('cls')
        r = random.randint(0, len(data) - 1)
        word = data[r]
        print("\nTry this word: \n")
        print(10*" ", end="")
        print(word["word"])
        print("\n")
        print("\nPress 1 : I got this one, move on..")
        print("Press 2 : Not sure, give me an example")
        print("Press 3 : Show me the meaning and uses\n")

        while True:
            choice = input()
            if choice == "1":
                break
            elif choice == "2":
                print(10 * " ", end="")
                print(word["example"].pop())
                now = input("\nHave you got this now? yes = y or no = n \n")
                if now == "y" or "yes":
                    break
                elif now == "n" or "no":
                    print(10 * " ", end="")
                    print("{} : {}\n".format(word["word"], word["meaning"]))
                    print(10 * " ", end="")
                    print("-> {}\n".format(word['example'].pop()))
                    print(10 * " ", end="")
                    print("-> {}\n".format(word['example'].pop()))
                    break
                else:
                    continue
            elif choice == "3":
                print(10 * " ", end="")
                print("{} : {}\n".format(word["word"], word["meaning"]))
                print(10 * " ", end="")
                print("-> {}\n".format(word['example'].pop()))
                print(10 * " ", end="")
                print("-> {}\n".format(word['example'].pop()))
                print(10 * " ", end="")
                print("-> {}\n".format(word['example'].pop()))
                break
            elif choice == 'exit':
                break
            else:
                print("\nPlease choose from any option pressing 1,2 or 3")
                continue
        print("\nPress enter to continue practicing..")
        print("Type 'exit' or 'e' to exit practicing")
        more = input()
        if more.lower() == "exit" or 'e':
            break
        else:
            continue


if __name__ == '__main__':
    os.system('cls')
    print(10 * " ", end="")
    print(10*"#")
    print(10 * " ", end="")
    print(" WordBook")
    print(10 * " ", end="")
    print(10 * "#")

    while True:
        option = input("##Press 1, to add new word\n##Press 2, for Practice\n(e for exit) ")

        if option == "1":
            new_word()
            os.system('cls')
        elif option == "2":
            practise()
            os.system('cls')
        elif option == "e":
            break




