#! /usr/bin/env python

import sys, random, os
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QVBoxLayout
from PyQt5.QtGui import QFont

random.seed(a=None, version=2)

#how many words wanted in result
global numberWords
numberWords = 5

#parse EFF Large wordlist into python dictionary
def parse_wordlist():
    global dictWord
    dictWord={}
    with open(os.path.join(sys.path[0], "eff_large_wordlist.txt"), "r") as f:
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

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.text_edit = QTextEdit(', '.join(buildList()))
        self.text_edit.setFont(QFont('Arial', 20))
        self.setGeometry(300, 300, 600, 250)
        
        self.update_button = QPushButton("Update")
        self.update_button.clicked.connect(self.updateText)

        layout = QVBoxLayout()
        layout.addWidget(self.text_edit)
        layout.addWidget(self.update_button)
        
        self.setLayout(layout)
        
        self.show()

    def updateText(self):
        self.text_edit.setText(', '.join(buildList()))

if __name__ == '__main__':
  app = QApplication(sys.argv)
  parse_wordlist()
  window = MyWindow()
  sys.exit(app.exec_())
