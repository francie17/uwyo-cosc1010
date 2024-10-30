alphabet = {   
    'A':'._',
    'B':'_...',
    'C':'_._.',
    'D':'_..',
    'E':'.',
    'F':'.._.',
    'G':'__.',
    'H':'....',
    'I':'..',
    'J':'.___',
    'K':'_._',
    'L':'._..',
    'M':'__',
    'N':'_.',
    'O':'___',
    'P':'.__.',
    'Q':'__._',
    'R':'._.',
    'S':'...',
    'T':'_',
    'U':'.._',
    'V':'..._',
    'W':'.__',
    'X':'_.._',
    'Y':'_.__',
    'Z':'__..'
}

text_input = input("enter text for translation: ")


def morse_code(sentence):
   translation = ""
   for letter in sentence.upper():
        if letter.isalpha():
            translation += alphabet[letter] + " " 
        elif letter == " ":
            translation += " "
    return translation


text_output = morse_code(text_input)   
print(text_output)