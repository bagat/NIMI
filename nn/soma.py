'''
Created on Feb 13, 2016

@author: nikola
'''
import math
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport

class Soma(object):

    siva = QBrush(Qt.gray)
    crvena = QBrush(Qt.red)
    
    def __init__(self,idN, threshold, x , y , af):
        '''
        Constructor
        '''
        self.id = idN
        self.threshold = threshold
        self.input = 0.0
        self.active = False
        self.function = af
        self.output = 0.0
        self.becktrack = []
        self.maxin = 0.0
        self.x = x
        self.y = y
        self.dx = 24
        self.dy = 12     
        
        self.polygon = QPolygon([QPoint(self.x,self.y), 
                                 QPoint(self.x+self.dx,self.y+self.dy),
                                 QPoint(self.x+self.dx,self.y-self.dy),
                                 QPoint(self.x,self.y)])
        self.trening = False
        
    def resetBT(self):
        self.becktrack = []
        
    def accumulate(self,Syn,x):
        self.input = self.input + x  
        if(self.trening==True):
            self.becktrack.append((Syn,x))
            if(self.maxin<x):
                self.maxin = x;   
             
    def activate(self):
        self.active = True
        self.output = 1  
        
    def deactivate(self):
        self.active = False
        self.output = 0                     
    def __str__(self, *args, **kwargs):
        if(self.active == True):
            return str(self.id)+" A input:"+str(self.input)  + " Output:"+str(self.output)
        else:  
            return str(self.id)+" N input:"+str(self.input)  + " Output:"+str(self.output)
    
    def setAF(self,af):    
        self.function = af;    
    
    def tempo(self):
        r,o = self.function(self.threshold,self.input);
        self.input = 0.0  
        self.maxin = 0.0       
        if(r == True):
            self.active = True
            self.output = o    
        else:
            self.active = False
            self.output = o
                           
    @staticmethod
    def AF_threshold(threshold,x):  
        if(x >= threshold):
            return (True,1.0);
        else:
            return (False,0.0);  
        
    @staticmethod
    def AF_Identity(threshold,x):  
        return (True,x);
        
    @staticmethod
    def AF_sigmoid(threshold,x): 
        sig = 1 / (1 + math.exp(-x))
        if(sig>=0.5):
            return (True,sig)
        return(False,sig)
      
    @staticmethod
    def AF_sign(threshold,x):  
        if(x >= threshold):
            return (True,1);
        else:
            return (False,-1);
        
    def draw(self,paint):
        #painte = QPainter(self)
        
        if(self.active):
            paint.setBrush(Soma.crvena)
        else:
            paint.setBrush(Soma.siva) 
            
        paint.drawPolygon(self.polygon)
        #paint.drawPolyline(self.polygon);
        
        paint.drawText(self.x+12,self.y+3, str(self.threshold))
        