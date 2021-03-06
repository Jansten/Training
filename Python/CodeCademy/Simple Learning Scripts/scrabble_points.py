# scrabble_score.py
# 2016-09-09, Michael Hannon
# User enters a string, gets the Scrabble score of the string returned
# Written as part of a CodeCademy course

score = {"a": 1, "c": 3, "b": 3, "e": 1, "d": 2, "g": 2, 
         "f": 4, "i": 1, "h": 4, "k": 5, "j": 8, "m": 3, 
         "l": 1, "o": 1, "n": 1, "q": 10, "p": 3, "s": 1, 
         "r": 1, "u": 1, "t": 1, "w": 4, "v": 4, "y": 4, 
         "x": 8, "z": 10}
         
word = raw_input("Enter a word: ")
def scrabble_score(word):
    point = 0
    for i in word.lower():
        if i in score:
            point += score[i]
    return point
    
print scrabble_score(word)