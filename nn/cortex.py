'''
Created on Feb 13, 2016

@author: nikola
'''
from soma import Soma
from axon import Synapse
from PyQt4.QtGui import * # @UnusedWildImport
from PyQt4.QtCore import * # @UnusedWildImport

class Cortex:
    
    textFont = QFont()    
    
    def __init__(self):
        '''
        Constructor
        '''
        Cortex.textFont.setPixelSize(8)
        self.some = []
        self.synapse = []
        self.count = 0;

    def tempo(self): 
        for syn in self.synapse:
            if(syn.preSyn.active == True):
                syn.postSyn.accumulate(syn,syn.preSyn.output * syn.W)
            else:
                syn.postSyn.accumulate(syn,0) 
        for soma in self.some:
            soma.tempo()
            
    def treningOn(self):
        for soma in self.some:
            soma.trening = True  
            soma.becktrack = []  
            
    def treningOff(self):
        for soma in self.some:
            soma.trening = False          
            
                      
    def __str__(self, *args, **kwargs):
        return "Soma: "+str(len(self.some))+" Syn: "+ str(len(self.synapse))
            
    def addSyn(self,n1,n2,w):
        self.synapse.append(Synapse(n1,n2,w)) 
        
    def addSoma(self,t, x, y, af):
        s = Soma(self.count,t, x, y, af)
        self.count = self.count + 1
        self.some.append(s)
        return s;   
    
    def draw(self,paint):
        paint.setFont(Cortex.textFont);
        paint.setPen(QPen(Qt.black))
        for syn in self.synapse:
            syn.draw(paint);   
        for soma in self.some:
            soma.draw(paint);      