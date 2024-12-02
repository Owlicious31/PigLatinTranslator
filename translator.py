import string


def is_valid(text):
    return text != " " and text not in string.punctuation and text not in string.digits


def get_words(text:str) -> list:
    """Returns the individual words in a string including spaces as separate words."""
    words = []
    individual_word = ""

    for character in text:
        if is_valid(character):
            individual_word += character

        else:
            words.append(individual_word)
            words.append(character)
            individual_word = ""

    words.append(individual_word)
    return words


def translate(text:str) -> str:
    """Translates words in a list into their pig latin equivalent and returns them as a combined string."""
    words = get_words(text)
    translated_text = ""
    new_words = []

    for word in words:
        if is_valid(word):
            first_letter = word[0]
            word = word[1:]
            word += f"{first_letter}ay"
            new_words.append(word.lower())
        else:
            new_words.append(word.lower())

    for word in new_words:
        translated_text += word

    return translated_text
