from PyQt5.QtWidgets import *

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
group.setLayout(group_main_line)
main_line.addWidget(group)

main_line.addWidget(answer_btn)

window.setLayout((main_line))
window.show()
app.exec()