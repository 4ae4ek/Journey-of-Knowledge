import re


def task_1(word):
    if word == word[::-1]:
        return 'is Palindrome'
    else:
        return 'not a Palindrome'


def task_2(string):
    return re.sub(' +', ' ', string)


print(task_1('alla'))
print(task_2('   rs   rq   '), 1)
