import random

from PyQt5.QtWidgets import *

import database

app = QApplication([])
window = QWidget()
menu_btn = QPushButton("Меню")
relax_bth = QPushButton("Відпочити")
timer_sbx = QSpinBox()
minute_lbl = QLabel("Хвилин")
question_lbl = QLabel("2+2?")
variant1_btn = QRadioButton("1")
variant2_btn = QRadioButton("2")
variant3_btn = QRadioButton("3")
variant4_btn = QRadioButton("4")
answer_btn = QPushButton("Відповісти")
next_question_btn =QPushButton("Наступне запитання")
res_lbl = QLabel("Результат")
group = QGroupBox("Варіанти відповідей")


main_line = QVBoxLayout()

horizontal_line1 = QHBoxLayout()
horizontal_line1.addWidget(menu_btn)
horizontal_line1.addStretch(1)
horizontal_line1.addWidget(relax_bth)
horizontal_line1.addWidget(timer_sbx)
horizontal_line1.addWidget(minute_lbl)
main_line.addLayout(horizontal_line1)
main_line.addWidget(question_lbl)



group_main_line = QVBoxLayout()
group_main_line.addWidget(variant1_btn)
group_main_line.addWidget(variant2_btn)
group_main_line.addWidget(variant3_btn)
group_main_line.addWidget(variant4_btn)
group_main_line.addWidget(res_lbl)
group.setLayout(group_main_line)
main_line.addWidget(group)

main_line.addWidget(answer_btn)
main_line.addWidget((next_question_btn))
answers = [variant1_btn,variant2_btn,variant3_btn,variant4_btn]


def set_quest():
    random.shuffle(answers)
    current_qustion = database.questions[database.nomer]
    question_lbl.setText(current_qustion["запитання"])
    answers[0].setText(current_qustion["Правильна відповідь"])
    answers[1].setText(current_qustion["Неправильна відповідь1"])
    answers[2].setText(current_qustion["Неправильна відповідь2"])
    answers[3].setText(current_qustion["Неправильна відповідь3"])
set_quest()

res_lbl.hide()
next_question_btn.hide()

def ans_func():
    if answers[0].isChecked():
        res_lbl.setText("Правильно")
    else:
        res_lbl.setText("Неправильно")
    answers[0].hide()
    answers[1].hide()
    answers[2].hide()
    answers[3].hide()
    res_lbl.show()
    next_question_btn.show()
    answer_btn.hide()

answer_btn.clicked.connect(ans_func)

window.setLayout((main_line))
window.show()
app.exec()