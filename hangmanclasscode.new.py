from __future__ import print_function
word = ""
letter = ""
updatedSpaces = []
lives = 6

def initialize():
    word = "earring"
    print['_ _ _ _ _ _ _']

def getLetter():
    print('Guess a letter.')
    letter = raw_input()
    global letter
    
def won():
    if letter in word:
        print('Yay, you won!!') 
    if letter not in word:
        print(getLetter)      
        
          
                         
def main():
    initialize()
    getLetter()                

main()                      