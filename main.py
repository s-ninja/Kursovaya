
import design
import red
import sys  # sys нужен для передачи argv в QApplication
from PyQt5 import QtWidgets

class ExampleApp(QtWidgets.QMainWindow,design.Ui_MainWindow,red.Ui_MainWindow_1):
    def __init__(self):
        super().__init__()
        self.setupUi(self)



def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = ExampleApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно

    app.exec_()  # и запускаем приложение



if __name__ == '__main__':
    main()