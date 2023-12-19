from krita import DockWidget
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from krita import *
#made by @arcaedex :)

DOCKER_TITLE = 'Turing Patterns'

class TuringPattern(DockWidget):

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Turing_Patterns")
        mainWidget = QWidget(self)
        self.setWidget(mainWidget)

        highpassLabel = QLabel("High Pass")
        self.highpassVal = QSpinBox()
        self.highpassVal.setRange(1, 30)
        self.highpassVal.setSingleStep(1)
        self.highpassVal.setValue(9)

        gausblurLabel = QLabel("Gaussian Blur")
        self.gausblurVal = QSpinBox()
        self.gausblurVal.setRange(1, 40)
        self.gausblurVal.setSingleStep(1)
        self.gausblurVal.setValue(7)

        genButton = QPushButton("Single Iteration", mainWidget) 
        genButton.clicked.connect(self.generate)

        mainWidget.setLayout(QVBoxLayout())
        mainWidget.layout().addWidget(highpassLabel)
        mainWidget.layout().addWidget(self.highpassVal)
        mainWidget.layout().addWidget(gausblurLabel)
        mainWidget.layout().addWidget(self.gausblurVal)
        mainWidget.layout().addWidget(genButton)

    def generate(self):
        application = Krita.instance()
        currentDoc = Krita.instance().activeDocument()
        currentLayer = currentDoc.activeNode()
        highpass = application.filter('gaussianhighpass')
        highpass.configuration().setProperty('blurAmount',self.highpassVal.value())
        highpass.apply(currentLayer, 0,0,currentDoc.width(), currentDoc.height())
        thresh = application.filter('threshold')
        thresh.apply(currentLayer, 0,0,currentDoc.width(), currentDoc.height())
        gausblur = application.filter('gaussian blur')
        gausblur.configuration().setProperty('vertRadius',self.gausblurVal.value())
        gausblur.configuration().setProperty('horizRadius',self.gausblurVal.value())
        gausblur.apply(currentLayer, 0,0,currentDoc.width(), currentDoc.height())
        currentDoc.refreshProjection()

    # notifies when views are added or removed
    # 'pass' means do not do anything
    def canvasChanged(self, canvas):
        pass

Krita.instance().addDockWidgetFactory(DockWidgetFactory("Turing_Patterns", DockWidgetFactoryBase.DockRight, TuringPattern))

