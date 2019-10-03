#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
# SPDX-License-Identifier: GPL-3.0
#
##################################################
# GNU Radio Python Flow Graph
# Title: Wff File Test
# Author: Zach Leffke, KJ4QLP
# Description: Wallops Interface, with GUI
#
# Generated: Thu Oct  3 12:11:22 2019
# GNU Radio version: 3.7.12.0
##################################################

if __name__ == '__main__':
    import ctypes
    import sys
    if sys.platform.startswith('linux'):
        try:
            x11 = ctypes.cdll.LoadLibrary('libX11.so')
            x11.XInitThreads()
        except:
            print "Warning: failed to XInitThreads()"

from PyQt4 import Qt
from gnuradio import blocks
from gnuradio import digital
from gnuradio import eng_notation
from gnuradio import gr
from gnuradio.eng_option import eng_option
from gnuradio.filter import firdes
from optparse import OptionParser
import kiss
import pmt
import sys
import vcc
from gnuradio import qtgui


class wff_file_test(gr.top_block, Qt.QWidget):

    def __init__(self):
        gr.top_block.__init__(self, "Wff File Test")
        Qt.QWidget.__init__(self)
        self.setWindowTitle("Wff File Test")
        qtgui.util.check_set_qss()
        try:
            self.setWindowIcon(Qt.QIcon.fromTheme('gnuradio-grc'))
        except:
            pass
        self.top_scroll_layout = Qt.QVBoxLayout()
        self.setLayout(self.top_scroll_layout)
        self.top_scroll = Qt.QScrollArea()
        self.top_scroll.setFrameStyle(Qt.QFrame.NoFrame)
        self.top_scroll_layout.addWidget(self.top_scroll)
        self.top_scroll.setWidgetResizable(True)
        self.top_widget = Qt.QWidget()
        self.top_scroll.setWidget(self.top_widget)
        self.top_layout = Qt.QVBoxLayout(self.top_widget)
        self.top_grid_layout = Qt.QGridLayout()
        self.top_layout.addLayout(self.top_grid_layout)

        self.settings = Qt.QSettings("GNU Radio", "wff_file_test")
        self.restoreGeometry(self.settings.value("geometry").toByteArray())


        ##################################################
        # Variables
        ##################################################
        self.scramble_label = scramble_label = ''
        self.output_label = output_label = ''
        self.kiss_label = kiss_label = ''
        self.hdlc_label = hdlc_label = ''
        self.ax25_label = ax25_label = ''

        ##################################################
        # Blocks
        ##################################################
        self.vcc_qt_hex_text_0_0_0 = vcc.qt_hex_text()
        self._vcc_qt_hex_text_0_0_0_win = self.vcc_qt_hex_text_0_0_0;
        self.top_grid_layout.addWidget(self._vcc_qt_hex_text_0_0_0_win, 2, 3, 1, 2)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 5):
            self.top_grid_layout.setColumnStretch(c, 1)

        self.vcc_qt_hex_text_0_0 = vcc.qt_hex_text()
        self._vcc_qt_hex_text_0_0_win = self.vcc_qt_hex_text_0_0;
        self.top_grid_layout.addWidget(self._vcc_qt_hex_text_0_0_win, 1, 3, 1, 2)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 5):
            self.top_grid_layout.setColumnStretch(c, 1)

        self._scramble_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._scramble_label_formatter = None
        else:
          self._scramble_label_formatter = lambda x: str(x)

        self._scramble_label_tool_bar.addWidget(Qt.QLabel('SCRAMBLE'+": "))
        self._scramble_label_label = Qt.QLabel(str(self._scramble_label_formatter(self.scramble_label)))
        self._scramble_label_tool_bar.addWidget(self._scramble_label_label)
        self.top_grid_layout.addWidget(self._scramble_label_tool_bar, 4, 0, 1, 1)
        for r in range(4, 5):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self._output_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._output_label_formatter = None
        else:
          self._output_label_formatter = lambda x: str(x)

        self._output_label_tool_bar.addWidget(Qt.QLabel('OUTPUT'+": "))
        self._output_label_label = Qt.QLabel(str(self._output_label_formatter(self.output_label)))
        self._output_label_tool_bar.addWidget(self._output_label_label)
        self.top_grid_layout.addWidget(self._output_label_tool_bar, 0, 3, 1, 2)
        for r in range(0, 1):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(3, 5):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.kiss_pdu_to_kiss_0 = kiss.pdu_to_kiss()
        self._kiss_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._kiss_label_formatter = None
        else:
          self._kiss_label_formatter = lambda x: str(x)

        self._kiss_label_tool_bar.addWidget(Qt.QLabel('KISS'+": "))
        self._kiss_label_label = Qt.QLabel(str(self._kiss_label_formatter(self.kiss_label)))
        self._kiss_label_tool_bar.addWidget(self._kiss_label_label)
        self.top_grid_layout.addWidget(self._kiss_label_tool_bar, 1, 0, 1, 1)
        for r in range(1, 2):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.kiss_hdlc_deframer_0 = kiss.hdlc_deframer(check_fcs=True, max_length=300)
        self._hdlc_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._hdlc_label_formatter = None
        else:
          self._hdlc_label_formatter = lambda x: str(x)

        self._hdlc_label_tool_bar.addWidget(Qt.QLabel('HDLC'+": "))
        self._hdlc_label_label = Qt.QLabel(str(self._hdlc_label_formatter(self.hdlc_label)))
        self._hdlc_label_tool_bar.addWidget(self._hdlc_label_label)
        self.top_grid_layout.addWidget(self._hdlc_label_tool_bar, 3, 0, 1, 1)
        for r in range(3, 4):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)
        self.digital_descrambler_bb_0 = digital.descrambler_bb(0x21, 0xFF, 16)
        self.blocks_packed_to_unpacked_xx_0 = blocks.packed_to_unpacked_bb(1, gr.GR_MSB_FIRST)
        self.blocks_file_source_0 = blocks.file_source(gr.sizeof_char*1, '/home/zleffke/Downloads/AX25_Scrambled.dat', False)
        self.blocks_file_source_0.set_begin_tag(pmt.PMT_NIL)
        self._ax25_label_tool_bar = Qt.QToolBar(self)

        if None:
          self._ax25_label_formatter = None
        else:
          self._ax25_label_formatter = lambda x: str(x)

        self._ax25_label_tool_bar.addWidget(Qt.QLabel('AX.25'+": "))
        self._ax25_label_label = Qt.QLabel(str(self._ax25_label_formatter(self.ax25_label)))
        self._ax25_label_tool_bar.addWidget(self._ax25_label_label)
        self.top_grid_layout.addWidget(self._ax25_label_tool_bar, 2, 0, 1, 1)
        for r in range(2, 3):
            self.top_grid_layout.setRowStretch(r, 1)
        for c in range(0, 1):
            self.top_grid_layout.setColumnStretch(c, 1)



        ##################################################
        # Connections
        ##################################################
        self.msg_connect((self.kiss_hdlc_deframer_0, 'out'), (self.kiss_pdu_to_kiss_0, 'in'))
        self.msg_connect((self.kiss_hdlc_deframer_0, 'out'), (self.vcc_qt_hex_text_0_0_0, 'pdus'))
        self.msg_connect((self.kiss_pdu_to_kiss_0, 'out'), (self.vcc_qt_hex_text_0_0, 'pdus'))
        self.connect((self.blocks_file_source_0, 0), (self.blocks_packed_to_unpacked_xx_0, 0))
        self.connect((self.blocks_packed_to_unpacked_xx_0, 0), (self.digital_descrambler_bb_0, 0))
        self.connect((self.digital_descrambler_bb_0, 0), (self.kiss_hdlc_deframer_0, 0))

    def closeEvent(self, event):
        self.settings = Qt.QSettings("GNU Radio", "wff_file_test")
        self.settings.setValue("geometry", self.saveGeometry())
        event.accept()

    def get_scramble_label(self):
        return self.scramble_label

    def set_scramble_label(self, scramble_label):
        self.scramble_label = scramble_label
        Qt.QMetaObject.invokeMethod(self._scramble_label_label, "setText", Qt.Q_ARG("QString", self.scramble_label))

    def get_output_label(self):
        return self.output_label

    def set_output_label(self, output_label):
        self.output_label = output_label
        Qt.QMetaObject.invokeMethod(self._output_label_label, "setText", Qt.Q_ARG("QString", self.output_label))

    def get_kiss_label(self):
        return self.kiss_label

    def set_kiss_label(self, kiss_label):
        self.kiss_label = kiss_label
        Qt.QMetaObject.invokeMethod(self._kiss_label_label, "setText", Qt.Q_ARG("QString", self.kiss_label))

    def get_hdlc_label(self):
        return self.hdlc_label

    def set_hdlc_label(self, hdlc_label):
        self.hdlc_label = hdlc_label
        Qt.QMetaObject.invokeMethod(self._hdlc_label_label, "setText", Qt.Q_ARG("QString", self.hdlc_label))

    def get_ax25_label(self):
        return self.ax25_label

    def set_ax25_label(self, ax25_label):
        self.ax25_label = ax25_label
        Qt.QMetaObject.invokeMethod(self._ax25_label_label, "setText", Qt.Q_ARG("QString", self.ax25_label))


def main(top_block_cls=wff_file_test, options=None):

    from distutils.version import StrictVersion
    if StrictVersion(Qt.qVersion()) >= StrictVersion("4.5.0"):
        style = gr.prefs().get_string('qtgui', 'style', 'raster')
        Qt.QApplication.setGraphicsSystem(style)
    qapp = Qt.QApplication(sys.argv)

    tb = top_block_cls()
    tb.start()
    tb.show()

    def quitting():
        tb.stop()
        tb.wait()
    qapp.connect(qapp, Qt.SIGNAL("aboutToQuit()"), quitting)
    qapp.exec_()


if __name__ == '__main__':
    main()
