'''
Created on Feb 13, 2016
a
'''

from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport
from nn.perc import Perceptron 

class Glavni(QMainWindow):
    
    def __init__(self, parent=None):
        super(Glavni,self).__init__()
        self.initUI()
            
 
        
        c = Cortex()
        n1 = c.addSoma(2)
        n2 = c.addSoma(2)
        n3 = c.addSoma(2)
        c.addSyn(n1, n3, 1);
        c.addSyn(n2, n3, 1);
        n1.activate();
        n2.activate();
        c.tempo();
        
        print n3
        
        self.p = Perceptron([4,6,6,4],1);
        
        inputSet = [ 
                     [1,1,0,0],
                     [0,0,1,1],
                     [1,0,0,0],
                     [0,0,0,0],
                     [1,0,0,1],
                     [1,0,1,1],
                     [1,0,1,0],
                     [1,0,1,0],
                     [1,1,0,1],
                     [1,1,1,0],
                     [1,1,1,1],
                     [0,1,0,0],
                     [0,1,0,1],
                     [0,1,1,0],
                     [0,1,1,1],
                     [0,0,1,0],
                     [0,0,0,1]
                   ]
        outputSet= [ 
                     [1,0,0,0],
                     [0,0,0,1],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0],
                     [0,0,0,0]
                     
                   ]
        
        self.p.train(inputSet, outputSet);
        self.p.cortex.treningOff()
        self.p.proveri(inputSet, outputSet);
        
        #self.p.setInput([0,0,1,1])
        #self.p.calc()
        #self.p.tempo()
        #self.p.tempo()
        #self.p.tempo()
        self.p.stat()   

    def initUI(self):
        #self.setWindowIcon(QIcon('images/gear_blue.ico'))
        self.setWindowState(Qt.WindowMaximized)
        self.setWindowTitle('NIMI')
        self.show()
        self.ctimer = QTimer()
        QObject.connect(self.ctimer, SIGNAL("timeout()"), self.timeUpdate)
        self.ctimer.start(500)
        self.ctimer2 = QTimer()

 
    def closeEvent(self, event):
        print("zatvaram")
        
    def timeUpdate(self):
        #self.p.tempo()   
        self.repaint()
    def paintEvent(self, QPaintEvent):
        paint = QPainter(self)
        paint.setRenderHint(QPainter.Antialiasing)
        self.p.cortex.draw(paint)
        
    def mousePressEvent(self, event):
    
        #- event.pos()
        self.repaint()
    
    def mouseMoveEvent(self, event):
        self.repaint()
    
    def mouseReleaseEvent(self, event):
        self.repaint()
    
