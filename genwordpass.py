#! /usr/bin/env python

import sys, random, os
from PyQt5.QtWidgets import (QApplication, QWidget, QLabel, QTextEdit, QLineEdit, QPushButton, QComboBox, QVBoxLayout, QHBoxLayout, QAction, QMainWindow)
from PyQt5.QtGui import QFont

random.seed(a=None, version=2)

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
  numb = ''
  for c in range (5):
    roll = random.randint(1,6)
    numb = int( str(numb) + str(roll) )  #builds the string of 5 rolls
  return dictWord[numb]  #returns the dict word with the right number

#build list of words to return as result
def buildList(num_words):
    answerList = []
    for c in range (1, (num_words +1) ):
      answerList.append( rollDice() )
    return (answerList) 

class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)

        self.text_edit = QTextEdit(', '.join(buildList(3)))
        self.text_edit.setFont(QFont('Arial', 20))
        self.setFixedSize(600, 250)
        self.createMenu()
        self.show()
            
        self.update_button = QPushButton("Update")
        self.update_button.clicked.connect(self.updateText)

        self.word_count = QComboBox()
        self.word_count.addItems(["3", "4", "5", "6", "7", "8"])
        self.word_count.currentIndexChanged.connect(self.updateText)
        self.word_count.setCurrentIndex(1)
            
        h_box1 = QHBoxLayout()
        h_box1.addWidget(self.text_edit)

        h_box2 = QHBoxLayout()
        h_box2.addWidget(self.update_button)
        h_box2.addStretch(1)
        h_box2.addWidget(self.word_count)

        v_box = QVBoxLayout()
        v_box.addWidget(self.text_edit)
        v_box.addLayout(h_box1)
        v_box.addLayout(h_box2)
        
        central_widget.setLayout(v_box)


    def createMenu(self):
        exit_act = QAction('Exit', self)
        exit_act.setShortcut('Ctrl+Q')
        exit_act.triggered.connect(self.close)

        menu_bar = self.menuBar()

        file_menu = menu_bar.addMenu('File')
        file_menu.addAction(exit_act)

        
    def updateText(self):
        self.text_edit.setText(', '.join(buildList(int(self.word_count.currentText()))))


if __name__ == '__main__':
  app = QApplication(sys.argv)
  parse_wordlist()
  window = MyWindow()
  sys.exit(app.exec_())
