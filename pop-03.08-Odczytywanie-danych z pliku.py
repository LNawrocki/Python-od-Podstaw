# encoding opcjonalnie
file = None

try:
    file = open('test.txt', encoding='UTF-8')
    file_content = file.read()
    print(file_content)
except Exception:
    # Przepuszczenie/ukrycie wyjątku
    pass
finally:
    if file is not None:
        file.close()
