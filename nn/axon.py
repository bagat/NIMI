'''
Created on Feb 13, 2016

@author: nikola
'''
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport

class Synapse(object):

    def __init__(self, n1=None,n2=None,w=1.0):
        '''
        Constructor
        '''
        self.preSyn = n1;
        self.postSyn = n2
        self.W = w;
        self.error = 0
        
        
    def draw(self,paint):
        #painte = QPainter(self)
        x1 = self.preSyn.x + self.preSyn.dx;
        y1 = self.preSyn.y;
        
        x2 = self.postSyn.x 
        y2 = self.postSyn.y
        if(self.W>0):
            x2 = x2 + 5 
            y2 = y2 -10
            paint.setPen(QPen(Qt.black))
        else:
            x2 = x2 + 5 
            y2 = y2 +5
            paint.setPen(QPen(Qt.black,1 ,Qt.DashDotDotLine))
        paint.drawLine(x1,y1, x2,y2); 
        paint.setPen(QPen(Qt.black))  
        paint.drawEllipse(x2,y2,5,5)
        paint.setPen(QPen(Qt.red))
        paint.drawText(((7*x1+x2)/8),((7*y1+y2)/8), "%.2f" % self.W)  
        paint.setPen(QPen(Qt.black))
        #print str(self.W)  