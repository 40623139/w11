# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Y:\tmp\github\ag7\ag7\final_project\ui\Dialog.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(450, 500)
        Dialog.setMinimumSize(QtCore.QSize(450, 500))
        Dialog.setMaximumSize(QtCore.QSize(450, 500))
        Dialog.setSizeGripEnabled(True)
        self.gridLayout = QtWidgets.QGridLayout(Dialog)
        self.gridLayout.setObjectName("gridLayout")
        self.clearAllButton = QtWidgets.QPushButton(Dialog)
        self.clearAllButton.setMinimumSize(QtCore.QSize(0, 50))
        self.clearAllButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.clearAllButton.setFont(font)
        self.clearAllButton.setObjectName("clearAllButton")
        self.gridLayout.addWidget(self.clearAllButton, 1, 4, 1, 2)
        self.display = QtWidgets.QLineEdit(Dialog)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.display.setFont(font)
        self.display.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.display.setObjectName("display")
        self.gridLayout.addWidget(self.display, 0, 0, 1, 6)
        self.clearButton = QtWidgets.QPushButton(Dialog)
        self.clearButton.setMinimumSize(QtCore.QSize(0, 50))
        self.clearButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.clearButton.setFont(font)
        self.clearButton.setObjectName("clearButton")
        self.gridLayout.addWidget(self.clearButton, 1, 2, 1, 2)
        self.eight = QtWidgets.QPushButton(Dialog)
        self.eight.setMinimumSize(QtCore.QSize(59, 89))
        self.eight.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.eight.setFont(font)
        self.eight.setObjectName("eight")
        self.gridLayout.addWidget(self.eight, 2, 2, 1, 1)
        self.backspaceButton = QtWidgets.QPushButton(Dialog)
        self.backspaceButton.setMinimumSize(QtCore.QSize(0, 50))
        self.backspaceButton.setMaximumSize(QtCore.QSize(16777215, 50))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.backspaceButton.setFont(font)
        self.backspaceButton.setObjectName("backspaceButton")
        self.gridLayout.addWidget(self.backspaceButton, 1, 0, 1, 2)
        self.clearMemoryButton = QtWidgets.QPushButton(Dialog)
        self.clearMemoryButton.setMinimumSize(QtCore.QSize(59, 89))
        self.clearMemoryButton.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.clearMemoryButton.setFont(font)
        self.clearMemoryButton.setObjectName("clearMemoryButton")
        self.gridLayout.addWidget(self.clearMemoryButton, 2, 0, 1, 1)
        self.seven = QtWidgets.QPushButton(Dialog)
        self.seven.setMinimumSize(QtCore.QSize(59, 89))
        self.seven.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.seven.setFont(font)
        self.seven.setObjectName("seven")
        self.gridLayout.addWidget(self.seven, 2, 1, 1, 1)
        self.setMemoryButton = QtWidgets.QPushButton(Dialog)
        self.setMemoryButton.setMinimumSize(QtCore.QSize(59, 89))
        self.setMemoryButton.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.setMemoryButton.setFont(font)
        self.setMemoryButton.setObjectName("setMemoryButton")
        self.gridLayout.addWidget(self.setMemoryButton, 4, 0, 1, 1)
        self.nine = QtWidgets.QPushButton(Dialog)
        self.nine.setMinimumSize(QtCore.QSize(59, 89))
        self.nine.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.nine.setFont(font)
        self.nine.setObjectName("nine")
        self.gridLayout.addWidget(self.nine, 2, 3, 1, 1)
        self.squareRootButton = QtWidgets.QPushButton(Dialog)
        self.squareRootButton.setMinimumSize(QtCore.QSize(59, 89))
        self.squareRootButton.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.squareRootButton.setFont(font)
        self.squareRootButton.setObjectName("squareRootButton")
        self.gridLayout.addWidget(self.squareRootButton, 2, 5, 1, 1)
        self.four = QtWidgets.QPushButton(Dialog)
        self.four.setMinimumSize(QtCore.QSize(59, 89))
        self.four.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.four.setFont(font)
        self.four.setObjectName("four")
        self.gridLayout.addWidget(self.four, 3, 1, 1, 1)
        self.divisionButton = QtWidgets.QPushButton(Dialog)
        self.divisionButton.setMinimumSize(QtCore.QSize(59, 89))
        self.divisionButton.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.divisionButton.setFont(font)
        self.divisionButton.setObjectName("divisionButton")
        self.gridLayout.addWidget(self.divisionButton, 2, 4, 1, 1)
        self.timesButton = QtWidgets.QPushButton(Dialog)
        self.timesButton.setMinimumSize(QtCore.QSize(59, 89))
        self.timesButton.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.timesButton.setFont(font)
        self.timesButton.setObjectName("timesButton")
        self.gridLayout.addWidget(self.timesButton, 3, 4, 1, 1)
        self.five = QtWidgets.QPushButton(Dialog)
        self.five.setMinimumSize(QtCore.QSize(59, 89))
        self.five.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.five.setFont(font)
        self.five.setObjectName("five")
        self.gridLayout.addWidget(self.five, 3, 2, 1, 1)
        self.powerButton = QtWidgets.QPushButton(Dialog)
        self.powerButton.setMinimumSize(QtCore.QSize(59, 89))
        self.powerButton.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.powerButton.setFont(font)
        self.powerButton.setObjectName("powerButton")
        self.gridLayout.addWidget(self.powerButton, 3, 5, 1, 1)
        self.six = QtWidgets.QPushButton(Dialog)
        self.six.setMinimumSize(QtCore.QSize(59, 89))
        self.six.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.six.setFont(font)
        self.six.setObjectName("six")
        self.gridLayout.addWidget(self.six, 3, 3, 1, 1)
        self.readMemoryButton = QtWidgets.QPushButton(Dialog)
        self.readMemoryButton.setMinimumSize(QtCore.QSize(59, 89))
        self.readMemoryButton.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.readMemoryButton.setFont(font)
        self.readMemoryButton.setObjectName("readMemoryButton")
        self.gridLayout.addWidget(self.readMemoryButton, 3, 0, 1, 1)
        self.one = QtWidgets.QPushButton(Dialog)
        self.one.setMinimumSize(QtCore.QSize(59, 89))
        self.one.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.one.setFont(font)
        self.one.setObjectName("one")
        self.gridLayout.addWidget(self.one, 4, 1, 1, 1)
        self.two = QtWidgets.QPushButton(Dialog)
        self.two.setMinimumSize(QtCore.QSize(59, 89))
        self.two.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.two.setFont(font)
        self.two.setObjectName("two")
        self.gridLayout.addWidget(self.two, 4, 2, 1, 1)
        self.three = QtWidgets.QPushButton(Dialog)
        self.three.setMinimumSize(QtCore.QSize(59, 89))
        self.three.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.three.setFont(font)
        self.three.setObjectName("three")
        self.gridLayout.addWidget(self.three, 4, 3, 1, 1)
        self.minusButton = QtWidgets.QPushButton(Dialog)
        self.minusButton.setMinimumSize(QtCore.QSize(59, 89))
        self.minusButton.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.minusButton.setFont(font)
        self.minusButton.setObjectName("minusButton")
        self.gridLayout.addWidget(self.minusButton, 4, 4, 1, 1)
        self.addToMemoryButton = QtWidgets.QPushButton(Dialog)
        self.addToMemoryButton.setMinimumSize(QtCore.QSize(59, 89))
        self.addToMemoryButton.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.addToMemoryButton.setFont(font)
        self.addToMemoryButton.setObjectName("addToMemoryButton")
        self.gridLayout.addWidget(self.addToMemoryButton, 5, 0, 1, 1)
        self.reciprocalButton = QtWidgets.QPushButton(Dialog)
        self.reciprocalButton.setMinimumSize(QtCore.QSize(59, 89))
        self.reciprocalButton.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.reciprocalButton.setFont(font)
        self.reciprocalButton.setObjectName("reciprocalButton")
        self.gridLayout.addWidget(self.reciprocalButton, 4, 5, 1, 1)
        self.zero = QtWidgets.QPushButton(Dialog)
        self.zero.setMinimumSize(QtCore.QSize(59, 89))
        self.zero.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.zero.setFont(font)
        self.zero.setObjectName("zero")
        self.gridLayout.addWidget(self.zero, 5, 1, 1, 1)
        self.dot = QtWidgets.QPushButton(Dialog)
        self.dot.setMinimumSize(QtCore.QSize(59, 89))
        self.dot.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.dot.setFont(font)
        self.dot.setObjectName("dot")
        self.gridLayout.addWidget(self.dot, 5, 2, 1, 1)
        self.plusButton = QtWidgets.QPushButton(Dialog)
        self.plusButton.setMinimumSize(QtCore.QSize(59, 89))
        self.plusButton.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.plusButton.setFont(font)
        self.plusButton.setObjectName("plusButton")
        self.gridLayout.addWidget(self.plusButton, 5, 4, 1, 1)
        self.changeSignButton = QtWidgets.QPushButton(Dialog)
        self.changeSignButton.setMinimumSize(QtCore.QSize(59, 89))
        self.changeSignButton.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.changeSignButton.setFont(font)
        self.changeSignButton.setObjectName("changeSignButton")
        self.gridLayout.addWidget(self.changeSignButton, 5, 3, 1, 1)
        self.equalButton = QtWidgets.QPushButton(Dialog)
        self.equalButton.setMinimumSize(QtCore.QSize(59, 89))
        self.equalButton.setMaximumSize(QtCore.QSize(59, 89))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.equalButton.setFont(font)
        self.equalButton.setObjectName("equalButton")
        self.gridLayout.addWidget(self.equalButton, 5, 5, 1, 1)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.clearAllButton.setText(_translate("Dialog", "Clear All"))
        self.clearButton.setText(_translate("Dialog", "Clear"))
        self.eight.setText(_translate("Dialog", "8"))
        self.backspaceButton.setText(_translate("Dialog", "Backspace"))
        self.clearMemoryButton.setText(_translate("Dialog", "MC"))
        self.seven.setText(_translate("Dialog", "7"))
        self.setMemoryButton.setText(_translate("Dialog", "MS"))
        self.nine.setText(_translate("Dialog", "9"))
        self.squareRootButton.setText(_translate("Dialog", "Sqrt"))
        self.four.setText(_translate("Dialog", "4"))
        self.divisionButton.setText(_translate("Dialog", "/"))
        self.timesButton.setText(_translate("Dialog", "*"))
        self.five.setText(_translate("Dialog", "5"))
        self.powerButton.setText(_translate("Dialog", "X^2"))
        self.six.setText(_translate("Dialog", "6"))
        self.readMemoryButton.setText(_translate("Dialog", "MR"))
        self.one.setText(_translate("Dialog", "1"))
        self.two.setText(_translate("Dialog", "2"))
        self.three.setText(_translate("Dialog", "3"))
        self.minusButton.setText(_translate("Dialog", "-"))
        self.addToMemoryButton.setText(_translate("Dialog", "M+"))
        self.reciprocalButton.setText(_translate("Dialog", "1/x"))
        self.zero.setText(_translate("Dialog", "0"))
        self.dot.setText(_translate("Dialog", "."))
        self.plusButton.setText(_translate("Dialog", "+"))
        self.changeSignButton.setText(_translate("Dialog", "+-"))
        self.equalButton.setText(_translate("Dialog", "="))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

