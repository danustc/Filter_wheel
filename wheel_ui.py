#!/usr/bin/python
import sys
from PyQt5 import QtWidgets,QtCore
from functools import partial
import parallax_design
import wheel

class UI(object):
    def __init__(self, port = 'COM19'): # substitute with your own COM port
        # ---------- Initialize a control and a UI, Generate the UI frame.
        self._control = wheel.Control(port)
        self._app = QtWidgets.QApplication(sys.argv)
        self._window = QtWidgets.QWidget()
        self._window.closeEvent = self.shutDown
        self._ui = parallax_design.Ui_Form()
        self._ui.setupUi(self._window)
        # --------- Specify UI functions ----------
        
        self._ui.radioButton_405OD0.toggled.connect(partial(self.set_405, 0))
        self._ui.radioButton_405OD1.toggled.connect(partial(self.set_405, 1))
        self._ui.radioButton_405OD2.toggled.connect(partial(self.set_405, 2))
        self._ui.radioButton_405OD3.toggled.connect(partial(self.set_405, 3))
        self._ui.radioButton_405OD4.toggled.connect(partial(self.set_405, 4))

        self._ui.radioButton_488OD0.toggled.connect(partial(self.set_488, 0))
        self._ui.radioButton_488OD1.toggled.connect(partial(self.set_488, 1))
        self._ui.radioButton_488OD2.toggled.connect(partial(self.set_488, 2))
        self._ui.radioButton_488OD3.toggled.connect(partial(self.set_488, 3))
        self._ui.radioButton_488OD4.toggled.connect(partial(self.set_488, 4))

        self._ui.radioButton_561OD0.toggled.connect(partial(self.set_561, 0))
        self._ui.radioButton_561OD1.toggled.connect(partial(self.set_561, 1))
        self._ui.radioButton_561OD2.toggled.connect(partial(self.set_561, 2))
        self._ui.radioButton_561OD3.toggled.connect(partial(self.set_561, 3))
        self._ui.radioButton_561OD4.toggled.connect(partial(self.set_561, 4))
        
        self._ui.radioButton_640OD0.toggled.connect(partial(self.set_640, 0))
        self._ui.radioButton_640OD1.toggled.connect(partial(self.set_640, 1))
        self._ui.radioButton_640OD2.toggled.connect(partial(self.set_640, 2))
        self._ui.radioButton_640OD3.toggled.connect(partial(self.set_640, 3))
        self._ui.radioButton_640OD4.toggled.connect(partial(self.set_640, 4))
        

        self._window.show()
        self._app.exec_()

    def set_405(self, n_OD):
        print("Optical density:", 0)
        self._control.set_OD(405, n_OD)


    def set_488(self, n_OD):
        print("Optical density:", 0)
        self._control.set_OD(488, n_OD)


    def set_561(self, n_OD):
        print("Optical density:", 0)
        self._control.set_OD(561, n_OD)
        
    def set_640(self, n_OD):
        print("Optical density:", 0)
        self._control.set_OD(640, n_OD)


    def shutDown(self, event):
        self._app.quit()

#----------------------------The Main Function ---------------------------
def main():
    ui = UI() # generate a UI

if __name__ == '__main__':
    main()
