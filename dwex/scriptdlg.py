from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *

class ScriptDlg(QDialog):
    def __init__(self, win):
        QDialog.__init__(self, win, Qt.WindowType.Dialog)
        ly = QVBoxLayout()
        l = QLabel(self)
        l.setText("Provide a Python expression for the \"die\" object:")
        ly.addWidget(l)
        self.text = QPlainTextEdit(self)
        ly.addWidget(self.text)
        buttons = QDialogButtonBox(QDialogButtonBox.StandardButton.Ok|QDialogButtonBox.StandardButton.Cancel, Qt.Orientation.Horizontal, self)
        buttons.accepted.connect(self.accept)
        buttons.rejected.connect(self.reject)
        ly.addWidget(buttons)
        self.setWindowTitle('Condition')
        self.setLayout(ly)

    def accept(self):
        self.py = self.text.document().toPlainText()
        if not self.py:
            QMessageBox(QMessageBox.Icon.Warning, "Error",
                "Please provide a Python expression that inspects the \"die\" object.", QMessageBox.StandardButton.Ok, self).show()
        else:
            try:
                self.cond = compile(self.py, 'inline', 'eval')
                QDialog.accept(self)
            except Exception as exc:
                QMessageBox(QMessageBox.Icon.Warning, "Python error",
                    "Python error: " + format(exc), QMessageBox.StandardButton.Ok, self).show()


    
        
