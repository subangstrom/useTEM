from comtypes.gen import ESVision
from comtypes.client import CreateObject, Constants

from xmlrpc.client import Binary
import xmlrpc.client

import acquisitionservers
import beamcontrol
from guiobjects import *
from acquistionManager import *
from microscope import *
from comtypes.safearray import safearray_as_ndarray

import logging
import enums
import pickle
import numpy as np
import ctypes
import array

"""
Requires numpy 1.15, comtypes 1.17.1

"""

logging.basicConfig(level=logging.INFO)

class Application():
    app = CreateObject("ESVision.Application")

    AcquisitionManager = AcquisitionManager(app)
    ScanningServer = acquisitionservers.ScanningServer(app)
    BeamControl = beamcontrol.BeamControl(app)
    Microscope = Microscope(app)
    CcdServer = acquisitionservers.CcdServer(app)
    objectDisplays = dict()

    _activeDisplayWindow = None

    def _timeStampName(self):
        pass


    def activeDisplayWindow(self):

        window  = self.app.ActiveDisplayWindow()
        self._activeDisplayWindow = DisplayWindow(window)

        return self._activeDisplayWindow.name


    def findDisplayObject(self, path):

        comps = path.split('/')

        window = self.app.FindDisplayWindow(comps[0])
        display = window.FindDisplay(comps[1])
        object = display.FindObject(comps[2])

        return DisplayObject(object).sendable

    def _convertComplexData(self, data):
        """
        This method converts Complex Data into a real and imag components in the image display

        """
        pass

    def createNewImageDisplay(self, size, cal=(0,0,1e-9,1e-9, 0, 0)):

        win = self.app.AddDisplayWindow()
        realDisp = win.AddDisplay("real", ESVision.esImageDisplay, ESVision.esImageDisplayType, ESVision.esSplitRight, 0);

        realDisp.Visible = True

        numPixX = size[0]
        numPixY = size[1]
        calibration = calibration2D(cal)

        realDisp.AddImage('real', numPixX, numPixY, calibration)

        return win.name

    def createNewComplexImageDisplay(self, size, cal=(0,0,1e-9,1e-9, 0, 0)):

        win = self.app.AddDisplayWindow()
        realDisp = win.AddDisplay("real", ESVision.esImageDisplay, ESVision.esImageDisplayType, ESVision.esSplitRight, 0);

        realDisp.Visible = False

        imgDisp = win.AddDisplay("imag", ESVision.esImageDisplay, ESVision.esImageDisplayType, ESVision.esSplitRight, 0);
        imgDisp.Visible = False

        display = win.AddDisplay("display", ESVision.esImageDisplay, ESVision.esImageDisplayType, ESVision.esSplitRight, 0);

        display.Visible = True

        numPixX = size[0]
        numPixY = size[1]

        calibration = calibration2D(cal)

        imgDisp.AddImage('imag', numPixX, numPixY, calibration)
        realDisp.AddImage('real', numPixX, numPixY, calibration)
        display.AddImage('display', numPixX, numPixY, calibration)

        return win.name

    def displayWindowNames(self):
        displayWindows = self.app.DisplayWindowNames()
        displayNames = list()

        for display in enumerate(displayWindows):
            displayNames.append(display)

        return displayNames

    def closeDisplayWindow(self, windowName):
        self.app.CloseDisplayWindow(windowName)

# Helper functions
app = Application().app

def calibration2D(cal):

    return app.Calibration2D(cal[0],cal[1],cal[2],cal[3],cal[4],cal[5])


def complexNumber(r, i):
    return app.ComplexNumber(r,i)

def range2D(range):

    return app.Range2D(range[0], range[1], range[2], range[3])

def position2D(pos):

    return app.Position2D(pos[0], pos[1])

def findDisplayObject(self, path):
    return  self.app.FindDisplayObject(path)


def findDisplayInWindow(app, windowName, displayName):
    displayWindow = app.FindDisplayWindow(windowName)
    display = displayWindow.FindDisplay(displayName)

    return display

    # def FindDisplayObject(self, path):
    #     pass

    # def FindDisplayWindow(self, windowName):
    #     return self.app.FindDisplayWindow(windowName)