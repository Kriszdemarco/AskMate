from collections import Counter
import string

def is_palindrome(text):
    text = word_cleaner(text)
    tr = text[::-1].lower() 
    if text.lower()==tr:
        return True
    return False



def is_isogram(text):
    text = word_cleaner(text)
    for letters in text.lower():
        if letters:
            if text.lower().count(letters)>1:
                return False
    return True
    

def is_pangram(text):
    text = word_cleaner(text)
    if set(text.lower()) == set(string.ascii_lowercase):
        return True
    return False




def is_anagram(text1, text2):
    if len(text1)!=len(text2):
        return False
    for i in set(text1):
        if text1.count(i)!=text2.count(i):
            return False
    return True


def is_blanagram(text1, text2):
    text1, text2 = word_cleaner(text1), word_cleaner(text2)
    text1=text1.lower()
    text2=text2.lower()
    if len(text1)!=len(text2):
        return False
    if len(set(text1)-set(text2))>1 and  len(set(text2)-set(text1))>1:
        return False
    return True



def word_cleaner(text):#levagja a szokozoket
    for i in text:
        if not i.isalpha():
            text = text.replace(i,"")
    return text

#pirnt(funkcionev(parameter-ek))