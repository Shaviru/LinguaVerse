try:
    from translate import Translator
    from colorama import Fore
    from iso639 import Lang, exceptions

    def translate(text, from_lang, to_lang):
        translator = Translator(from_lang=from_lang, to_lang=to_lang)
        Translation = translator.translate(text)
        print(Translation)

    input_source_lang = input("What language are you translating from (in words): ")
    input_target_lang = input("What language do you want to translate to (in words): ")
    translate_text = input("Enter the text you want to translate: ")

    lg = Lang(input_source_lang)
    source_lang = lg.pt1
    lg = Lang(input_target_lang)
    target_lang = lg.pt1
    translate(translate_text, source_lang, target_lang)

except exceptions.InvalidLanguageValue as err:
    print(Fore.RED + "\nAn error occurred. Check if the languages are spelt correctly and try again")
except:
    print(Fore.RED + "\nAn error occurred. Please try again.")
