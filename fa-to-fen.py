#A very simple script to convert Persian text to Fenglish

def convert_to_fenglish(input_text):
    farsi_mapping = {
        "ا": "a", "ب": "b", "پ": "p", "ت": "t", "ث": "s", "ج": "j", "چ": "ch", "ح": "h", "خ": "kh",
        "د": "d", "ذ": "z", "ر": "r", "ز": "z", "ژ": "zh", "س": "s", "ش": "sh", "ص": "s", "ض": "z",
        "ط": "t", "ظ": "z", "ع": "a", "غ": "gh", "ف": "f", "ق": "gh", "ک": "k", "گ": "g", "ل": "l",
        "م": "m", "ن": "n", "و": "v", "ه": "h", "ی": "i",
        "ّ": "", "ِ": "e", "ُ": "o", "َ": "a", "ٌ": "an", "ٍ": "en", "ً": "on", "ـ": ""
    }

    result = ""
    for char in input_text:
        fenglish_char = farsi_mapping.get(char, char)
        result += fenglish_char

    return result

input_text = input("Enter Farsi text: ")

converted_text = convert_to_fenglish(input_text)

print("Converted to Fenglish: " + converted_text)
