'''
Created on Feb 13, 2016

@author: nikola
'''
from nn.cortex import Cortex
from nn.soma import  Soma
import random

class Perceptron(object):
    """ Represent perceptron with variable size of hiden layers
        Minimum number of layers in perceptron = 2
    """
          
    def __init__(self,hidenLayers=[4,4,4,4],threshold = 1.0, x = 100, y = 100):
        """Constructor
        
        hidenLayers (list): 
            Count of soma in each layer.

            Multiple paragraphs are supported in parameter
            descriptions.
            
        threshold (float) set threshold of each soma   
        """
        
        self.cortex = Cortex()
        self.layInput = []
        self.layHiden = []
        self.layOutput = []
        dy = y
        dx = x
        offsety = 100
        offsetx = 100
        self.error = 0.000001;
        self.hidenLayers = hidenLayers
        if(len(hidenLayers)<2):
            self.hidenLayers = []
            return;
        
        for _ in range(0,hidenLayers[0]):
            self.layInput.append(self.cortex.addSoma(threshold,dx,dy,Soma.AF_sigmoid))
            dy = dy + offsety
        dy = y
        dx =  x + (len(hidenLayers)-1) * offsetx
        for _ in range(0,hidenLayers[len(hidenLayers)-1]):   
            self.layOutput.append(self.cortex.addSoma(threshold,dx,dy,Soma.AF_sigmoid))  
            dy = dy + offsety
        dy = y
        dx = x + offsetx                           
        self.layHiden.append(self.layInput)
        for h in range(1,len(hidenLayers)-1):
            hl = []
            for _ in range(0,hidenLayers[h]):
               
                hl.append(self.cortex.addSoma(threshold,dx,dy,Soma.AF_sigmoid))  
                dy = dy + offsety
            dx = dx + offsetx    
            dy = y              
            self.layHiden.append(hl)
        self.layHiden.append(self.layOutput)
        random.seed(400)
        for hl in range(0,len(self.layHiden)-1):   
            for pre in self.layHiden[hl]:
                for pos in self.layHiden[hl+1]:
                    ww = random.uniform(-1.0, 1.0)
                    self.cortex.addSyn(pre, pos, ww);
                          
    
    def calc(self):
        """
        calculation of network output
        """    
        for _ in range(0,len(self.hidenLayers)-1):        
            self.cortex.tempo(); 
            
    def tempo(self):
        """
        calculation of one tempo 
        """    
        self.cortex.tempo(); 
                
    def stat(self):
        """
        prints net statistic
        """
        print self.cortex 
           
    def setInput(self, inputx):
        if(len(inputx)!=len(self.layInput)):
            return
        x = 0
        for n in self.layInput:
            if(inputx[x]>0):
                n.activate();
            else:
                n.deactivate();
            x = x +1   
             
    def ukljuciTrening(self):    
        self.cortex.treningOn()  
    def iskljuciTrening(self):    
        self.cortex.treningOff()
                          
    def train(self,inputSet,outputSet):
        for i in range(1,50):
            print "trening: "+str(i)
            for x in range(0,len(inputSet)):
                self.trainSet(inputSet[x], outputSet[x])
            
 
    def trainSet(self, ulaz, izlaz):
        self.cortex.treningOn()
        for _ in range(0,len(self.hidenLayers)-1):   
            self.setInput(ulaz)     
            self.cortex.tempo(); 
        for n in self.layOutput:
            #calculate error
            pass


            
    def proveri(self,inputSet,outputSet):
            grr = 0
            for x in range(0,len(inputSet)):
                print inputSet[x],"-> ", outputSet[x], 
                gg = self.proveriGreske(inputSet[x], outputSet[x])
                grr = grr + gg
                if(gg==1): 
                    print "greska"
                else:
                    print ''
            print "Test Netacno "+str(grr)+ " od "+str(len(inputSet))
                
    def proveriGreske(self, ulaz, izlaz):
        self.cortex.treningOff()
        
        for _ in range(0,len(self.hidenLayers)-1):   
            self.setInput(ulaz)     
            self.cortex.tempo(); 
        x = 0;
        self.setInput(ulaz) 
       
        for n in self.layOutput:
            print str(n.active),
            if(n.active == True and izlaz[x]==0):
                return 1
            if(n.active == False and izlaz[x]==1):
                return 1
            x = x + 1  
        return 0   
              