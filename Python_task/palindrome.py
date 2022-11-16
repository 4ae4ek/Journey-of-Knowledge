# объявление функции
def is_palindrome(text):
    mass = [',', '.', '!', '?', '-', ' ']
    for i in mass:
        text = text.replace(i, '')
    text = text.lower()
    if text == text[::-1]:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))