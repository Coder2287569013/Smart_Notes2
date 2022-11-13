from PyQt5.QtWidgets import QApplication, QInputDialog
from smart import *
import json 

# notes = {
#     "Ласкаво просимо!": {
#         "text": "Це программа для створення заміток...",
#         "tegs": ["інструкція", "про программу"]
#     }
# }

# with open("notes.json", "w", encoding="utf-8") as file:
#     json.dump(notes, file)

app = QApplication([])

def show_note():
    t = win.listWidget_2.currentItem().text()
    win.textEdit.setText(notes[t]["text"])
    win.listWidget.clear()
    win.listWidget.addItems(notes[t]["tegs"])

def add_note():
    note_name, ok = QInputDialog.getText(win, "Додати замітку", "Назва замітки")
    if note_name != "" and ok:
        notes[note_name] = {"text": "", "tegs": ["", ""]}
        win.listWidget_2.addItem(note_name)

def save_note():
    note_name = win.listWidget_2.currentItem().text()
    text = win.textEdit.toPlainText()
    notes[note_name]["text"] = text
    print(notes)
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file)

def delete_note():
    note_name = win.listWidget_2.currentItem().text()
    win.listWidget_2.takeItem(win.listWidget_2.currentRow())
    del notes[note_name]
    with open("notes.json", "w", encoding="utf-8") as file:
        json.dump(notes, file)

with open("notes.json", "r", encoding="utf-8") as file:
    notes = json.load(file)
    
win = Ui_Form()
win.setupUi(win)
win.show()   

win.listWidget_2.addItems(notes.keys())
win.listWidget_2.itemClicked.connect(show_note)
win.pushButton_2.clicked.connect(add_note)
win.pushButton_3.clicked.connect(save_note)
win.pushButton.clicked.connect(delete_note)
app.exec_()