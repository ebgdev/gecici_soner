from icecream import ic
lst = ["kucuk","kazak","ada","soner","erfan"]

def isPalindorme(word):
    return word == word[::-1]
        
for word in lst:
    ic(word,isPalindorme(word))