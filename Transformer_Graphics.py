#!/usr/bin/env python
#coding:utf-8
# Author:   --<>
# Purpose: 
# Created: 10/09/2014

import sys
import unittest

from PyQt4 import QtCore, QtGui, QtOpenGL

########################################################################
class TransformerG(QtGui.QWidget):
    """ This wigdet will be inserted into another layout"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        #super(TransformerG,self).__init__(self, parent=None) # Python2
        #super().__init__(self, parent=None) #Python 3
        super().__init__() #Python 3
        
             
        self.view = TransformerView()
        brush=QtGui.QBrush(QtGui.QColor(240,240,255))
        self.view.setBackgroundBrush(brush)
        layout = QtGui.QVBoxLayout()
        layout.addWidget(self.view)
        self.setLayout(layout)
        
    
    
    
########################################################################
class TransformerView(QtGui.QGraphicsView):
    """"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        #super(TransformerView,self).__init__(self) # Python 2
        #super().__init__(self) # Python 3
        super().__init__() # Python 3
        
        self.initView()
        
        
    def initView(self):
        self.scene = TransformerScene()
        self.setSceneRect(0,0,400,400)
        self.setScene(self.scene)
        
        
        
        
########################################################################
class TransformerScene(QtGui.QGraphicsScene):
    """This is where the pieces go"""

    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        #super().__init__(self, parent=None)
        super().__init__()
        
        
        
        first= TransformerItem()
        first.setPos(100,100)
        self.addItem(first)
        
        first2= TransformerItem()
        first2.setPos(200,100)
        self.addItem(first2)        
        
        editbox = QtGui.QSpinBox()
        editbox.setMaximumWidth(50)
        editbox.setValue(1)
        editbox.setPrefix('tap ')
        align = QtCore.Qt.AlignRight
        editbox.setAlignment(align)
        editbox.move(200,200)
        
        self.addWidget(editbox)
        
        
        
    
class TransformerItem(QtGui.QGraphicsItem):
    '''The transformer symbol'''
    
    #----------------------------------------------------------------------
    def __init__(self):
        """Constructor"""
        super().__init__()
        
        
        
    def boundingRect(self):
        penWidth = 2.0
        return QtCore.QRectF(-10 - penWidth / 2, -10 - penWidth / 2,
                      20 + penWidth, 20 + penWidth)
        
        
    def paint(self, painter, option, widget):
        #painter.drawRoundRect(-10, -10, 20, 20, 5,5)
        
        rectangle = QtCore.QRectF(10.0, 20.0, 80.0, 80.0)
        startA= 30*16
        spanA= 360*16
        painter.drawArc(rectangle, startA, spanA)
        
        brush=QtGui.QBrush(QtGui.QColor(150,150,0))
        pen = QtGui.QPen(QtGui.QColor(120,0,200))
        painter.setBrush(brush)
        painter.setPen(pen)
        painter.drawRect(rectangle)
        
        
        rectangle = QtCore.QRectF(10, 50.0, 80.0, 80.0)
        painter.drawArc(rectangle, startA, spanA)
        #painter.
        
        #painter2=QtGui.QPainter()
        
        #painter2.setBrush(brush)
        
        #brush=QtGui.QBrush(QtGui.QColor(150,150,0))
    
        
        
        
        
        
        

if __name__=='__main__':
    app = QtGui.QApplication([])
    ex = TransformerG()
    ex.show()
    app.exec_()