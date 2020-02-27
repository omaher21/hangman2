from __future__ import print_function
word = ""
updatedSpaces = []
lives = 6

def main():
    initialize()
    getLetter()
    check() 

def initialize():
    global word
    word = input("Type your word here: ")
    lenW = len(word)
    while lenW != 0:
        updatedSpaces.append('-')
        lenW-=1

def getLetter():
    global letter
    global word
    global letter
    letter = input("Guess a letter here: ")
    check()
    
def check():
    ''' find the index of the word and replace it with the correct index from the list'''
    global word
    global updatedSpaces
    global lives
    lives = 6
    if letter in word:
        i = (word.find(letter))
        del (updatedSpaces[i])
        updatedSpaces.insert(i,letter)
        if i != len(word)-1:
            e = word.find(letter, i+1, len(word)+ 1)
            if e != -1:
                del (updatedSpaces[e])
                updatedSpaces.insert(e,letter)
                if e != len(word)-1:
                    a = word.find(letter, e+1, len(word)+1)
                    if a != -1:
                        del (updatedSpaces[a])
                        updatedSpaces.insert(a,letter)
  
    if letter not in word:
        print ('Sorry not the right letter, try again')
        lives-=1
        print ('You have',lives,'lives left')
    won()
    
def won():
    global lives
    print (updatedSpaces)
    if '-' not in updatedSpaces:
        print("Congratulations! the correct word was", word, "nice job!")
    else:
        getLetter()      

main()                      