def strip_and_uppercase(text):
    return str(text).strip().upper()


text = '    jestem tekstem do zmiANny   '

print(text)

text = strip_and_uppercase(text)

print(text)