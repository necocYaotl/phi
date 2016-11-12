import os, sys, random

folderPath = os.path.dirname(__file__)
wordPath = os.path.join(folderPath, 'static/hanging')
wordFile = os.path.join(wordPath,'words2.txt')

def loadWords():
    """ reads text files, returns a list."""
    inFile = open(wordFile, 'r')
    wordlist = []
    for line in inFile:
        wordlist.append(line)
    return wordlist

def chosen():
    """ gets a list, gives a random member of it."""
    wordList = loadWords()
    w = random.choice(wordList)
    word = w[:-1]
    return word

def dissect(word):
    letters = []
    for c in word:
        letters.append(c)
    return letters


def valid(letter, word):
    try:
        int(letter)
        return "numMock"
    except:
        if len(letter) > 1:
            if letter == word:
                return "compWin"
            else:
                return "compMock"

        for l in word:
            if letter == l:
                return "right"

        return "wrong"


def hangedMan(wrg):
    man0 ="""
  ##############
  ##############
  ##          ##
  ##
  ##
  ##
  ##
  ##
  ##
  ##
  ##
##############
##############"""

    man1 ="""
  ##############
  ##############
  ##          ##
  ##           o
  ##
  ##
  ##
  ##
  ##
  ##
  ##
##############
##############"""

    man2 ="""
  ##############
  ##############
  ##          ##
  ##           o
  ##           |
  ##
  ##
  ##
  ##
  ##
  ##
##############
##############"""

    man3 ="""
  ##############
  ##############
  ##          ##
  ##           o
  ##          /|
  ##
  ##
  ##
  ##
  ##
  ##
##############
##############"""

    man4 ="""
  ##############
  ##############
  ##          ##
  ##           o
  ##          /|\\
  ##
  ##
  ##
  ##
  ##
  ##
##############
##############"""

    man5 ="""
  ##############
  ##############
  ##          ##
  ##           o
  ##          /|\\
  ##          /
  ##
  ##
  ##
  ##
  ##
##############
##############"""

    man6 ="""
  ##############
  ##############
  ##          ##
  ##           o
  ##          /|\\
  ##          / \\
  ##
  ##
  ##
  ##
  ##
##############
##############"""


    if wrg == 0:
        return man0
    elif wrg == 1:
        return man1
    elif wrg == 2:
        return man2
    elif wrg == 3:
        return man3
    elif wrg == 4:
        return man4
    elif wrg == 5:
        return man5
    elif wrg == 6:
        return man6
