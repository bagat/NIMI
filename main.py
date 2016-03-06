'''
Created on Feb 13, 2016


'''

import sys
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
from ui.glavni import Glavni
            
def main():
    #state.sim();
    app = QApplication(sys.argv)
    _ = Glavni()
    rez = app.exec_()
    sys.exit(rez)

if __name__ == '__main__':
    main();
        