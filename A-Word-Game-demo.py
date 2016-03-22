import time
import copy
import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = 8

SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}

WORDLIST_FILENAME = "words.txt"

def loadWords():
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	
def getWordScore(word, n):
    score=0
    for i in word:
        score+=SCRABBLE_LETTER_VALUES[i]
    score*=len(word) 
    if len(word)==n:
        score+=50  
    return score

def dealHand(n):
    hand={}
    numVowels = n / 3
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]
        hand[x] = hand.get(x, 0) + 1
        
    for i in range(numVowels, n):    
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

def updateHand(hand, word):
    hand2=hand.copy()
    for i in word:
        if i in hand2.keys():
            hand2[i]-=1
            
    return hand2

def calculateHandlen(hand):
    count=0
    for i in hand:
        count+=hand[i]
    return count

def compChooseWord(hand, wordList, n):
    bestWord="none"
    maxScore=0
    wo=[]
    for letter in hand.keys():
        for j in range(hand[letter]):
            wo.append(letter)
    
    for w in wordList:
        correct=True
        wo2=copy.copy(wo)
        for l in w:
            
            if l not in wo2:
                correct=correct and False
                break
            else:
                correct=correct and True
                wo2.remove(l)
                continue
            
        if correct==True:
            wordScore=getWordScore(w, n)
            if wordScore>maxScore:
                maxScore=wordScore
                bestWord=w
                
    return bestWord

def displayHandd(hand):
   
    l=""
    for letter in hand.keys():
        for j in range(hand[letter]):
             l=l+letter+' '             
    return l     

def isValidWord(word, hand, wordList):
    correct=True
    if word in wordList:
        hand2=hand.copy()
        word2=getFrequencyDict(word)
        for i in word2:
            if i in hand2:
                if hand2[i]-word2[i]>=0:
                    correct=correct and True
                else:
                    correct=correct and False
            else:
                correct=correct and False
    else:
        correct=False
        
    return correct


def playHand(hand, wordList, n):
    total=0
    while calculateHandlen(hand)>0:
        print ""
        print "Current Hand:  ",
        print displayHandd(hand)
        word=raw_input("Enter word, or a \".\" to indicate that you are finished: ")
        if word==".": 
            print "Goodbye! Total score: "+str(total)+" points."
            break
        else:
            if isValidWord(word, hand, wordList):
                score=getWordScore(word, n)
                total+=score
                print "\""+word+"\"",
                print " earned "+str(score)+" points. Total: "+str(total)+" points"
                hand=updateHand(hand, word)
                hand2=hand.copy()
                for i in hand2:
                    if hand2[i]==0:
                        del hand[i]
            else:
                print "Invalid word, please try again."
    if calculateHandlen(hand)==0:
        print ""
        print "Run out of letters. Total score: "+str(total)+" points."
   
    
def compPlayHand(hand, wordList, n):
    
    total=0
    
    while calculateHandlen(hand)>1:
        print "\nCurrent Hand:  ",
        print displayHandd(hand)
        word=compChooseWord(hand, wordList, n)
        if word=="none":
            print "Total score: "+str(total)+" points"
            break
        
        score=getWordScore(word, n)
        total+=score
        print "\""+word+"\" earned "+str(score)+" points. Total: "+str(total)+" points"
        hand=updateHand(hand, word)
        hand2=hand.copy()
        for i in hand2:
            if hand2[i]==0:
                del hand[i]
        
    if calculateHandlen(hand)==1:
        print "\nCurrent Hand:  ",
        print displayHandd(hand)
        print "Total score: "+str(total)+" points."
    elif calculateHandlen(hand)==0: 
        print "Total score: "+str(total)+" points."        

def playGame(wordList):
    hand={}
    do=True
    while do:
        
        inp=raw_input("Enter n to deal a new hand, r to replay the last hand, or e to end game: ")
        if inp=='n':
            do2=True
            while do2:
                inp2=raw_input("Enter u to have yourself play, c to have the computer play: ")
                if inp2=='u':
                    hand=dealHand(HAND_SIZE)
                    playHand(hand, wordList, HAND_SIZE)
                    do2=False
                elif inp2=='c':
                    hand=dealHand(HAND_SIZE)
                    compPlayHand(hand, wordList, HAND_SIZE)
                    do2=False
        elif inp=='r':
            if len(hand)==0:
                print "You have not played a hand yet. Please play a new hand first!"
            else:
                do2=True
                while do2:
                    inp2=raw_input("Enter u to have yourself play, c to have the computer play: ")
                    if inp2=='u':
                        playHand(hand, wordList, HAND_SIZE)
                        do2=False
                    elif inp2=='c':
                        compPlayHand(hand, wordList, HAND_SIZE)
                        do2=False
        elif inp=='e':
            do=False
        else:
            print "Invalid command."

if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)
    


