from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import*
from memo_app import app

txt_Question = QLineEdit('')
txt_Answer = QLineEdit('')
txt_Wrong1 = QLineEdit('')
txt_Wrong2 = QLineEdit('')
txt_Wrong3 = QLineEdit('')

layout_form = QFormLayout()

layout_form.addRow('Питання:', txt_Question)
layout_form.addRow('Правильна відповідь:',txt_Answer)
layout_form.addRow('Неправильна відповідь ',txt_Wrong1)
layout_form.addRow('Неправильний варіант ',txt_Wrong2)
layout_form.addRow('Неправильна відповідь ',txt_Wrong3)