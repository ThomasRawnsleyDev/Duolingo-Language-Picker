from random import *

langs = open("Langs.txt", "r").read()
langs = langs.split("\n")
ignore = open("langignore.txt", "r").read()
ignore = ignore.split("\n")
print(f"Languages = {langs}")
print(f"Ignored languages = {ignore}")
print("   --- Duolingo language chooser ---   ")
def randomise(langs, ignore):
    chosen = randint(0, len(langs))
    for i in ignore:
        if langs[chosen - 1] == i:
            randomise(langs, ignore)
        else:
            print(f"Your chosen language is: {langs[chosen - 1]}")
            print(f"Language number: {chosen}")
            quit()

randomise(langs, ignore)