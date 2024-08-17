from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import *
from memo_app import app
#from memo_edit_layout import layout_from
#from memo_card_layout import layout_card

list_questions = QListView()
#Wdght_edit = QWidget()
#Wdght_edit.setLayout(layout_form)

btn_add = QPushButton('Нове запитання')
btn_delete = QPushButton('Видалити запитання')
btn_start = QPushButton('Почати тренування')

main_col1 = QVBoxLayout()
main_col1.addWidget(list_questions)
main_col1.addWidget(btn_add)

main_col2 = QVBoxLayout()
#main_col2.addWidget(wdght, edit)
test = QListView()
main_col2.addWidget(test)
main_col2.addWidget(btn_delete)

main_line1 = QHBoxLayout()
main_line1.addLayout(main_col1)
main_line1.addLayout(main_col2)

main_line2 = QHBoxLayout()
main_line2.addStretch(1)
main_line2.addWidget(btn_start, stretch=2)
main_line2.addStretch(1)

layout_main = QVBoxLayout()
layout_main.addLayout(main_line1)
layout_main.addLayout(main_line2)

screen = QWidget()
screen.setLayout(layout_main)
screen.show()
app.exec()
