import sys, random
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QPainter, QColor


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Git и желтые окружности')
        self.pushButton.clicked.connect(self.dr)

    def dr(self):
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw(qp)
        qp.end()

    def draw(self, qp):
        for i in range(random.randint(1, 9)):
            r = 255
            g = 211
            b = 0
            lenn = random.randint(1, 130)
            qp.setBrush(QColor(r, g, b))
            qp.drawEllipse(random.randint(0, 600), random.randint(0, 600), lenn, lenn)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    form = MyWidget()
    form.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())