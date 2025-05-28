from icecream import ic
lst = ["kucuk","kazak","ada","soner","erfan"]

def isPalindorme(word):
    return word == word[::-1]
        
for word in lst:
    ic(word,isPalindorme(word))



def gt_3(astr):
    res = []
    if len(astr)>3:
        res.append(astr)
    return res

for astr in lst:
    ic(gt_3(astr))
    
print('hello world')