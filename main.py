from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QWidget

from memo_app import app
from memo_main_layout import*
from memo_edit_layout import*

window = QWidget()
window.setLayout(layout_main)

window.show()
app.exec()