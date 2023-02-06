#! /usr/bin/env python

import sys, random
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QTextEdit, QLineEdit
from PyQt5.QtGui import QFont

random.seed(a=None, version=2)

#how many words wanted in result
global numberWords
numberWords = 4

#parse EFF Large wordlist into python dictionary
def parse_wordlist():
    global dictWord
    dictWord={}
    with open('eff_large_wordlist.txt') as f:
      for line in f:
        (key, val) = line.split()
        dictWord[int(key)] = val

#roll die x 5 times, then lookup the dictionary resulting word
def rollDice():
  global roll
  numb = ''
  for c in range (5):
    roll = random.randint(1,6)
    numb = int( str(numb) + str(roll) )  #builds the string of 5 rolls
  return dictWord[numb]  #returns the dict word with the right number

#build list of words to return as result
def buildList():
    answerList = []
    for c in range (1, (numberWords +1) ):
      answerList.append( rollDice() )
    return (answerList) 

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle("Generate Wordlist Password")

        self.text_edit = QTextEdit(', '.join(buildList()))
        self.text_edit.setFont(QFont('Arial', 20))
        #self.line_edit.setFrame(1)
        self.setCentralWidget(self.text_edit)
        
        self.show()

if __name__ == '__main__':
  app = QApplication(sys.argv)
  parse_wordlist()
  window = MyWindow()
  sys.exit(app.exec_())
