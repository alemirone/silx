# coding: utf-8
# /*##########################################################################
#
# Copyright (c) 2015-2017 European Synchrotron Radiation Facility
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# ###########################################################################*/
"""This module provides a QMainWindow with a 3D scene and associated toolbar.
"""

from __future__ import absolute_import

__authors__ = ["T. Vincent"]
__license__ = "MIT"
__date__ = "26/01/2017"


from silx.gui import qt

from .Plot3DWidget import Plot3DWidget
from .tools import OutputToolBar, InteractiveModeToolBar
from .tools import ViewpointToolButton


class Plot3DWindow(qt.QMainWindow):
    """OpenGL widget with a 3D viewport and an overview."""

    def __init__(self, parent=None):
        super(Plot3DWindow, self).__init__(parent)
        if parent is not None:
            # behave as a widget
            self.setWindowFlags(qt.Qt.Widget)

        self._plot3D = Plot3DWidget()
        self.setCentralWidget(self._plot3D)

        toolbar = InteractiveModeToolBar(parent=self)
        toolbar.setPlot3DWidget(self._plot3D)
        self.addToolBar(toolbar)
        self.addActions(toolbar.actions())

        toolbar = qt.QToolBar(self)
        toolbar.addWidget(ViewpointToolButton(plot3D=self._plot3D))
        self.addToolBar(toolbar)

        toolbar = OutputToolBar(parent=self)
        toolbar.setPlot3DWidget(self._plot3D)
        self.addToolBar(toolbar)
        self.addActions(toolbar.actions())

    def getPlot3DWidget(self):
        """Get the :class:`Plot3DWidget` of this window"""
        return self._plot3D

    # Proxy to Plot3DWidget

    def setProjection(self, projection):
        return self._plot3D.setProjection(projection)

    setProjection.__doc__ = Plot3DWidget.setProjection.__doc__

    def getProjection(self):
        return self._plot3D.getProjection()

    getProjection.__doc__ = Plot3DWidget.getProjection.__doc__

    def centerScene(self):
        return self._plot3D.centerScene()

    centerScene.__doc__ = Plot3DWidget.centerScene.__doc__

    def resetZoom(self):
        return self._plot3D.resetZoom()

    resetZoom.__doc__ = Plot3DWidget.resetZoom.__doc__

    def getBackgroundColor(self):
        return self._plot3D.getBackgroundColor()

    getBackgroundColor.__doc__ = Plot3DWidget.getBackgroundColor.__doc__

    def setBackgroundColor(self, color):
        return self._plot3D.setBackgroundColor(color)

    setBackgroundColor.__doc__ = Plot3DWidget.setBackgroundColor.__doc__
