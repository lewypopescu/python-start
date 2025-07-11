from translate import Translator

translator = Translator(to_lang="nl")

try:
    with open('my_exercise1.txt', 'r+') as file:
        lines = file.readlines()
        print(lines)
        translations = [translator.translate(line) for line in lines]
        print(translations)
        file.write(
            f"\nHere is your translation in NL: {translations}.\nGood jobbb!")
        with open('my_exercise2.txt', 'w') as file2:
            file2.writelines(translations)
            print("Translations written to my_exercise2.txt")
except FileNotFoundError as err:
    print("File not found. Please ensure the file exists before trying to read it.")
    raise err
